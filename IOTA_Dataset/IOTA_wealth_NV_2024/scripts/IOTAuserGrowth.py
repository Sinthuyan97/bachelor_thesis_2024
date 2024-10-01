import pandas as pd
import csv
import pathlib
import networkx as nx
import time
import os
from datetime import datetime
from tqdm import tqdm
import ast
import numpy as np
import warnings



if __name__ == "__main__":

    warnings.filterwarnings("ignore")

    load_dir = '/local/scratch/correspondence_network/part1_final_logs/'
    save_dir = '/local/scratch/correspondence_network/part1_final_logs/RC/'

    currencies = ['feathercoin', 'btc_2012', 'btc_sample', 'iota_14days', 'iota', 'monacoin', 'cardano_sample']
    currencies = ['ftc', 'btc', 'mona', 'ada']
    heur = 'h0_h1' 
    ####
    iota_components = '/local/scratch/correspondence_network/part1_final_logs/iota_logs/unweighted/'+heur+'/generated_files/iota_'+heur+'_components.csv'
    
    df_iota_comps=pd.read_csv(iota_components)
    print('Component file in memory..')

    mapAddrEntities = df_iota_comps.iloc[:,[0,2]]
    print('Mapping Address => Entity in memory..')

    addrs = {}
    entities = {}
    coin = 'iota'

    coin_data_dir= '/local/scratch/correspondence_network/part1_code/correspondence_network/data2/TXS_DAY_'
    dir_path = coin_data_dir + coin.upper()+'/'
    df_addrs = pd.read_csv('/local/scratch/correspondence_network/part1_final_logs/iota_logs/unweighted/' + heur + '/generated_files/iota_' + heur + '_address_ids.csv')
    print('Analysed addresses history in memory..')
    files = os.listdir(dir_path)
    # sort the files based on their date
    files = sorted(files, key=lambda x: datetime.strptime(x[:10], '%Y-%m-%d'))
    mapAddrEntities['address_ids'] = mapAddrEntities['address_ids'].apply(lambda x: ast.literal_eval(x))
    #for addr_list in mapAddrEntities:

    tqdm_bar = tqdm(files, desc="processed files")
    col_names = ['nr_addresses','nr_entities']
    
    # Delete the file if it already exists
    if os.path.exists(save_dir+coin+heur+'userGrowth.csv'):
        os.remove(save_dir+coin+heur+'userGrowth.csv')
    with open(save_dir+coin+heur+'userGrowth.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=col_names)
        writer.writeheader()
        for file in files:
            file_path = os.path.join(dir_path, file)
            f = pd.read_csv(file_path)
            #inputs=np.array([item for sublist in f.iloc[:,3].apply(ast.literal_eval).values for item in sublist]) 
            inputs = []
            column_values = f.iloc[:, 3]
            for val in column_values:
                if not val == 'Not found':
                    sublist = ast.literal_eval(val)
                    inputs.extend(sublist)
            inputs = np.array(inputs)

            #outputs=np.array([item for sublist in f.iloc[:,5].apply(ast.literal_eval).values for item in sublist])
            outputs = []
            column_values = f.iloc[:, 5]
            for val in column_values:
                if not val == 'Not found':
                    sublist = ast.literal_eval(val)
                    outputs.extend(sublist)
            outputs = np.array(outputs)
            adx=np.concatenate((inputs, outputs))
            adx=pd.unique(adx)
            for addr in adx: 
                filtered = df_addrs[df_addrs['address'] == addr]
                if not filtered.empty:
                    address_id = filtered['address_id'].iloc[0]
                    addrs[address_id] = 1

                    # Filter the DataFrame based on the input integer
                    filtered_df = mapAddrEntities[mapAddrEntities['address_ids'].apply(lambda x: address_id in x)]
                    
                    entities[filtered_df['component'].values[0]] = 1

                    # Remove the element
                    df_addrs = df_addrs[df_addrs['address'] != addr]

            writer.writerow({'nr_addresses':len(df_addrs),'nr_entities':len(entities)})
            tqdm_bar.update(1)
            