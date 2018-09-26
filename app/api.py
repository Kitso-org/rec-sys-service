from flask import Flask, request, jsonify
from core.recommender import Recommender
from pythonanyapp import app

recommender = Recommender()


@app.route('/recommendation', methods=['POST'])
def getRecommendation():
    req_data = request.get_json()

    user_id = req_data['user_id']
    n_to_return = req_data['n']

    recommended = recommender.get_top_n_recommended_movies(
        user_id, n_to_return)
    return recommended

@app.route('/teste', methods=['GET'])
def getTest():
    return "Live"
