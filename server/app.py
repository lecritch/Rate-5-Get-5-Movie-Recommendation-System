from flask import Flask, request
import pandas as pd
import pickle

app = Flask(__name__)

movies = pd.read_csv('../data/mod_movies_lc', index_col=0)

with open('../model_files/svd_model.bin', 'rb') as f_in:
    model = pickle.load(f_in)
    f_in.close()

@app.route('/')
def get_home():
    five_movies = movies.sample(5)
    body = """
    <html>
        <head>
            <title>Rate 5, Get 5</title>
        </head>
        <body>
            <h1>Rate 5, Get 5</h1>
            <form action="/recs" method="post">
                <table>
                    <tr>
                        <th>Movie Title</th>
                        <th></th>
                        <th></th>
                        <th></th>
                        <th></th>
                        <th></th>
                        <th></th>
                    </tr>"""
    for i, movie in five_movies.iterrows():
        body += f"""
        <tr>
            <td>{movie['title']}</td>
            <td>
                <input type="radio" id="{movie['movieId']}_1" name="{movie['movieId']}" value="1">
                <label for="{movie['movieId']}_1">1</label><br>
            </td>
            <td>
                <input type="radio" id="{movie['movieId']}_2" name="{movie['movieId']}" value="2">
                <label for="{movie['movieId']}_2">2</label><br>
            </td>
            <td>
                <input type="radio" id="{movie['movieId']}_3" name="{movie['movieId']}" value="3">
                <label for="{movie['movieId']}_3">3</label><br>
            </td>
            <td>
                <input type="radio" id="{movie['movieId']}_4" name="{movie['movieId']}" value="4">
                <label for="{movie['movieId']}_4">4</label><br>
            </td>
            <td>
                <input type="radio" id="{movie['movieId']}_5" name="{movie['movieId']}" value="5">
                <label for="{movie['movieId']}_5">5</label><br>
            </td>
            <td>
                <input type="radio" id="{movie['movieId']}_na" name="{movie['movieId']}" value="na">
                <label for="{movie['movieId']}_na">na</label><br>
            </td>
        </tr>
        """
    body += """
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                            
                        <td colspan="4" align="right">
                            <input type="submit" value="Get My 5!">
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
    userId = 1000
    user_ratings = []
    
    for movieId in request.form.keys():
        user_ratings.append((userId, movieId, int(request.form[movieId])))

    preds = model.test(user_ratings)

    for pred in preds:
        estimated_rating = pred.est
        print(estimated_rating)

    body = """
    <html>
        <head>
            <title>Rate 5, Get 5</title>
        </head>
        <body>
            <h1>Based on your ratings, we think your ratings should actually be:</h1>
    """

    for pred in preds:
        body += f"""
            <h2>{movies[movies['movieId'] == int(pred.iid)]['title'].values[0]}:  {pred.est}</h2>
        """

    body += """
        </body>
    </html>  
    """
    
    return body


if __name__ == '__main__':
    app.run()