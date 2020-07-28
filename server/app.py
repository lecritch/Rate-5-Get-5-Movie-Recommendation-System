from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def get_home():
    return """
    <html>
        <head>
            <title>Rate 5, Get 5</title>
        </head>
        <body>
            <h1>Rate 5, Get 5</h1>
            <form action="/recs" method="get">
                <table>
                    <tr>
                        <th>Movie Title</th>
                        <th></th>
                        <th></th>
                        <th></th>
                        <th></th>
                        <th></th>
                        <th></th>
                    </tr>
                    <tr>
                        <td>Greenberg</td>
                        <td>
                            <input type="radio" id="g_1" name="g_rating" value="1">
                            <label for="g_1">1</label><br>
                        </td>
                        <td>
                            <input type="radio" id="g_2" name="g_rating" value="2">
                            <label for="g_2">2</label><br>
                        </td>
                        <td>
                            <input type="radio" id="g_3" name="g_rating" value="3">
                            <label for="g_3">3</label><br>
                        </td>
                        <td>
                            <input type="radio" id="g_4" name="g_rating" value="4">
                            <label for="g_4">4</label><br>
                        </td>
                        <td>
                            <input type="radio" id="g_5" name="g_rating" value="5">
                            <label for="g_5">5</label><br>
                        </td>
                        <td>
                            <input type="radio" id="g_na" name="g_rating" value="na">
                            <label for="g_na">na</label><br>
                        </td>
                    </tr>
                    <tr>
                        <td>Failure To Launch</td>
                        <td>
                            <input type="radio" id="ftl_1" name="ftl_rating" value="1">
                            <label for="ftl_1">1</label><br>
                        </td>
                        <td>
                            <input type="radio" id="ftl_2" name="ftl_rating" value="2">
                            <label for="ftl_2">2</label><br>
                        </td>
                        <td>
                            <input type="radio" id="ftl_3" name="ftl_rating" value="3">
                            <label for="ftl_3">3</label><br>
                        </td>
                        <td>
                            <input type="radio" id="ftl_4" name="ftl_rating" value="4">
                            <label for="ftl_4">4</label><br>
                        </td>
                        <td>
                            <input type="radio" id="ftl_5" name="ftl_rating" value="5">
                            <label for="ftl_5">5</label><br>
                        </td>
                        <td>
                            <input type="radio" id="ftl_na" name="ftl_rating" value="na">
                            <label for="ftl_na">na</label><br>
                        </td>
                    </tr>
                    <tr>
                        <td>Sleepless In Seattle</td>
                        <td>
                            <input type="radio" id="sis_1" name="sis_rating" value="1">
                            <label for="sis_1">1</label><br>
                        </td>
                        <td>
                            <input type="radio" id="sis_2" name="sis_rating" value="2">
                            <label for="sis_2">2</label><br>
                        </td>
                        <td>
                            <input type="radio" id="sis_3" name="sis_rating" value="3">
                            <label for="sis_3">3</label><br>
                        </td>
                        <td>
                            <input type="radio" id="sis_4" name="sis_rating" value="4">
                            <label for="sis_4">4</label><br>
                        </td>
                        <td>
                            <input type="radio" id="sis_5" name="sis_rating" value="5">
                            <label for="sis_5">5</label><br>
                        </td>
                        <td>
                            <input type="radio" id="sis_na" name="sis_rating" value="na">
                            <label for="sis_na">na</label><br>
                        </td>
                    </tr>
                    <tr>
                        <td>Due Date</td>
                        <td>
                            <input type="radio" id="dd_1" name="dd_rating" value="1">
                            <label for="dd_1">1</label><br>
                        </td>
                        <td>
                            <input type="radio" id="dd_2" name="dd_rating" value="2">
                            <label for="dd_2">2</label><br>
                        </td>
                        <td>
                            <input type="radio" id="dd_3" name="dd_rating" value="3">
                            <label for="dd_3">3</label><br>
                        </td>
                        <td>
                            <input type="radio" id="dd_4" name="dd_rating" value="4">
                            <label for="dd_4">4</label><br>
                        </td>
                        <td>
                            <input type="radio" id="dd_5" name="dd_rating" value="5">
                            <label for="dd_5">5</label><br>
                        </td>
                        <td>
                            <input type="radio" id="dd_na" name="dd_rating" value="na">
                            <label for="dd_na">na</label><br>
                        </td>
                    </tr>
                    <tr>
                        <td>How Do You Know?</td>
                        <td>
                            <input type="radio" id="hdyk_1" name="hdyk_rating" value="1">
                            <label for="hdyk_1">1</label><br>
                        </td>
                        <td>
                            <input type="radio" id="hdyk_2" name="hdyk_rating" value="2">
                            <label for="hdyk_2">2</label><br>
                        </td>
                        <td>
                            <input type="radio" id="hdyk_3" name="hdyk_rating" value="3">
                            <label for="hdyk_3">3</label><br>
                        </td>
                        <td>
                            <input type="radio" id="hdyk_4" name="hdyk_rating" value="4">
                            <label for="hdyk_4">4</label><br>
                        </td>
                        <td>
                            <input type="radio" id="hdyk_5" name="hdyk_rating" value="5">
                            <label for="hdyk_5">5</label><br>
                        </td>
                        <td>
                            <input type="radio" id="hdyk_na" name="hdyk_rating" value="na">
                            <label for="hdyk_na">na</label><br>
                        </td>
                    </tr>
                    <hr>
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

@app.route("/recs")
def get_recs():
    userId = 1000
    ratings = []
    for key in request.args.keys():
        ratings.append({'userId': userId, 'movieId': key,
                        'rating': request.args.get(key)})
    print(ratings)
    return """
    <html>
        <head>
            <title>Rate 5, Get 5</title>
        </head>
        <body>
            <h1>Rate 5, Get 5</h1>
            <h2>Your Ratings: show ratings</h2>
            <h2>Your Recommendations: show recs</h2>
        </body>
    </html>
        
    """

if __name__ == '__main__':
    app.run()