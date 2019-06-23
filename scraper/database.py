import pymongo

def MyMongoClient(uri):
	production_mongouri = uri
	client = pymongo.MongoClient(production_mongouri)
	return client

def ProxyMongoClient(uri):
	production_mongouri = uri
	client = pymongo.MongoClient(production_mongouri)
	return client
