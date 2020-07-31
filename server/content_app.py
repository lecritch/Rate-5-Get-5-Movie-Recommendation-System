from flask import Flask, request, redirect, url_for
import pandas as pd
import pickle

import os
import sys

module_path = os.path.abspath(os.path.join(os.pardir))

if module_path not in sys.path:
    sys.path.append(module_path)
    
from src import content_rec as cr

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_home(): 
    content = cr.ContentRecommender()
    
    body = f"""
    <html>
    <head>
        <title>Rate 5, Get 5</title>
        <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    </head>
    <body>
    	<div class="container">
            <h1>If You Like 'Avatar', You Might Also Like</h1>
            <h2>{content.recommend('Avatar (2009)')}</h2>
        	<form action="/" method="post">
            </div>      
        </div>
    </body>
</html>
        """
    
    return body