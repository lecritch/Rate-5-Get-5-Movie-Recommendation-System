# Recommendation Systems Project 

by Dann Moore, Jacob Prebys and Leana Critchell 


<img src="../../src/figures/movielens_logo.png" alt="drawing" width="250"/>


### Overview

We aim to create a recommendation system based on the MovieLens dataset from the GroupLens research lab at the University of Minnesota. Furthermore, we would like to deploy a web app that will alloy a user to enter some ratings for movies that they have seen, and then, based on the model we have implemented, it will reccomend movies that align with their interests. 

### Success Criteria


### Our Data

The datasets used can be found [here](https://grouplens.org/datasets/movielens/latest/). There is a complete dataset available here which includes over 27,000,000 reviews. They also offer a subset of this data that has about 100,000 reviews. For our initial data exploration and model tuning, we will be using this subset.


### Metrics

For this recommendation system, we are provided with actual ratings that actual users gave to movies. Because we have a numerical rating system, the standard metrics for regression problems apply here. Calculating the root mean squared error (RMSE) is a natural choice for model evaluation, but there are problems in practice with this method. Most notably, the movies that have few ratings don't have much affect on the RMSE; therefore, the movies that have a ton of ratings are going to be the most recommended in a model tuned for RMSE. There are other metrics that we are considering--namely NDGC-- and these are more applicable to recommendation systems. More info on these can be found [here](http://fastml.com/evaluating-recommender-systems/)


### Modeling




### Evaluation



### Deployment

To deploy our recommendation system we decided to use the Python library Flask, which is a framework for making simple web-apps backed with Python code. With this tool we were able to make a cool app that will ask users to rate a certain number of movies, and it will recommend films based on similar users' interests.



### Members

|         Name             |                  GitHub          | 
|--------------------------|----------------------------------|
|Leana Critchell           | [lecritch](https://github.com/lecritch)|
|Jacob Prebys              | [jprebys](https://github.com/jprebys)|
|Dann Morr                 | [dannmorr](https://github.com/dannmorr)|
