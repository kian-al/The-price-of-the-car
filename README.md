

# 🚗 Car Price Analysis with Python

This repository contains Python scripts to scrape car pricing data from the *Hamrah Mechanic* website and perform machine learning analysis to estimate or predict car prices.

## 📂 Project Structure

- `hamrah-mechanic_scraping.py`: Scrapes car pricing data from the Hamrah Mechanic website.
- `data_DB.csv`: A CSV file containing the scraped car data.
- `ML_hamrah_mechanic.py`: Applies machine learning algorithms to analyze and model the pricing data.
- `write_file.py`: Handles writing extracted data into the CSV file.

## 🛠️ Requirements

- Python 3.x
- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `scikit-learn`
  - (Install using `pip install -r requirements.txt` if you create one)

## 🚀 How to Use

1. **Scrape the Data:**

   Run the `hamrah-mechanic_scraping.py` script to extract car pricing data from the website and save it into `data_DB.csv`.

   ```bash
   python hamrah-mechanic_scraping.py

    Run Machine Learning Analysis:

    Once the data is collected, use the ML_hamrah_mechanic.py script to apply ML models for training and prediction.

    python ML_hamrah_mechanic.py

⚠️ Notes

    Respect Website Terms: Ensure that your scraping activities comply with the terms of use of the Hamrah Mechanic website.

    Avoid Getting Blocked: Use delays or headers in your requests to prevent getting banned from the website.

🙌 Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements
