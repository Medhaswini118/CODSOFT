import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample data for movies and user ratings
ratings_data = {
    'user_id': [1, 1, 2, 2, 3],
    'movie_id': [101, 102, 101, 103, 102],
    'rating': [5, 4, 3, 5, 4]
}

movies_data = {
    'movie_id': [101, 102, 103],
    'title': ['Inception', 'The Matrix', 'Interstellar'],
    'genre': ['Sci-Fi', 'Sci-Fi', 'Sci-Fi'],
    'description': [
        'A thief who steals corporate secrets through dream-sharing technology.',
        'A computer hacker learns about the true nature of his reality.',
        'A team of explorers travel through a wormhole in space.'
    ]
}

# Create DataFrames
ratings_df = pd.DataFrame(ratings_data)
movies_df = pd.DataFrame(movies_data)


# Content-Based Filtering

# Combine genre and description for feature extraction
movies_df['features'] = movies_df['genre'] + " " + movies_df['description']

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['features'])

# Calculate cosine similarity between movies
movie_similarity = cosine_similarity(tfidf_matrix)

def get_content_based_recommendations(movie_title):
    # Get the index of the movie that matches the title
    idx = movies_df[movies_df['title'] == movie_title].index[0]

    # Get pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(movie_similarity[idx]))

    # Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the top 2 most similar movies (excluding itself)
    sim_scores = sim_scores[1:3]

    # Get movie indices
    movie_indices = [i[0] for i in sim_scores]

    return movies_df.iloc[movie_indices][['title', 'genre']]

print("\nContent-Based Filtering Recommendations for 'Inception':")
print(get_content_based_recommendations('Inception'))