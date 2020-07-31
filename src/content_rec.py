
class ContentRecommender:
    
    
    def __init__(self):
        
        self.similarities, self.titles, self.indices = self.getSims()
    
    
    
    def getSims(self):
        import pandas as pd
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import linear_kernel, cosine_similarity


        meta = pd.read_csv('../data/movies_metadata.csv', low_memory=False).set_index('id')
        movies = pd.read_csv('../data/movies.csv', dtype=object).set_index('movieId')
        links = pd.read_csv('../data/links.csv', dtype=object).set_index('movieId')

        
        meta['imdb_id'] = meta['imdb_id'].str[-7:]
        meta = meta.set_index('imdb_id')
        
        
        movies2 = movies.join(links)
        movies2 = movies2.set_index('imdbId').drop('tmdbId', axis=1)
        
        movies3 = movies2.join(meta.overview).dropna()
        movies3.genres = movies3.genres.apply(lambda x: x.replace('|', ' '))
        movies3['description'] = 2*(movies3.genres + ' ') +  movies3.overview
        
        tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2) ,min_df=0, stop_words='english')
        tfidf_matrix = tf.fit_transform(movies3['description'])
        
        movies3 = movies3.reset_index()
        titles = movies3['title']
        indicies = pd.Series(movies3.index, index=movies3['title'])
        
        
        return linear_kernel(tfidf_matrix, tfidf_matrix), titles, indicies
    
        
        
        
    def recommend(self, title):
        
        
        idx = self.indices[title]
        sim_scores = list(enumerate(self.similarities[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]
        results =  self.titles.iloc[movie_indices]
        
        print(f'Here are some titles similar to {title}')
        print('='*60)
        for num, movie in enumerate(results):
            
            print(num+1, '. ' + movie, sep='')
        print('='*60)
    
    
    
    def random_title(self):
        
        return self.titles.sample().item()
        
        
        