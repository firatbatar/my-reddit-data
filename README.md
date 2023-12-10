# My Reddit Usage Data Analysis

## Description

Sabancı University CS210 Intorduction to Data Scince Course Fall 2023-2024 Term Project.  
This project will be an analysis on my own <a href="https://www.reddit.com/" target="_blank">Reddit</a> usage.

## Motivation

While thinking about a project I thought I might analyze my interaction with outside world which is done mostly through social media. Since Reddit is my primary social media platform, I decided to go with that.  
The motivation of this analysis is to gain a deeper understanding of my own Reddit usage patterns. By analyzing the subreddits I'm subscribed to, when I am active in Reddit, and my engagement with posts and comments, I aim to gain insights into my online behavior and interests.

## Data Source

I have two main sources of data:

-   Data that is directly exported from Reddit as a personal [data request](https://www.reddit.com/settings/data-request).
-   Data that is scrapped using [Reddit API](https://www.reddit.com/dev/api/) through a simple Python script using [PRAW](https://github.com/praw-dev/praw) package, following [Reddit's API rules](https://github.com/reddit/reddit/wiki/API). Script is available in `reddit_api_scraping.py` file.

Besides these, in order to create a tag system for subreddits, I have created a Google Form to get tags annotated by hand. I wrote a Apps Script to automatically create a Google Form automatically from the data. Form is available [here](https://forms.gle/cKnMTpAyFxGkHKVy5).

### Requested data

Requested data is in .csv format and contains:

-   Subscribed subreddits
-   Login history
-   Voted posts
-   Voted comments
-   Created posts
-   Created comments

### Reddit API

Using Reddit API, I scrapped the following data:

-   Total number of upvotes and downvotes for each post and comment
-   The score (net upvotes) of each comment
-   Available submission flairs for each subreddit (if exists)
-   Flairs of each post (if exists)

Requested data is read by scraper script and after scrapping, it is saved as new .csv files.

## Data Analysis

### Tools

**[Jupyter Notebook](https://jupyter.org/):** Used for coding and documentation.
**[Pandas](https://pandas.pydata.org/):** Used for data cleaning, filtering, and structuring.  
**[Altair](https://altair-viz.github.io/index.html):** Mainly employed for exploratory data analysis (EDA) and interactive visualizations.  
**[Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/):** Supplementary for visualizations if needed.
**[Numpy](https://numpy.org/):** Used for mathematical operations.
**[Scipy](https://www.scipy.org/):** Used for statistical analysis.
**[distfit](https://github.com/erdogant/distfit)** Used for distribution fitting.


### Stages of Analysis

All the analysis is done in `reddit_usage_analysis.ipynb` file. Notebook is structered and commented in a way that it can be followed easily.

#### Data Cleaning and Structuring

Different .csv files are read and filtered according to the needs of the analysis. Detailed information about the data cleaning and structuring can be found in the notebook `reddit_usage_analysis.ipynb`. But in short:

-   Subscribed subreddits are sorted in lexicographical order. Followed users are removed.
-   Login history is filtered to only include date, month, and day names in GMT+3 timezone.
-   Voted posts and comments are filtered to only include my vote direction, score, flair, sub name, and if I am subscribed to that sub or not.
-   Created posts and comments are filtered to only include score, flair, sub name, if I am subscribed to that sub or not, and date.

#### Visualizations

## Findings

<!-- Template from ChatGPT
Through this analysis, I discovered:

Patterns in subreddit subscriptions and correlations with personal interests or activities.
Insights into my online behavior based on login times and comparison with my class schedule.
Voting patterns on posts/comments, including frequency and preferences based on flairs and vote counts.
Self-reflection on my own contributions through posts/comments and their respective flairs/vote counts.
-->

## Limitations and Future Work

<!-- Template from ChatGPT
Limitations
Data Completeness: Reliability of data collected through APIs and personal data requests might have limitations or missing elements.
Subjectivity: Human annotations may have subjective biases affecting the accuracy of subreddit tags and flairs.
Future Work
Enhanced Data Collection: Implement improved methods to collect more comprehensive and accurate data, reducing missing elements.
Advanced Analysis Techniques: Explore machine learning or advanced analytical methods for deeper insights into behavior patterns.
Longitudinal Analysis: Conduct analysis over a more extended period to observe changes in behavior and interests over time
-->
