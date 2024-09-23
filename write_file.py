import mysql.connector
import re
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np
import random
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
    cleaned_text = [re.sub(r'\s*تومان\s*|\s*KM\s*$', '', text) for text in item]
    function = cleaned_text[2]
    if function == "صفر":
        function = function.replace('صفر', '0')  # Convert "صفر" to 0
    function = function.replace(',', '')
    function = int(function)
    year = int(cleaned_text[1])
    
    price = cleaned_text[3].replace(',', '')
    try:
        price = int(price)
    except ValueError:
        continue  # Skip this row if price cannot be converted to an integer
    
    features.append([cleaned_text[0], year, function])
    labels.append(price)

# Convert features to a numpy array
features = np.array(features)

# Use LabelEncoder for the first feature
label_encoder = LabelEncoder()
features[:, 0] = label_encoder.fit_transform(features[:, 0])

# Scale features
scaler = StandardScaler()
features = scaler.fit_transform(features)

# Create and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(features, labels)

# Input car information and make prediction
print('''
    Please enter the information in this way, otherwise the program will not work : 
    15,845-پژو 207-1402    ''')
car_info = input("Please enter the car info: ")
car_info = car_info.strip().split('-')
new_data = [car_info[0], int(car_info[1]), int(car_info[2])]
new_data[0] = label_encoder.transform([new_data[0]])[0]  # Encode the first feature
new_data = scaler.transform([new_data])  # Scale the features
prediction = model.predict(new_data)
rounded_prediction = round(prediction[0])

print("Predicted price:", rounded_prediction)

# Close cursor and connection
cursor.close()
cnx.close()
