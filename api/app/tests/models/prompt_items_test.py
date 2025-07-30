from app.models.prompt_items import PromptItems


def test_new_promptItems():
    # Test.
    result = PromptItems(
        diameter=12742,
        gravity=1.00,
        distance=150,
        temperature=15,
        atmosphere=90,
        water=80,
        terrain=50,
        volcano=60,
        aurora=50,
    )

    # Check.
    assert result is not None
    assert result.diameter == 12742
    assert result.gravity == 1.00
    assert result.distance == 150
    assert result.temperature == 15
    assert result.atmosphere == 90
    assert result.water == 80
    assert result.terrain == 50
    assert result.volcano == 60
    assert result.aurora == 50
