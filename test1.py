import mysql.connector
import re
from sklearn.tree import DecisionTreeRegressor

# Connect to the database
cnx = mysql.connector.connect(user='kian', password='Kian.py192', host='127.0.0.1', database='fina_project')
cursor = cnx.cursor()
query_result = "SELECT * FROM info;"
cursor.execute(query_result)
result = cursor.fetchall()

# Initialize lists to store features and labels
features = []
labels = []

# Convert input data
for item in result:
    print(item)