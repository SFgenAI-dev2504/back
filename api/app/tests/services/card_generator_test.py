from app.services.card_generator import CardGenerator


def test_calc_level_1_min():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 1000,
        "gravity": 0.0,
        "distance": 50,
        "temperature": -200,
        "atmosphere": 0,
        "water": 0,
        "terrain": 0,
        "volcano": 0,
        "aurora": 0,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 1
    assert result.gravity_level == 1
    assert result.distance_level == 1
    assert result.temperature_level == 1
    assert result.atmosphere_level == 1
    assert result.water_level == 1
    assert result.terrain_level == 1
    assert result.volcano_level == 1
    assert result.aurora_level == 1


def test_calc_level_1_max():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 20900,
        "gravity": 0.5,
        "distance": 545,
        "temperature": -135,
        "atmosphere": 10,
        "water": 10,
        "terrain": 10,
        "volcano": 10,
        "aurora": 10,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 1
    assert result.gravity_level == 1
    assert result.distance_level == 1
    assert result.temperature_level == 1
    assert result.atmosphere_level == 1
    assert result.water_level == 1
    assert result.terrain_level == 1
    assert result.volcano_level == 1
    assert result.aurora_level == 1


def test_calc_level_2_min():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 20901,
        "gravity": 0.51,
        "distance": 546,
        "temperature": -134,
        "atmosphere": 11,
        "water": 11,
        "terrain": 11,
        "volcano": 11,
        "aurora": 11,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 2
    assert result.gravity_level == 2
    assert result.distance_level == 2
    assert result.temperature_level == 2
    assert result.atmosphere_level == 2
    assert result.water_level == 2
    assert result.terrain_level == 2
    assert result.volcano_level == 2
    assert result.aurora_level == 2


def test_calc_level_2_max():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 40800,
        "gravity": 1.0,
        "distance": 1040,
        "temperature": -100,
        "atmosphere": 20,
        "water": 20,
        "terrain": 20,
        "volcano": 20,
        "aurora": 20,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 2
    assert result.gravity_level == 2
    assert result.distance_level == 2
    assert result.temperature_level == 2
    assert result.atmosphere_level == 2
    assert result.water_level == 2
    assert result.terrain_level == 2
    assert result.volcano_level == 2
    assert result.aurora_level == 2


def test_calc_level_3_min():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 40801,
        "gravity": 1.01,
        "distance": 1041,
        "temperature": -99,
        "atmosphere": 21,
        "water": 21,
        "terrain": 21,
        "volcano": 21,
        "aurora": 21,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 3
    assert result.gravity_level == 3
    assert result.distance_level == 3
    assert result.temperature_level == 3
    assert result.atmosphere_level == 3
    assert result.water_level == 3
    assert result.terrain_level == 3
    assert result.volcano_level == 3
    assert result.aurora_level == 3


def test_calc_level_3_max():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 60700,
        "gravity": 1.5,
        "distance": 1535,
        "temperature": -65,
        "atmosphere": 30,
        "water": 30,
        "terrain": 30,
        "volcano": 30,
        "aurora": 30,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 3
    assert result.gravity_level == 3
    assert result.distance_level == 3
    assert result.temperature_level == 3
    assert result.atmosphere_level == 3
    assert result.water_level == 3
    assert result.terrain_level == 3
    assert result.volcano_level == 3
    assert result.aurora_level == 3


def test_calc_level_4_min():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 60701,
        "gravity": 1.51,
        "distance": 1536,
        "temperature": -64,
        "atmosphere": 31,
        "water": 31,
        "terrain": 31,
        "volcano": 31,
        "aurora": 31,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 4
    assert result.gravity_level == 4
    assert result.distance_level == 4
    assert result.temperature_level == 4
    assert result.atmosphere_level == 4
    assert result.water_level == 4
    assert result.terrain_level == 4
    assert result.volcano_level == 4
    assert result.aurora_level == 4


