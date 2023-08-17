import pandas as pd
from pymongo import MongoClient

data = [
    {'Carro': 'Onix', 'Cor': 'Prata', 'Montadora': 'Chevrolet'},
    {'Carro': 'Polo', 'Cor': 'Branco', 'Montadora': 'Volkswagen'},
    {'Carro': 'Sandero', 'Cor': 'Prata', 'Montadora': 'Renault'},
    {'Carro': 'Fiesta', 'Cor': 'Vermelho', 'Montadora': 'Ford'},
    {'Carro': 'City', 'Cor': 'Preto', 'Montadora': 'Honda'}
]

df = pd.DataFrame(data)

client = MongoClient('mongodb://localhost:27017')

db = client['SPRO']

collection = db['Carros']

collection.insert_many(data)

