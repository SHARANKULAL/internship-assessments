# Setup Guide: DBpedia Intelligence Scraper

Follow these steps to deploy the DBpedia monitoring tool on your local environment.

## Step 1: Install Python
Ensure you have Python 3.8+ installed.

## Step 2: Install Libraries
Open your terminal and run:
```bash
pip install requests beautifulsoup4
```

## Step 3: Deployment
Run the scraper script:
```bash
python dbpedia_scraper.py
```

## Step 4: Output
Check the `week4` folder for `dbpedia_knowledge_updates.csv`. This file contains the latest extracted knowledge markers for analysis.
