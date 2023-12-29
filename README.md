# My Reddit Usage Data Analysis

## Description

Sabancı University CS210 Intorduction to Data Scince Course Fall 2023-2024 Term Project.  
This project will be an analysis on my own <a href="https://www.reddit.com/" target="_blank">Reddit</a> usage.

## Motivation

While thinking about a project I thought I might analyze my interaction with outside world which is done mostly through social media. Since Reddit is my primary social media platform, I decided to go with that.  
The motivation of this analysis is to gain a deeper understanding of my own Reddit usage patterns. By analyzing the subreddits I'm subscribed to, when I am active in Reddit, and my engagement with posts and comments, I aim to gain insights into my online behavior and interests.

### Tools

**[Jupyter Notebook](https://jupyter.org/):** Used for coding and documentation.  
**[Pandas](https://pandas.pydata.org/):** Used for data cleaning, filtering, and structuring.  
**[Altair](https://altair-viz.github.io/index.html):** Mainly employed for exploratory data analysis (EDA) and interactive visualizations.  
**[Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/):** Supplementary for visualizations if needed.  
**[Numpy](https://numpy.org/):** Used for mathematical operations.  
**[Scipy](https://www.scipy.org/):** Used for statistical analysis.  
**[distfit](https://github.com/erdogant/distfit)** Used for distribution fitting.

## Data Source

I have two main sources of data:

-   Data that is directly exported from Reddit as a personal [data request](https://www.reddit.com/settings/data-request).
-   Data that is scrapped using [Reddit API](https://www.reddit.com/dev/api/) through a simple Python script using [PRAW](https://github.com/praw-dev/praw) package, following [Reddit's API rules](https://github.com/reddit/reddit/wiki/API). Script is available in `reddit_api_scraping.py` file.

In addition to these two, in order to create a general content type system for subreddits, I have created a Google Form to get "tags" annotated by human. I wrote a Apps Script to automatically create a Google Form automatically from the data. Form is available [here](https://forms.gle/cKnMTpAyFxGkHKVy5). I have collected **7** responses from my friends. I have basically selected the most common tags three tags for each subreddit but I have applied some more filtering. For details see `reddit_api_scraping.py` file.

### Requested data

Requested data is in .csv format and contains:

-   Subscribed subreddits
-   Login history
-   Voted posts and comments
-   Created posts and comments

### Reddit API

Using Reddit API, I scrapped the following data:

-   The score (net upvotes) for each post and comment that I have voted.
-   The score of each post and comment that I have created.
-   The same script also combines annotated data with the raw data.

Requested data is read by scraper script and after scrapping, it is saved as new .csv files.  

Then the data is processed in `data_process.ipynb` file. Process includes cleaning and structuring the data. For details on every step for each different group of data see the file.

### Data Visualizations

Almost all the visualizations, the ones that are spesisific to an analysis are not here, are made in `data_visualization.ipynb` file. During the EDA, I have created many visualizations to understand the data better and to come up with interesting questions. Not all the visualizations are used and included in the final report. However, all can be found in the notebook.  

I have used Altair for most of the visualizations. Altair is a declarative statistical visualization library for Python, based on Vega. I used Altair because it is very easy to use and it is very powerful, I wanted to create all my visualizations interactive so that EDA and final report is more clear and iteresting.

### Data Analysis

All the analysis is done in `data_analysis.ipynb` file. Notebook is structered and commented in a way that it can be followed easily. In addition to the statistical tests, the notebook also includes some of the visualizations that are used in the report. Again (almost) all the visualizations are made using Altair and they are interactive.

The details of the analysis can be found in the notebook, but the final report is in its [own webiste](https://firatbatar.com/my-reddit-usage).

## Findings

_For the detailed findings, please visit the [report](https://firatbatar.com/my-reddit-usage)._

Through this analysis, I discovered:  
- Patterns in my Reddit usage times and correlations with my class schedule.
- Voting patterns on posts/comments, including preferences based on subreddits and their tags.
- Self-reflection on my own contributions through posts/comments and their respective subreddits and tags.
- The factors that affect the way I interact in Reddit.
- How I start, join, and contribute to discussions on Reddit.

## Limitations

The limitations can be generally seperated into two categories:

### Data Sourced Limitations

**Data Completeness:** Considering my time on Reddit and the way I interact with data is somewhat limited, the data stays a bit short for some the possible analysis.  
**Subjectivity:** Like I have stated Reddit does not have a native system to classify subreddit. Even though I tried to solve this using human annotators, they may have subjective biases affecting the accuracy of subreddit tags.

### Personal Limitations

**Privacy:** Since the project is based on a personal data, I have to be careful about the privacy of the data. There were some details that I did not want to share, so I did not used them in the analysis.  
**Knowledge:** Especially in the first stages of the project, I did not have enough knowledge about data science and data analysis. So, even though I tried to improve the project and the analysis as I learned more, there are still some parts inherited from the early stages of the project and some parts that I could not improve. With more knowledge and experience, and some knowledge about machine learning, I believe the project can be improved.

## Future Work

**Longitudinal Analysis:** Since data is on my usage of a social media plotform, the analysis can be updated with newer data over a more extended period to observe changes in behavior and interests over time.  
**Advanced Analysis Techniques:** With more knowledge and experience on data science and machine learning, if I continue to take courses on the subject, I might return and improve some things that I am not able to do now.  
**Final Report Website:** I have created a website for the final report. However, due to my limited knowledge especially on using Altair, I could not create the website as detailed as I wanted and combine with interactive visualizations. I believe there is some room for improvement there.

