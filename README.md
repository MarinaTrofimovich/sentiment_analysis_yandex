# sentiment_analysis_yandex

# Sentiment analysis for the customer's task

## Description

- Created a tool that predict the sentiment of smartphone's review.

- Scraped over 23000 reviews on smartphones from the Yandex market using Python and Selenium.

- Performed the data cleaning and selection and found the best way of labeling the data (final number of reviews 6500+).

- Optimized pepiline "CountVectorizer(), TfidfTransformer(), LinearSVC()" using RandomizedSearchCV to reach the best model.

- Built a client facing API using Flask.


This project was implemented as part of the 6th online course ["Data analysis project"](https://www.coursera.org/learn/data-analysis-project) of the specialization ["Machine learning and data analysis"](https://www.coursera.org/specializations/machine-learning-data-analysis).

The quality assessment of the trained algorithm is checked using an automatic system in the [Kaggle competition](https://www.kaggle.com/c/morecomplicatedsentiment).

The quality of the model on customer's data is 95.5%. 

<img align="center" width="700" height="500" src="/images/Leaderboard.png" />

For demonstrating the work of the model the demo-site on Flask was created.


<table><tr>
<td> <img align="center" width="600" height="300" src="/images/Screenshot1.png" /> </td>
<td> <img align="center" width="600" height="300" src="/images/Screenshot2.png" /> </td>
</tr></table>


## Content

- ***train.json*** - scraped data form the Yandex market

- ***test.csv*** - customer's reviews

- ***scraping_of_data_from_Yandex_market.ipynb*** - jupyter notebook for the web scraping

- ***sentiment_analysis_customer_reviews.ipynb*** - jupyter notebook with the data preparation and training the model

- ***sentiment_classifier.py, demo.py*** - elements of the Flask-project

- ***sent_class.pkl*** - the prediction model

- ***templates folder*** contains index.html file with the demo-html-page



## How to run?

1. install [flask](https://flask.palletsprojects.com/en/1.1.x/)
```
$ pip install flask
```
2. run demo: 
```
$ python demo.py
```
3. open http://0.0.0.0:80/.

(If the application is not running by this URL, check the Terminal.
In most cases the default port might be busy, therefore follow
instructions in Terminal.)
