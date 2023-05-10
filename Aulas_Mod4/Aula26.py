#   Aula 26 - Listagem de dados - parte 1

from pymongo import collection
from pymongo import MongoClient


def get_database():
    CONNECTION_STRING = (
        "mongodb+srv://root:<WGRHIth3BzcSS4z1>@cluster0.tnzynwo.mongodb.net/"
    )

    client = MongoClient(CONNECTION_STRING)
    print("Conectado com sucesso!")
    return client["soul_code_db"]

dbname = get_database()
collection_name = dbname["itens_soulcode"]

detalhes_itens = collection_name.find()
#detalhes_itens = collection_name.find({"categoria":"Online"})
#detalhes_itens = collection_name.find({"$or" : [{"categoria":"Online"}, {"categoria":"Físico"}]})
#detalhes_itens = collection_name.find({"$and" : [{"categoria":"Online"}, {"categoria":"Físico"}]})
#detalhes_itens = collection_name.find({"nome_item":{"$regex":"^Mi"}})
for item in detalhes_itens:
    print(item)