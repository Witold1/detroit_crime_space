from typing import Union
import pymongo
pymongo.version

import pandas as pd

from .logger import prepare_logger
logger = prepare_logger()
from tqdm import tqdm


def read_credentials(file_path : str = './data/credentials.txt') -> str:
    '''
    read password and dbname from external file to prepare connector string to pymongo.mongo_client.MongoClient
    # Connect to Your Cluster
    # https://docs.atlas.mongodb.com/tutorial/connect-to-your-cluster/
    # Insert and View Data in Your Cluster -> 
    # https://docs.atlas.mongodb.com/tutorial/insert-data-into-your-cluster/
    
    :Parameters:
    
    input
        - :file_path: file path to credentials to mongo CLUSTER
    return
        - :connect_mongo_string: mongo's string to CLUSTER connection via application
    '''
    import json
    with open(file_path, encoding='utf-8', mode='r') as f:
        json_credentials_dict = json.load(f)
        connect_mongo_string = json_credentials_dict['mongo_string'].format_map(json_credentials_dict)
        return connect_mongo_string
		
def db_connector(connect_mongo_string : str) -> pymongo.mongo_client.MongoClient:
    '''
    connects to cloud database endpoint. connects to CLUSTER and return pymongo.mongo_client.MongoClient or error text
    # Insert and View Data in Your Cluster -> 
    # https://docs.atlas.mongodb.com/tutorial/insert-data-into-your-cluster/
    
    :Parameters:
    
    input
        - :connect_mongo_string: mongo's string to CLUSTER connection via application
    return
        - :client: pymongo.mongo_client.MongoClient
    '''
    if connect_mongo_string is not None: 
        try:
            client = pymongo.MongoClient(connect_mongo_string)
            if client.admin.command('replSetGetStatus')['ok']: logger.info(f'Сonnection to cloud: True')     
            return client
        except pymongo.errors.OperationFailure:
            print(' bad auth Authentication failed.')
            logger.info(f' bad auth Authentication failed.')
			
def insert_per_one_item(collection : pymongo.collection.Collection, container : Union[pd.DataFrame, dict], one : bool = True):
    '''
    insert elements from container to cloud database. get DATABASE.COLLECTION and insert data iterating over container
    # Insert and View Data in Your Cluster -> 
    # https://docs.atlas.mongodb.com/tutorial/insert-data-into-your-cluster/
    
    :Parameters:
    
    input
        - :collection: mongo's DATABASE.COLLECTION
        - :container: DataFrame or dict 
    return
        - :items: container to cloud database
        - :inserted_ids: container of unique ids
    '''
    for item in tqdm(container):
        # theoretically, wi may use update(..., upsert=True) logic or just load the whole base
        # https://pymongo.readthedocs.io/en/stable/tutorial.html#bulk-inserts
        # https://pymongo.readthedocs.io/en/stable/api/index.html
		# PANDAS case https://sricharanphp.blogspot.com/2020/01/insert-pandas-dataframe-into-mongodb.html
        inserted_item_object = collection.insert_one(item)
        # print(inserted_item_object.inserted_id)
		
def insert_many_items(collection : pymongo.collection.Collection, container : Union[pd.DataFrame, dict], one : bool = True):
    '''
    insert elements from container to cloud database. get DATABASE.COLLECTION and insert data iterating over container
    # Insert and View Data in Your Cluster -> 
    # https://docs.atlas.mongodb.com/tutorial/insert-data-into-your-cluster/
    
    :Parameters:
    
    input
        - :collection: mongo's DATABASE.COLLECTION
        - :container: DataFrame or dict 
    return
        - :items: container to cloud database
        - :inserted_ids: container of unique ids
    '''
    # https://docs.mongodb.com/manual/reference/method/db.collection.insertMany/
    inserted_item_object = collection.insert_many(container)
        # print(inserted_item_object.inserted_id)
		
def get_items(collection : pymongo.collection.Collection):
    '''
    find all elements from cloud database. get DATABASE.COLLECTION and iterate with cursor
    # Insert and View Data in Your Cluster -> 
    # https://docs.atlas.mongodb.com/tutorial/insert-data-into-your-cluster/
    
    :Parameters:
    
    input
        - :collection: mongo's DATABASE.COLLECTION
    return
        - :items: container with all items from cloud database
    '''
    db_cursor = collection.find({})
    for item in db_cursor:
        yield item
    logger.info(f'Database got. {collection.database.name}/{collection.name}')
	
def get_many_items(base_name : str ='crimes', collection_name : str ='example'):
    '''
    Downloads all elements from from the cloud database.
    # PANDAS case example https://sricharanphp.blogspot.com/2020/01/insert-pandas-dataframe-into-mongodb.html
    
    :Parameters:
    
    input
        - :base_name: mongo's DATABASE name
        - :collection_name: mongo's DATABASE.COLLECTION name
    return
        - :iterator: downloaded data from DB
    '''
    mongo_string = read_credentials()
    client = db_connector(connect_mongo_string=mongo_string)
    db_database = client[base_name]
    collection = db_database[collection_name]
    # НУЖНА ПРОВЕРКА НА ХОРОШИЙ СТАТУС ПОДКЛЮЧЕНИЯ, вроде 
    
    # collection.Database.MongoClient.connect = True
    # в
    # Collection(Database(MongoClient(host=['cluster0-shard-00-00-biafb.gcp.mongodb.net:27017', 
    # 'cluster0-shard-00-02-biafb.gcp.mongodb.net:27017', 'cluster0-shard-00-01-biafb.gcp.mongodb.net:27017'], 
    # document_class=dict, tz_aware=False, connect=True, ssl=True, replicaset='Cluster0-shard-0', authsource='admin', 
    # retrywrites=True, w='majority'), 'crimes'), 'detroit_2.Database.MongoClient.host')
    
    data_iterator_format = get_items(collection)
    return data_iterator_format
