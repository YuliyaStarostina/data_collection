import gridfs
from pymongo import MongoClient
 
client = MongoClient('mongodb://localhost:27017/')
  
db = client["steam"]

collection = db["games"]

fs = gridfs.GridFS(db)
 
file_data =  open('C:\\Users\Asus\\Desktop\\Обучение\\Сбор и разметка данных\\seminars\\lection_3\\steam_games.json', 'rb')
    
data = file_data.read()
fs.put(file_data, filename='C:\\Users\Asus\\Desktop\\Обучение\\Сбор и разметка данных\\seminars\\lection_3\\steam_games.json')