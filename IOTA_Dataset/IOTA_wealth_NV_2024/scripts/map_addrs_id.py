import pandas as pd
import csv
import time
from tqdm import tqdm
from concurrent import futures


def map_chunk(df_trxs,id_map):
    try:
        for _, trx in df_trxs.iterrows():
            if trx['timestamp'] == 'NaN':
                input_addresses = eval(trx['block_index']) if trx['block_index'] != 'Not found' else []
                output_addresses = eval(trx['input_amounts_x']) if trx['input_amounts_x'] != 'Not found' else []
            else:
                input_addresses = eval(trx['input_addresses_x']) if trx['input_addresses_x'] != 'Not found' else []
                output_addresses = eval(trx['output_addresses_y']) if trx['output_addresses_y'] != 'Not found' else []
            for addr in input_addresses + output_addresses:
                id_map.append(addr)
        return id_map
    except Exception as inst:
        print('here 2')
        print('trx',trx['transaction_id'])
        print('in',trx['input_addresses_x'])
        print('out',trx['output_addresses_y'])
        print(type(inst))    # the exception type
        print(inst.args)     # arguments stored in .args
        print(inst)
        sys.exit(1)

def mapcoins(coin):
    server_data_dir = '/srv/abacus-1/'
    btc_server_dir = '/local/scratch/exported/btc_trxs/'
    
    chunk_size = 10000
    if   coin == 'iota':   data_path = server_data_dir + 'iota_tx_data/IOTA_1year_tx_data2.csv'
    elif coin == 'btc':    data_path = server_data_dir + 'btc_trx/BTC_TXS.csv'
    elif coin =='ada':     data_path = server_data_dir + 'btc_trx/ADA_TXS.csv'
    elif coin == 'btc_2012':       data_path = btc_server_dir + 'BTC_TXS_2012.csv'
    elif coin == 'ftc':    data_path = server_data_dir + 'btc_trx/FTC_TXS.csv'
    elif coin == 'mona':   data_path = server_data_dir + 'btc_trx/MONA_TXS.csv'
    else: 
        print('\n\n***** ERROR : Data Path not found for currency ' + cur + '. Check path or pathnames.py file for the entry of this currency ***** \n\n')
    print('STARTED Mapping '+coin+' coin.')
    id_map = []
    
    
    try:
        if coin=='ftc' or coin=='mona':
            for chunk in pd.read_csv(data_path, chunksize=chunk_size, header=None):
                chunk.columns=['transaction_id','block_index','input_addresses_x','input_amounts_x','output_addresses_y','output_amounts_y','timestamp']
                id_map = map_chunk(chunk,id_map)    
        else:
            for chunk in pd.read_csv(data_path, chunksize=chunk_size):
                id_map = map_chunk(chunk,id_map)
    except Exception as inst:
        print('here 1')
        raise
        
    print('ENDED Chunking '+coin+' file.')
    id_map=list(set(id_map))
    try:
        with open('/local/scratch/correspondence_network/part1_code/correspondence_network/data2/map_addrs_'+coin+'.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['address_id', 'address'])
            for idx,add in enumerate(id_map):
                writer.writerow([idx, add])
            print('ENDED writing '+coin+' file.')
    except Exception as inst:
        print('issues')
        print(type(inst))    # the exception type
        print(inst.args)     # arguments stored in .args
        print(inst) 
    
   
        
if __name__ == "__main__":
    currencies = ['ftc', 'btc', 'iota', 'mona', 'ada']
    currencies = ['ftc', 'btc', 'mona', 'ada']
    currencies = ['btc_2012']
    tqdm_bar = tqdm(currencies, desc="processed files")

    print('here 1')
    with futures.ProcessPoolExecutor(max_workers=32) as ex:
        
        submitted = {ex.submit(mapcoins, curr) for curr in currencies}

        for fut in futures.as_completed(submitted):
            tqdm_bar.update(1)
    