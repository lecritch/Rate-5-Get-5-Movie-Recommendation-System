from flask import Flask, request, redirect, url_for
import pandas as pd
import pickle
from surprise import Reader, Dataset
from surprise.prediction_algorithms import SVDpp

app = Flask(__name__)

movies = pd.read_csv('../data/mod_movies_lc', index_col=0)
ratings = pd.read_csv('../data/mod_ratings_lc', index_col=0)

with open('../model_files/svd_model.bin', 'rb') as f_in:
    model = pickle.load(f_in)
    f_in.close()
    
## MANUALLY ADD MODEL
# model = SVDpp(n_factors=50, reg_all=0.05, lr_all=0.01)

@app.route('/', methods=['GET', 'POST'])
def get_home():    
    
    if len(request.form) == 5:
        return redirect(url_for('get_recs', data=request.form), code=307)
    
    body = """
    <html>
    <head>
        <title>Rate 5, Get 5</title>
        <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    </head>
    <body>
    	<div class="container">
            <h1>Rate 5, Get 5</h1>
        	<form action="/" method="post">
        """
    
    movie_to_rate = movies.sample(1)
    
    if request.form is not None:
        for key in request.form.keys():
            if request.form[key] == "na":
                continue
            else:
                body += f"""
                <input type="hidden" name="{key}" value="{request.form[key]}">
                """
    
    body +=  f"""
    			<div class="box-1">
	                <h2>Rate this Movie:</h2>
	                <div class="box-2">
			            <h3>{movie_to_rate['title'].values[0]}</h3>
			            	<ul>
				                <li><input type="radio" id="{movie_to_rate['movieId']}_1" name="{movie_to_rate['movieId'].values[0]}" value="1">
				                <label for="{movie_to_rate['movieId']}_1">1</label><br></li>
				                <li><input type="radio" id="{movie_to_rate['movieId']}_2" name="{movie_to_rate['movieId'].values[0]}" value="2">
				                <label for="{movie_to_rate['movieId']}_2">2</label><br></li>
				                <li><input type="radio" id="{movie_to_rate['movieId']}_3" name="{movie_to_rate['movieId'].values[0]}" value="3">
				                <label for="{movie_to_rate['movieId']}_3">3</label><br></li>
				                <li><input type="radio" id="{movie_to_rate['movieId']}_4" name="{movie_to_rate['movieId'].values[0]}" value="4">
				                <label for="{movie_to_rate['movieId']}_4">4</label><br></li>
				                <li><input type="radio" id="{movie_to_rate['movieId']}_5" name="{movie_to_rate['movieId'].values[0]}" value="5">
				                <label for="{movie_to_rate['movieId']}_5">5</label><br></li>
				                <li><input type="radio" id="{movie_to_rate['movieId']}_na" name="{movie_to_rate['movieId'].values[0]}" value="na">
				                <label for="{movie_to_rate['movieId']}_na">na</label><br></li>
				            </ul>
                            """
    
    if len(request.form) == 4:
        body += """
		            	<input class="button" type="submit" value="Get My Recommendations!">
    """
    else:
        body += """
                        <input class="button" type="submit" value="Rate Another">
        """
    
    body += """
    </div>
                </div>      
            </form>
        </div>
    </body>
</html>
"""

    return body

@app.route("/recs", methods=['POST'])
def get_recs():

    body = f"""
    <html>
    <head>
        <title>Your Movie Recommendations</title>
        <link rel="stylesheet" type="text/css" href="/static/css/style_recs.css">
    </head>
    <body>
    	<div class="container">
    		<div class="box-1">
            	<h1>5 Movies, Just For You:</h1>
            </div>
    """      
    userId = 1000
    user_ratings = []
    reader = Reader()
    
    # create list of dictionary items containing user's ratings from previous page
    for movieId in request.form.keys():
        rating_one_movie = {'userId': userId, 'movieId': movieId, 'rating': int(request.form[movieId])}
        user_ratings.append(rating_one_movie)
        
    
#     # add the new ratings to the original movies df
#     combined_ratings = ratings.append(user_ratings, ignore_index=True)
#     data = Dataset.load_from_df(combined_ratings, reader)
    
#     # fit the model to the data with the new user's ratings
# #     model.fit(data.build_full_trainset()) # do we need .build_full_trainset() here? - seems so since it doens't work without
    
#     # create a list of tuples containing the new user's predicted ratings for each movie
#     list_of_movies = []
#     for movieId in ratings['movieId'].unique():
#         print(model.predict(userId, movieId)[3])
#         list_of_movies.append((movieId, model.predict(userId, movieId)[3]))
    
#     # rank the predictions from highest to lowest
#     rank_movies = sorted(list_of_movies, key = lambda x:x[1], reverse=True)
    
#     # grab the top 5 highest predicted ratings
#     top_5 = rank_movies[:5]
    
    # print out the top 5 recommendations

    count = 1
    for movie in user_ratings:
        body += f"""
        <div class="box-2">
            	<h3>{count}. {movies[movies['movieId'] == int(movie['movieId'])]['title'].values[0]}</h3>
            </div>
        """
#         body += f"""<h2>{count}. {movies[movies['movieId'] == movie[0]]['title'].values[0]}</h2>""" ## uncomment once I figure out modelling
        count += 1

    body += f"""
        </div>
    </body>
</html>  
    """
    
    return body


if __name__ == '__main__':
    app.run()
    
    
    
    
    
    
    




#### graveyard code ####

#     if len(request.form) >= 4:
#         body += """
#         <form action="/recs" method="post">
#                """
#     else:


#  for pred in preds:
#         body += f"""
#             <h2>{movies[movies['movieId'] == int(pred.iid)]['title'].values[0]}:  {pred.est}</h2>
#         """



#     n = 5
    
#     while n < 0:
#         for idx, rec in enumerate(user_ratings):
#                 title = movies.loc[movies['movieId'] == int(rec[0])]['title']
#                 print(f'Recommendation # {idx + 1}:  {title}', '\n')
#                 n -= 1
#                 if n == 0:
#                     break


#     preds = model.test(user_ratings)

#     for pred in preds:
#         estimated_rating = pred.est
#         print(estimated_rating)


# ratings = [1, 2, 3, 4, 5]
#     for rating in ratings:
#         body += f"""
#                     <li><form action="/" method="post">
#                     <input type="hidden" name="{movie_to_rate['movieId'].values[0]}" value="{rating}">
#                     <input type="submit" value="{rating}"></form></li>
                    
#                 """