import pandas as pd
import csv
import time
from tqdm import tqdm
from concurrent import futures
import pymongo
import math
import datetime
import sys


#ada_df = pd.read_csv('/local/scratch/correspondence_network/part1_code/correspondence_network/data2/ada_blockNr_tmpstp.csv')
#ada_df.columns=['blockNr','timestamp']

def replaceAddrsWithIDS(df_trxs,writer,address_id_map,coin):
    lastBlockNr = 0
    lastBlockTmstp = 0
    try:
        for _, trx in df_trxs.iterrows():
            
            if trx['input_addresses_x'] != 'Not found' and trx['output_addresses_y'] != 'Not found':
                if trx['timestamp'] == 'NaN':
                    trx['timestamp'] = trx['output_amounts_y']
                    trx['output_amounts_y'] =trx['output_addresses_y']
                    trx['output_addresses_y'] = trx['input_amounts_x']
                    trx['input_amounts_x'] = trx['input_addresses_x']
                    trx['input_addresses_x'] = trx['block_index']
                    trx['block_index'] = trx['transaction_id']
                    trx['transaction_id'] = trx['Unnamed: 0']
                    
                    ins_address_set = eval(trx['block_index'])
                    trx['input_addresses_x'] = [address_id_map[addr] for addr in ins_address_set]

                    outs_address_set = eval(trx['output_addresses_y'])
                    trx['output_addresses_y'] = [address_id_map[addr] for addr in outs_address_set]
                
                else:
                    ins_address_set = eval(trx['input_addresses_x'])
                    trx['input_addresses_x'] = [address_id_map[addr] for addr in ins_address_set]

                    outs_address_set = eval(trx['output_addresses_y'])
                    trx['output_addresses_y'] = [address_id_map[addr] for addr in outs_address_set]
                
                if coin == 'iota':
                    date_string = trx['timestamp']
                    # Parse the date string into a datetime object
                    dt = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

                    # Convert the datetime object to a Unix timestamp
                    trx['timestamp'] = int(dt.timestamp())
                
                if coin == 'ada': # only for cardano: missing timestamp
                    if math.isnan(trx['timestamp']):
                        if trx['block_index'] == lastBlockNr:
                            trx['timestamp'] = lastBlockTmstp
                        else:
                   #         trx['timestamp'] = ada_df.loc[ada_df['blockNr'] == trx['block_index'], 'timestamp'].iloc[0]
                            lastBlockNr = trx['block_index']
                            lastBlockTmstp = trx['timestamp']
                            

                writer.writerow(trx)
    except Exception as inst:
        print(trx['timestamp'])
        print(trx['transaction_id'])
        print(type(inst))    # the exception type
        print(inst.args)     # arguments stored in .args
        print(inst)
        sys.exit(1)

def createFile(coin):
    try:
        server_data_dir = '/srv/abacus-1/'
        btc_server_dir = '/local/scratch/exported/btc_trxs/'
        target_dir = '/local/scratch/correspondence_network/part1_code/correspondence_network/data2/'

        chunk_size = 10000
        columns=['transaction_id','block_index','input_addresses_x','input_amounts_x','output_addresses_y','output_amounts_y','timestamp']

        print('read map')
        map_df = pd.read_csv('/local/scratch/correspondence_network/part1_code/correspondence_network/data2/map_addrs_'+coin+'.csv')
        address_id_map = dict(zip(map_df['address'], map_df['address_id']))
        print('map in memory')

        if   coin == 'iota':   data_path = server_data_dir + 'iota_tx_data/IOTA_1year_tx_data2.csv'
        elif coin == 'btc':    data_path = server_data_dir + 'btc_trx/BTC_TXS.csv'
        elif coin == 'btc_2012':       data_path = btc_server_dir + 'BTC_TXS_2012.csv'
        elif coin =='ada':     data_path = server_data_dir + 'btc_trx/ADA_TXS.csv'
        elif coin == 'ftc':    data_path = server_data_dir + 'btc_trx/FTC_TXS.csv'
        elif coin == 'mona':   data_path = server_data_dir + 'btc_trx/MONA_TXS.csv'
        else: 
            print('\n\n***** ERROR : Data Path not found for currency ' + cur + '. Check path or pathnames.py file for the entry of this currency ***** \n\n')
        print('STARTED Mapping '+coin+' coin.')

        with open(target_dir+'TXS_with_IDs_'+coin+'.csv', mode='w') as replaceAddr:
            writer = csv.writer(replaceAddr)
            writer.writerow(columns)
            if coin=='ftc' or coin=='mona': 
                for chunk in pd.read_csv(data_path, chunksize=chunk_size, header=None,names=columns):
                    replaceAddrsWithIDS(chunk,writer,address_id_map,coin)
            else:
                for chunk in pd.read_csv(data_path, chunksize=chunk_size):
                    replaceAddrsWithIDS(chunk,writer,address_id_map,coin)
        print('ENDED writing '+coin+' file.')
    except Exception as inst:
        print('createFile')
        
        print(type(inst))    # the exception type
        print(inst.args)     # arguments stored in .args
        print(inst)
        sys.exit(1)
        
if __name__ == "__main__":
    currencies = ['ftc', 'btc', 'iota', 'mona', 'ada']
    currencies = ['iota']
    tqdm_bar = tqdm(currencies, desc="processed files")

    
    with futures.ProcessPoolExecutor(max_workers=32) as ex:
        
        submitted = {ex.submit(createFile, curr) for curr in currencies}

        for fut in futures.as_completed(submitted):
            tqdm_bar.update(1)
    