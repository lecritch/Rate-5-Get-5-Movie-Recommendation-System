from flask import Flask, request, redirect, url_for
import pandas as pd
import pickle
from surprise import Reader, Dataset

app = Flask(__name__)

movies = pd.read_csv('../data/mod_movies_lc', index_col=0)
ratings = pd.read_csv('../data/mod_ratings_lc', index_col=0)

with open('../model_files/svd_model 2.bin', 'rb') as f_in:
    model = pickle.load(f_in)
    f_in.close()


@app.route('/', methods=['GET', 'POST'])
def get_home():
    if len(request.form) == 5:
        return redirect(url_for('get_recs', data=request.form), code=307)

    body = """
    <html>
        <head>
            <title>Rate 5, Get 5</title>
        </head>
        <body>
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

    body += f"""<table>
                    <tr>
                        <th>Movie Title</th>
                    </tr>
        <tr>
            <td>{movie_to_rate['title'].values[0]}</td>
            <td>
                <input type="radio" id="{movie_to_rate['movieId']}_1" name="{movie_to_rate['movieId'].values[0]}" value="1">
                <label for="{movie_to_rate['movieId']}_1">1</label><br>
            </td>
            <td>
                <input type="radio" id="{movie_to_rate['movieId']}_2" name="{movie_to_rate['movieId'].values[0]}" value="2">
                <label for="{movie_to_rate['movieId']}_2">2</label><br>
            </td>
            <td>
                <input type="radio" id="{movie_to_rate['movieId']}_3" name="{movie_to_rate['movieId'].values[0]}" value="3">
                <label for="{movie_to_rate['movieId']}_3">3</label><br>
            </td>
            <td>
                <input type="radio" id="{movie_to_rate['movieId']}_4" name="{movie_to_rate['movieId'].values[0]}" value="4">
                <label for="{movie_to_rate['movieId']}_4">4</label><br>
            </td>
            <td>
                <input type="radio" id="{movie_to_rate['movieId']}_5" name="{movie_to_rate['movieId'].values[0]}" value="5">
                <label for="{movie_to_rate['movieId']}_5">5</label><br>
            </td>
            <td>
                <input type="radio" id="{movie_to_rate['movieId']}_na" name="{movie_to_rate['movieId'].values[0]}" value="na">
                <label for="{movie_to_rate['movieId']}_na">na</label><br>
            </td>
        </tr>
        """

    body += """
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>

                        <td colspan="4" align="right">
                            <input type="submit" value="Rate Another!">
                        </td>
                    </tr>
                </table>
            </form>
        </body>
    </html>
    """
    return body


@app.route("/recs", methods=['POST'])
def get_recs():
    body = f"""
    <html>
        <head>
            <title>Rate 5, Get 5</title>
        </head>
        <body>
            <h1>Based on your ratings, we think your ratings should actually be:</h1>
            <h1>{request.form}</h1>
    """
    userId = 1000
    user_ratings = []
    reader = Reader()

    for movieId in request.form.keys():
        rating_one_movie = {'userId': userId, 'movieId': movieId,
                            'rating': int(request.form[movieId])}
        user_ratings.append(rating_one_movie)

    # preds = model.test(user_ratings)

    #     for pred in preds:
    #         estimated_rating = pred.est
    #         print(estimated_rating)



    # add the new ratings to the original movies df
    combined_ratings = ratings.append(user_ratings, ignore_index=True)
    data = Dataset.load_from_df(combined_ratings, reader)

    model.fit(data.build_full_trainset())

    list_of_movies = []
    for movieId in ratings['movieId'].unique():
        list_of_movies.append((movieId, model.predict(userId, movieId)[3]))

    rank_movies = sorted(list_of_movies, key=lambda x: x[1], reverse=True)

    top_5 = rank_movies[:5]

    #     n = 5

    #     while n < 0:
    #         for idx, rec in enumerate(user_ratings):
    #                 title = movies.loc[movies['movieId'] == int(rec[0])]['title']
    #                 print(f'Recommendation # {idx + 1}:  {title}', '\n')
    #                 n -= 1
    #                 if n == 0:
    #                     break

    for movie in top_5:
        body += f"""
            <h2>{movies[movies['movieId'] == movie[0]}:  {pred.est}</h2>
        """

    body += f"""
    <h1>User ratings dict: {user_ratings}</h1>
    <h1>Rank movies list:  {rank_movies[:5]}</h1>
        </body>
    </html>  
    """

    return body


if __name__ == '__main__':
    app.run()








    #     if len(request.form) >= 4:
    #         body += """
    #         <form action="/recs" method="post">
    #                """
    #     else:


    #  for pred in preds:
    #         body += f"""
    #             <h2>{movies[movies['movieId'] == int(pred.iid)]['title'].values[0]}:  {pred.est}</h2>
    #         """