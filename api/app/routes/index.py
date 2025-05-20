from time import sleep

from flask import Blueprint, jsonify, request
import random

index_bp = Blueprint('index', __name__)


@index_bp.route('/generate', methods=['GET', 'POST'])
def generate():
    req = request.get_json()
    diameter = req.get("diameter")
    mass = req.get("mass")
    average_distance_from_the_sun = req.get("averageDistanceFromTheSun")
    revolution_period = req.get("revolutionPeriod")
    rotation_period = req.get("rotationPeriod")

    image_urls = [
        "Andromeda_Galaxy.png",
        "Betelgeuse.png",
        "Cat_s_Eye_Nebula.png",
        "Crab_Nebula.png",
        "Horsehead_Nebula.png",
        "Mercury.png",
        "Pillars_of_Creation.png",
        "Sun.png",
        "Venus.png",
        "Whirlpool_Galaxy.png",
    ]

    random.shuffle(image_urls)

    sleep(6)

    result = {
        "data": [
            {
                "id": 1,
                "element1": random.randint(0, 100),
                "element2": random.randint(0, 100),
                "element3": random.randint(0, 100),
                "element4": random.randint(0, 100),
                "element5": random.randint(0, 100),
            },
            {
                "id": 2,
                "element1": random.randint(0, 100),
                "element2": random.randint(0, 100),
                "element3": random.randint(0, 100),
                "element4": random.randint(0, 100),
                "element5": random.randint(0, 100),
            },
        ],
        "imageUrl": "http://localhost:5001/static/images/" + image_urls[0]
    }
    return jsonify(result)
