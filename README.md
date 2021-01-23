# sentiment_analysis_yandex

## Description

A customer came to your company and needs a solution of the problem of analyzing the sentiment of smartphone reviews. The customer wants you to evaluate the possible performance of such an algorithm on a small test sample (only 100 reviews, without labels). No more data is provided to you.

You have to look at the reviews provided by the customer, collect similar reviews as a training sample, and experiment with setting the problem (label positive and negative examples) so that the result on the customer's reviews is as good as possible (strictly more than 85%).

This project was implemented as part of the 6th online course ["Data analysis project"](https://www.coursera.org/learn/data-analysis-project) of the specialization ["Machine learning and data analysis"](https://www.coursera.org/specializations/machine-learning-data-analysis).

The quality assessment of the trained algorithm is checked using an automatic system in the [Kaggle competition](https://www.kaggle.com/c/morecomplicatedsentiment).

Over 23000 reviews and their scores were collected from the Yandex market to train the model. After data cleaning and preparation part the algorithm was trained on more than 6000 reviews.

The quality of the model on customer's data is 95.5%. 

<img align="center" width="700" height="500" src="/images/Leaderboard.png" />

For demonstrating the work of the model the demo-site on Flask was created.


<table><tr>
<td> <img align="center" width="600" height="300" src="/images/Screenshot1.png" /> </td>
<td> <img align="center" width="600" height="300" src="/images/Screenshot2.png" /> </td>
</tr></table>


## Content

train.json - scraped data form the Yandex market

test.csv - customer's reviews

scraping_of_data_from_Yandex_market.ipynb - jupyter notebook for the web scraping

sentiment_analysis_customer_reviews.ipynb - jupyter notebook with the data preparation and training the model

sentiment_classifier.py, demo.py - elements of the Flask-project

sent_class.pkl - the prediction model

templates folder contains index.html file with the demo-html-page



## How to run?

1. install flask;

2. save locally the current folder;

3. open Terminal (command line);

4. go to the saved folder;

5. run demo:
$ python demo.py

6. open http://0.0.0.0:80/.
(If the application is not running by this URL, check the Terminal.
In most cases the default port might be busy, therefore follow
instructions in Terminal.)
