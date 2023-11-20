# My Reddit Usage Data Analysis

## Description  
Sabancı University CS210 Intorduction to Data Scince Course Fall 2023-2024 Term Project.  
This project will be an analysis on my own <a href="https://www.reddit.com/" target="_blank">Reddit</a> usage. 

## Goal  
I will explore the data and try to make analysis on
* subreddits that I am subscribed to,
* subreddits that I am active in,
* the time of my activity,
* types of activity

## Tools  
I will use Python programming language and will work on a IPython Notebook (Jupyter Notebook) file.  
I mainly plan to use libraries
* **PRAW** to access Reddit API
* **Pandas** to structure the data
* **Matplotlib**, **Seaborn** (, and maybe **Altair**) to visualse and visually analyse the data

## Data Collection  
Data is collected in two main ways:
* Data that is directly exported from Reddit as a personal <a href="https://www.reddit.com/settings/data-request" target="_blank">data request</a>.  
* Data that is scrapped using <a href="https://www.reddit.com/dev/api/">Reddit API</a> through a simple Python script using <a href="https://github.com/praw-dev/praw">PRAW</a> package, following <a href="https://github.com/reddit/reddit/wiki/API">Reddit's API rules</a>.  

Note that .csv files in <a href="/data/" style="text-decoration: none;">data</a> folder are a combination of requested, scrapped and even some filtered data for the purpose of keeping API keys secret and avoiding scraping the same data every time.
