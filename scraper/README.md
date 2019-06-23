# Scraping Process for All Accounts
You must create your own set env to set database and proxy database URI's

1. cd scraper/
2. python3 -m venv env
3. source env/bin/activate
4. pip install -r requirements.txt
5. python app.y

# Testing
1. python generate_test_data.py
2. python app.py -test