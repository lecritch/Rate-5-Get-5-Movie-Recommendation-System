from flask import Flask, request, redirect, url_for
import pandas as pd


app = Flask(__name__)

movies = pd.read_csv('../data/mod_movies_lc', index_col=0)

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
    
    # randomly select movies to rate
    movie_to_rate = movies.sample(1)
    
    if request.form is not None:
        for key in request.form.keys():
            if request.form[key] == "na":
                continue
            else:
                body += f"""
                <input type="hidden" name="{key}" value="{request.form[key]}">
                """
    
    # code for radio dials
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
    
    # code to change button once user is making their 5th selection
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
    
    # for demo purposes, randomly select 5 movies to recommend
    recommend_5 = movies.sample(5)

    count = 1
    for movie in recommend_5.title:
        body += f"""
        <div class="box-2">
            	<h3>{count}. {movie}</h3>
            </div>
        """
        count += 1

    body += f"""
        </div>
    </body>
</html>  
    """
    
    return body


if __name__ == '__main__':
    app.run()