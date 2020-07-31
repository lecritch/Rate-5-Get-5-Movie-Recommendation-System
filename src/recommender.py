

def main():
    
    #instantialize reader
    from surprise import Reader, Dataset
    reader = Reader()
    
    # get the movies and ratings data
    movies, ratings = load_and_process_data()
    
    # get new ratings from new user 0
    new_user_ratings = movie_rater(movies)
    
    # add new user 0 ratings to original ratings dataset
    new_ratings_df = ratings.append(new_user_ratings, ignore_index=True)
    new_data = Dataset.load_from_df(new_ratings_df, reader)
    
    # fit our model to the new dataset
    fit_model = initialize_and_fit_model(new_data)
    
    # make predictions of ratings for all movies for our new user
    list_of_movies = []
    for m_id in ratings['movieId'].unique():
        list_of_movies.append((m_id, fit_model.predict(0,m_id)[3]))
        
    # sort our new user predicted ratings in decending order
    ranked_movies = sorted(list_of_movies, key=lambda x:x[1], reverse=True)
    
    # push our recommendations
    recommended_movies(ranked_movies, movies, 5)
    
    
    
    
def load_and_process_data():
    """
    This function will load in the movie and ratings datasets
    from the data folder
       
    returns:
     - the movies DataFrame
     - the ratings Dataframe
    """
    
    import pandas as pd
    from surprise import Dataset 

    df = pd.read_csv('../data/ratings.csv')
    df = df.drop(columns='timestamp')
    movies = pd.read_csv('../data/movies.csv')
    
    return movies, df




def initialize_and_fit_model(data):
    """
    This function will instantialize and fit the model we choose for 
    our program on our data(including the new user data)
    
    returns:
     - a model that has been fit on our data(including the new user data)
    """
    
    from surprise.prediction_algorithms import SVD
    svd = SVD(n_factors=50, reg_all=0.05)    
    return svd.fit(data.build_full_trainset())
    
    
    
    
    
def movie_rater(movies, num=5, genre=None):
    """
    This function asks a user to input their ratings for <num> amount of movies
    it will return a list of dictionaries representing their ratings
    
    return:
     - list of dicts of the form: 
           [{'userID': userID, 'movieId': movieId, 'rating': rating},
            {'userID': userID, 'movieId': movieId, 'rating': rating},
            ...]
    """
    
    
    # initialize
    userID = 0
    rating_list = []
    
    # begin our input cycle
    while num > 0:
        
        # if a genre is specified, print a random movie of that genre, else print any random movie
        if genre:
            movie = movies[movies['genres'].str.contains(genre)].sample(1)
        else:
            movie = movies.sample(1)
        print(movie)
        
        # ask for rating, if rating is 'n' generate another movie
        rating = input('How do you rate this movie on a scale of 1-5, press n if you have not seen :\n')
        if rating == 'n':
            continue
            
        # if not 'n', add users rating to the list    
        else:
            rating_one_movie = {'userId':userID,'movieId':movie['movieId'].values[0],'rating':rating}
            rating_list.append(rating_one_movie) 
            num -= 1
            
    return rating_list  


def recommended_movies(user_ratings, movie_title_df, n):
    """
    This function will take in all of the predicted user ratings,
    sorted in decending order, and it will print out the top n    
    """
    
    for idx, rec in enumerate(user_ratings):
        title = movie_title_df.loc[movie_title_df['movieId'] == int(rec[0])]['title']
        print('Recommendation # ', idx+1, ': ', title, '\n')
        n-= 1
        if n == 0:
            break
            
            
            
            
            
            
            
            
            
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    