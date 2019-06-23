import pymongo
import os
from set_env import set_env
set_env()

def MyMongoClient():
	client = pymongo.MongoClient(os.environ['MONGO_URI'])
	return client

def ProxyMongoClient():
	client = pymongo.MongoClient(os.environ['PROXY_DB_URI'])
	return client
