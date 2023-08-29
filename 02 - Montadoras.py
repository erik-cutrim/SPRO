import pandas as pd
from pymongo import MongoClient

data = [
    {'Montadora': 'Chevrolet', 'País': 'EUA'},
    {'Montadora': 'Volkswagen', 'País': 'Alemanhã'},
    {'Montadora': 'Renault', 'País': 'França'},
    {'Montadora': 'Ford', 'País': 'EUA'},
    {'Montadora': 'Honda', 'País': 'Japão'}
]

df = pd.DataFrame(data)

client = MongoClient('mongodb://localhost:27017')

db = client['SPRO']

collection = db['Montadoras']

collection.insert_many(data)
