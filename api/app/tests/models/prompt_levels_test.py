from app.models.prompt_levels import PromptLevels


def test_new_promptLevels():
    # Test.
    result = PromptLevels(
        diameter_level=1,
        gravity_level=2,
        distance_level=3,
        temperature_level=4,
        atmosphere_level=5,
        water_level=6,
        terrain_level=7,
        volcano_level=8,
        aurora_level=9,
    )

    # Check.
    assert result is not None
    assert result.diameter_level == 1
    assert result.gravity_level == 2
    assert result.distance_level == 3
    assert result.temperature_level == 4
    assert result.atmosphere_level == 5
    assert result.water_level == 6
    assert result.terrain_level == 7
    assert result.volcano_level == 8
    assert result.aurora_level == 9