def test_calc_level_4_max():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 80600,
        "gravity": 2.0,
        "distance": 2030,
        "temperature": -30,
        "atmosphere": 40,
        "water": 40,
        "terrain": 40,
        "volcano": 40,
        "aurora": 40,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 4
    assert result.gravity_level == 4
    assert result.distance_level == 4
    assert result.temperature_level == 4
    assert result.atmosphere_level == 4
    assert result.water_level == 4
    assert result.terrain_level == 4
    assert result.volcano_level == 4
    assert result.aurora_level == 4


def test_calc_level_5_min():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 80601,
        "gravity": 2.01,
        "distance": 2031,
        "temperature": -29,
        "atmosphere": 41,
        "water": 41,
        "terrain": 41,
        "volcano": 41,
        "aurora": 41,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 5
    assert result.gravity_level == 5
    assert result.distance_level == 5
    assert result.temperature_level == 5
    assert result.atmosphere_level == 5
    assert result.water_level == 5
    assert result.terrain_level == 5
    assert result.volcano_level == 5
    assert result.aurora_level == 5


def test_calc_level_5_max():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 100500,
        "gravity": 2.5,
        "distance": 2525,
        "temperature": 5,
        "atmosphere": 50,
        "water": 50,
        "terrain": 50,
        "volcano": 50,
        "aurora": 50,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 5
    assert result.gravity_level == 5
    assert result.distance_level == 5
    assert result.temperature_level == 5
    assert result.atmosphere_level == 5
    assert result.water_level == 5
    assert result.terrain_level == 5
    assert result.volcano_level == 5
    assert result.aurora_level == 5


def test_calc_level_6_min():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 100501,
        "gravity": 2.51,
        "distance": 2526,
        "temperature": 6,
        "atmosphere": 51,
        "water": 51,
        "terrain": 51,
        "volcano": 51,
        "aurora": 51,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 6
    assert result.gravity_level == 6
    assert result.distance_level == 6
    assert result.temperature_level == 6
    assert result.atmosphere_level == 6
    assert result.water_level == 6
    assert result.terrain_level == 6
    assert result.volcano_level == 6
    assert result.aurora_level == 6


def test_calc_level_6_max():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 120400,
        "gravity": 3.0,
        "distance": 3020,
        "temperature": 40,
        "atmosphere": 60,
        "water": 60,
        "terrain": 60,
        "volcano": 60,
        "aurora": 60,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 6
    assert result.gravity_level == 6
    assert result.distance_level == 6
    assert result.temperature_level == 6
    assert result.atmosphere_level == 6
    assert result.water_level == 6
    assert result.terrain_level == 6
    assert result.volcano_level == 6
    assert result.aurora_level == 6


def test_calc_level_7_min():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 120401,
        "gravity": 3.01,
        "distance": 3021,
        "temperature": 41,
        "atmosphere": 61,
        "water": 61,
        "terrain": 61,
        "volcano": 61,
        "aurora": 61,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 7
    assert result.gravity_level == 7
    assert result.distance_level == 7
    assert result.temperature_level == 7
    assert result.atmosphere_level == 7
    assert result.water_level == 7
    assert result.terrain_level == 7
    assert result.volcano_level == 7
    assert result.aurora_level == 7


def test_calc_level_7_max():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 140300,
        "gravity": 3.5,
        "distance": 3515,
        "temperature": 95,
        "atmosphere": 70,
        "water": 70,
        "terrain": 70,
        "volcano": 70,
        "aurora": 70,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 7
    assert result.gravity_level == 7
    assert result.distance_level == 7
    assert result.temperature_level == 7
    assert result.atmosphere_level == 7
    assert result.water_level == 7
    assert result.terrain_level == 7
    assert result.volcano_level == 7
    assert result.aurora_level == 7


def test_calc_level_8_min():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 140301,
        "gravity": 3.51,
        "distance": 3516,
        "temperature": 96,
        "atmosphere": 71,
        "water": 71,
        "terrain": 71,
        "volcano": 71,
        "aurora": 71,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 8
    assert result.gravity_level == 8
    assert result.distance_level == 8
    assert result.temperature_level == 8
    assert result.atmosphere_level == 8
    assert result.water_level == 8
    assert result.terrain_level == 8
    assert result.volcano_level == 8
    assert result.aurora_level == 8


