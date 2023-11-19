from collections import defaultdict

import numpy as np
import DBAdapter as db
import uuid
import base64

def join_encoding_vec(list1, list2, total_size):
    vec = [0] * total_size
    for l in list1:
        vec[l - 1] = 1
    for l in list2:
        vec[l - 1] = -1
    return vec


def join_encoding_mat(list1, list2, total_size):
    result = []
    for l1, l2 in zip(list1, list2):
        result.append(join_encoding_vec(l1, l2, total_size))
    return np.array(result)


def euclidean_distance(vector1, vector2):
    return np.linalg.norm(vector1 - vector2)


def k_closest_vector_indices(target_vector, other_vectors, k):
    distances = [euclidean_distance(target_vector, other_vector) for other_vector in other_vectors]
    sorted_indices = np.argsort(distances)
    k_closest_indices = sorted_indices[:k]
    return k_closest_indices


def create_pref_mat(conn, r_count):
    likes = db.get_likes(conn)
    grouped_data = defaultdict(list)
    for user_id, recipe_id in likes:
        grouped_data[user_id].append(recipe_id)
    likes_per_user = list(grouped_data.values())
    del grouped_data
    dislikes = db.get_dislikes(conn)
    grouped_data = defaultdict(list)
    for user_id, recipe_id in dislikes:
        grouped_data[user_id].append(recipe_id)
    dislikes_per_user = list(grouped_data.values())

    return join_encoding_mat(likes_per_user, dislikes_per_user, r_count)


def create_filter_mask_group(conn, users, r_count):
    user_recipes = db.get_recipes_for_users(conn, users)
    mask = [False] * r_count
    for rec in user_recipes:
        mask[rec['id'] - 1] = True
    return mask


def create_filter_mask(conn, user, r_count):
    return create_filter_mask_group(conn, [user], r_count)


def generate_url_safe_uuid():
    random_uuid = uuid.uuid4()
    uuid_bytes = random_uuid.bytes
    url_safe_uuid = base64.urlsafe_b64encode(uuid_bytes).rstrip(b'=')
    return url_safe_uuid.decode('utf-8')


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]
