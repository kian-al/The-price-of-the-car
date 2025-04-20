# Importing necessary libraries
from sklearn import tree  # For using the Decision Tree algorithm
from sklearn.preprocessing import LabelEncoder  # For encoding car models
import ast  # For converting strings to actual lists

# Defining empty lists to store input data and prices
x = []  # Input features (car model, year, mileage)
y = []  # Car price

# Specifying the file path for data
input_file = "F:/learning/programming/project/back-end/python/The-price-of-the-car/data_DB.csv"

# Opening the data file for reading and processing line by line
with open(input_file, 'r', encoding="utf-8") as file:
    # Reading each line in the file
    for idx, line in enumerate(file):
        try:
            # Converting the string to a real list using ast.literal_eval
            item = ast.literal_eval(line.strip())

            # Extracting the car model, year, mileage, and price from the list
            model = item[0].strip()  # Car model
            year = int(item[1].strip())  # Year of manufacture as an integer
            km_str = item[2].strip().replace(',', '').replace('صفر', '0')  # Cleaning mileage
            km = int(km_str)  # Converting mileage to an integer

            price_str = item[3].strip().replace(',', '')  # Cleaning price
            price = int(price_str)  # Converting price to an integer

            # Appending the features (model, year, mileage) to x and price to y
            x.append([model, year, km])
            y.append(price)
        except Exception as e:
            # In case of an error, print the error and the problematic line
            print(f"⛔ Error in line {idx+1}: {line.strip()} → {e}")
            continue

# Print the number of processed data entries
print(f"\n✅ Number of processed data entries: {len(x)}")

# Encoding the car models to numerical values
le = LabelEncoder()  # Creating an encoder object
models = [row[0] for row in x]  # Extracting car models from the data
encoded_models = le.fit_transform(models)  # Converting the car models to numbers

# Replacing the car model names with their encoded values in the input data
for i in range(len(x)):
    x[i][0] = encoded_models[i]  # Replacing the model with the encoded value

# Training the Decision Tree model using the input data and prices
clf = tree.DecisionTreeClassifier()  # Creating a Decision Tree model
clf = clf.fit(x, y)  # Training the model with the data

# Asking the user for car information
print(f'''
📌 Please enter car information in the following format:
Mileage-Model-Year
Example: 0-Toyota Corolla-2022
''')

# Getting input from the user and processing it
car_info = input("🚗 Car information: ").strip().split('-')

try:
    # Checking the input format (should have three parts)
    if len(car_info) != 3:
        raise ValueError("Incorrect input format. Please enter as 'Mileage-Model-Year'.")

    # Processing mileage, model, and year
    km = int(car_info[0].replace(',', '').replace('صفر', '0'))  # Converting mileage to integer
    model = car_info[1].strip()  # Car model
    year = int(car_info[2].strip())  # Year of manufacture

    # Checking if the model is in the list of encoded models
    if model not in le.classes_:
        print(f"❌ Model '{model}' is not in the database.\n🔍 Valid models: {', '.join(le.classes_)}")
    else:
        # Encoding the model input from the user
        encoded_model = le.transform([model])[0]
        new_data = [[encoded_model, year, km]]  # Preparing new data for prediction

        # Predicting the car price using the trained model
        prediction = clf.predict(new_data)
        print(f"\n💰 Estimated car price: {prediction[0]:,} تومان")  # Displaying the predicted price
except ValueError as ve:
    # Handling errors in case of incorrect input format
    print(f"❌ {ve}")
except Exception as e:
    # Handling other exceptions
    print("❌ Error in processing input:", e)
