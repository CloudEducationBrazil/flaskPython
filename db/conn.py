from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#uri = "mongodb+srv://flavioadm:A1b2C3@provaheleno.fthmkx4.mongodb.net/test"
#uri = "mongodb+srv://guigamoraesmaciel:020219Vg@guigamoraes.4gwqhml.mongodb.net/test" # Guilherme
#uri = "mongodb+srv://arseniomendes20:Ams0210021@googleclouduniruy.fbxtwzh.mongodb.net/test" # Arsenio ok
uri = ""
server_api = ServerApi('1')
try:
    #client = MongoClient(uri, server_api=server_api)
    #client.admin.command('ping')

    print("Sucesso na conexão com o banco de dados")

    #client.close()
except Exception as e:
    print("Falha na conexão com o MongoDB:", e)