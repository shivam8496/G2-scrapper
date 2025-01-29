Step 0 - SetUp VENV using `conda create -p venv python==<Python version>` and then `conda activate` to enter the virtual env
Step 1 - Run test_proxies.py to import all the valid proxies
Step 2 - run "pip install -r requirements.txt" to install all the dependencies
Step 3 - now u can run web_scraper.py to start the script sample command "python web_scraper.py "google" 12-02-2024 5-02-2024"
Step 4- <companyNmae>.json file will be created and the data will be stored in it 

NOTE - There are Some problems in Step-4 because `www.g2.com ` blocks bots , I tried using `undetected_chromedriver` and `Rotated Proxies`but still sometimes bot `web_scraper.py` gets Blocked.Could not comoleye due to time constraints but this can be fixed in future
