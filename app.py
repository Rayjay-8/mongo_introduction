from pymongo import MongoClient
import pprint

# Conectando ao MongoDB
client = MongoClient('mongodb://root:example@localhost:27017')

# Selecionando o banco de dados
db = client['mydatabase']

# Criando uma coleção (tabela)
collection = db['status']

# Inserindo um documento (registro) na coleção
# post = {"author": "ray", "text": "super hacker way 222", "idade": 19}
# collection.insert_one(post)

# status_manifesto = ([
#    {"id": 1, "descricao": "Iniciar", "statusanterios": [0] },
#    {"id": 2, "descricao": "Parar", "statusanterios": [1] },
#    {"id": 3, "descricao": "Erro", "statusanterios": [0, 1, 2 ] },
# ])

# collection.insert_many(status_manifesto)

# Encontrando um documento na coleção
# print(collection.find_one({"id": 2}))

# ABRE O APP
# pprint.pprint(list(collection.find({ "statusanterios": 0}, {"id": 1, "descricao": 1})))

print("-"*20)
# SELECIONOU INICIAR AGORA DEVE MOSTRAR...
# pprint.pprint(list(collection.find({ "statusanterios": 1}, {"id": 1, "descricao": 1})))

print("-"*20)
# SELECIONOU ERRO AGORA DEVE MOSTRAR
# pprint.pprint(list(collection.find(
#    { "statusanterios": 3}, {"id": 1, "descricao": 1}).sort({
#    {"descricao": 1}
# })))

pprint.pprint(list(collection.find(
   {}, {"id": 1, "descricao": 1}).sort({
   "descricao": -1
})))

## faz a soma dos statusanterios

pprint.pprint(list(collection.aggregate([
   { "$group": {"_id": "$statusanterios", "count": {"$sum":1}}},
   {"$unwind": "$statusanterios"}
])))