def test_calc_level_8_max():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 160200,
        "gravity": 4.0,
        "distance": 4010,
        "temperature": 150,
        "atmosphere": 80,
        "water": 80,
        "terrain": 80,
        "volcano": 80,
        "aurora": 80,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 8
    assert result.gravity_level == 8
    assert result.distance_level == 8
    assert result.temperature_level == 8
    assert result.atmosphere_level == 8
    assert result.water_level == 8
    assert result.terrain_level == 8
    assert result.volcano_level == 8
    assert result.aurora_level == 8


def test_calc_level_9_min():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 160201,
        "gravity": 4.01,
        "distance": 4011,
        "temperature": 151,
        "atmosphere": 81,
        "water": 81,
        "terrain": 81,
        "volcano": 81,
        "aurora": 81,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 9
    assert result.gravity_level == 9
    assert result.distance_level == 9
    assert result.temperature_level == 9
    assert result.atmosphere_level == 9
    assert result.water_level == 9
    assert result.terrain_level == 9
    assert result.volcano_level == 9
    assert result.aurora_level == 9


def test_calc_level_9_max():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 180100,
        "gravity": 4.5,
        "distance": 4505,
        "temperature": 250,
        "atmosphere": 90,
        "water": 90,
        "terrain": 90,
        "volcano": 90,
        "aurora": 90,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 9
    assert result.gravity_level == 9
    assert result.distance_level == 9
    assert result.temperature_level == 9
    assert result.atmosphere_level == 9
    assert result.water_level == 9
    assert result.terrain_level == 9
    assert result.volcano_level == 9
    assert result.aurora_level == 9


def test_calc_level_10_min():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 180101,
        "gravity": 4.51,
        "distance": 4506,
        "temperature": 251,
        "atmosphere": 91,
        "water": 91,
        "terrain": 91,
        "volcano": 91,
        "aurora": 91,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 10
    assert result.gravity_level == 10
    assert result.distance_level == 10
    assert result.temperature_level == 10
    assert result.atmosphere_level == 10
    assert result.water_level == 10
    assert result.terrain_level == 10
    assert result.volcano_level == 10
    assert result.aurora_level == 10


def test_calc_level_10_max():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 200000,
        "gravity": 5.0,
        "distance": 5000,
        "temperature": 500,
        "atmosphere": 100,
        "water": 100,
        "terrain": 100,
        "volcano": 100,
        "aurora": 100,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level == 10
    assert result.gravity_level == 10
    assert result.distance_level == 10
    assert result.temperature_level == 10
    assert result.atmosphere_level == 10
    assert result.water_level == 10
    assert result.terrain_level == 10
    assert result.volcano_level == 10
    assert result.aurora_level == 10


def test_calc_level_1_under():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 999,
        "gravity": -0.01,
        "distance": 49,
        "temperature": -201,
        "atmosphere": -1,
        "water": -1,
        "terrain": -1,
        "volcano": -1,
        "aurora": -1,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level is None
    assert result.gravity_level is None
    assert result.distance_level is None
    assert result.temperature_level is None
    assert result.atmosphere_level is None
    assert result.water_level is None
    assert result.terrain_level is None
    assert result.volcano_level is None
    assert result.aurora_level is None


def test_calc_level_10_over():
    # Given.
    request = {
        "planetName": "test星",
        "diameter": 200001,
        "gravity": 5.01,
        "distance": 5001,
        "temperature": 501,
        "atmosphere": 101,
        "water": 101,
        "terrain": 101,
        "volcano": 101,
        "aurora": 101,
    }
    card_generator = CardGenerator(request)

    # Test.
    result = card_generator.calc_level()

    # Check.
    assert result.diameter_level is None
    assert result.gravity_level is None
    assert result.distance_level is None
    assert result.temperature_level is None
    assert result.atmosphere_level is None
    assert result.water_level is None
    assert result.terrain_level is None
    assert result.volcano_level is None
    assert result.aurora_level is None
