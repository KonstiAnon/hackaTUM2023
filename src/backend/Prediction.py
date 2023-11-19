import numpy as np
from sklearn.neighbors import KNeighborsRegressor


def predict(data, user_rating, mask, suggestions=4, neighbors=4):
    knn_regressor = KNeighborsRegressor(n_neighbors=neighbors)
    knn_regressor.fit(data, data)
    predicted_ratings = knn_regressor.predict(user_rating)

    # returns list of indices for prediction
    predicted_ratings *= mask
    top_indices = np.argsort(predicted_ratings)[-1, -suggestions::]
    return (top_indices + 1).tolist()
