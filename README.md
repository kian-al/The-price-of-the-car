# 🚗 Car Price Analysis with Python

This repository contains Python scripts to scrape car pricing data from the *Hamrah Mechanic* website and perform machine learning analysis to estimate or predict car prices.

---

## 📂 Project Structure

- `hamrah-mechanic_scraping.py`: Scrapes car pricing data from the Hamrah Mechanic website.
- `data_DB.csv`: A CSV file containing the scraped car data.
- `ML_hamrah_mechanic.py`: Applies a machine learning model (Decision Tree) to analyze and predict car prices based on the dataset.
- `write_file.py`: Handles writing extracted data into the CSV file.

---

## 🛠️ Requirements

- Python 3.x  
- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `scikit-learn`

Install dependencies with:

```bash
pip install -r requirements.txt

🚀 How to Use
1. Scrape the Data

Run the following command to extract car data from the Hamrah Mechanic website:

python hamrah-mechanic_scraping.py

This will generate or update the data_DB.csv file with structured car pricing data.
2. Run the Machine Learning Model

After the data is prepared, use the machine learning script to train the model and interactively predict car prices:

python ML_hamrah_mechanic.py

You will be prompted to enter a car's info in the following format:

[KM driven]-[Model Name]-[Year]
Example: 50000-تویوتا کرولا-2020

The model will then estimate the car's price based on the trained Decision Tree.
🧠 ML Details

    Uses DecisionTreeClassifier from scikit-learn

    Encodes car models using LabelEncoder

    Predicts price based on:

        Car model (categorical, encoded)

        Year of production (integer)

        Kilometers driven (integer)

⚠️ Notes

    Respect Website Terms: Ensure that your scraping activities comply with the terms of use of the Hamrah Mechanic website.

    Avoid Getting Blocked: Use delays or headers in your requests to prevent being blocked.

🙌 Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

📄 Document link: [Canvas Presentation](https://chatgpt.com/canvas/shared/6804c596edac81918d4c2ce7d46e7b20)
