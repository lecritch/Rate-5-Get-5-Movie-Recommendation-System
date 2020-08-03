class ContentRecommender:
    """
    class to be used to make recommendations based of the content of films
    initialize it, and it will generate a similarity matrix for all of the films in
    the movies.csv file in the data folder. Call its recommend() method with a film title
    and it will return the top 10 similar films
    """
    
    
    
    def __init__(self):
        
        self.similarities, self.titles, self.indices = self.getSims()
    
    
    
    def getSims(self):
        
        """
        This method does the bulk of the initialization
        it will import the data, link the data, process the data,
        vectorize the data, and then compute a cosine similarity matrix
        
        returns:
            - A cosine similarity matrix of all pairwise movie combinations
            - A list of movie titles
            - A list of index numbers
        
        """
        import pandas as pd
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

        # read the data into DataFrames
        meta = pd.read_csv('../../data/movies_metadata.csv', low_memory=False).set_index('id')
        movies = pd.read_csv('../../data/movies.csv', dtype=object).set_index('movieId')
        links = pd.read_csv('../../data/links.csv', dtype=object).set_index('movieId')

        # Join the descriptions with their titles in our original dataset
        meta['imdb_id'] = meta['imdb_id'].str[-7:]
        meta = meta.set_index('imdb_id')        
        movies2 = movies.join(links)
        movies2 = movies2.set_index('imdbId').drop('tmdbId', axis=1)
        
        
        # add genre information to the descriptions
        movies3 = movies2.join(meta.overview).dropna()
        movies3.genres = movies3.genres.apply(lambda x: x.replace('|', ' '))
        movies3['description'] = 2*(movies3.genres + ' ') +  movies3.overview
        
        # vectorize the modified descriptions
        tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2) ,min_df=0, stop_words='english')
        tfidf_matrix = tf.fit_transform(movies3['description'])
        
        # remake our list of movies
        movies3 = movies3.reset_index()
        titles = movies3['title']
        indicies = pd.Series(movies3.index, index=movies3['title'])
        
        
        return linear_kernel(tfidf_matrix, tfidf_matrix), titles, indicies
    
        
        
        
    def recommend(self, title):
        """
        This funciton takes in a movie title and isolates the 
        similarity values between it and every other title in our data
        Then by default it prints out the 10 most similar movies
        
        returns:
            nothing
        """
        #sort the similarity scores
        idx = self.indices[title]
        scores = list(enumerate(self.similarities[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        scores = scores[1:11]
        
        #get the movies we want
        movie_indices = [i[0] for i in scores]
        results =  self.titles.iloc[movie_indices]
        
        # print the results in a somewhat nice way
        print(f'Here are some titles similar to {title}')
        print('='*60)
        for num, movie in enumerate(results):            
            print(num+1, '. ' + movie, sep='')
        print('='*60)
    
    
    
    def random_title(self):
        """
        generates a random movie title from the movies dataset
        
        returns:
            -The string title of a random movie
        """
        
        return self.titles.sample().item()
        
        
        