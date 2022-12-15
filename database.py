from pymongo import MongoClient
import certifi 


MONGO_URI ='mongodb+srv://Mongo:mongo@cluster0.59jr2ah.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI,tlsCAFile=ca)
        db = client["bdd_products_app"]
    except ConnectionError:
        print('Error de conexion con la bd')
    return db 