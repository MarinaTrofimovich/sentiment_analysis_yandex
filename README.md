# sentiment_analysis_yandex

# Sentiment analysis for the customer's task

## Description

A customer needs a solution of the problem of analyzing the sentiment of smartphone reviews. He wants to evaluate the possible performance of such an algorithm on a small test sample (only 100 reviews, without labels). No more data is provided.

This project was implemented as part of the 6th online course ["Data analysis project"](https://www.coursera.org/learn/data-analysis-project) of the specialization ["Machine learning and data analysis"](https://www.coursera.org/specializations/machine-learning-data-analysis).

The quality assessment of the trained algorithm is checked using an automatic system in the [Kaggle competition](https://www.kaggle.com/c/morecomplicatedsentiment).

Over 23000 reviews and their scores were collected from the Yandex market as a training sample. After data cleaning, data selection and experimenting with setting the problem (labeling positive and negative examples) the algorithm was trained on more than 6000 reviews.

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
