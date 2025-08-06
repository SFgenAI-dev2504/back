from app.models.prompt_levels import PromptLevels
from app.services.prompt_builder import PromptBuilder

PLANET_NAME = "パワプロクンセイ"


def test_build_ai_image_prompt_mercury():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=1,
        gravity_level=1,
        distance_level=1,
        temperature_level=6,
        atmosphere_level=1,
        water_level=1,
        terrain_level=9,
        volcano_level=2,
        aurora_level=1,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_ai_image_prompt()

    # Check.
    assert (
        result
        == "a tiny planet, with microgravity, orbiting very close to its star. The planet has a temperate climate and with no atmosphere, exposing the bare surface. Its surface is completely dry, with no visible water, with chaotic, heavily cratered landscapes, with extinct volcanoes and hardened lava fields, and with no auroras visible in the sky. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )


def test_build_ai_image_prompt_venus():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=1,
        gravity_level=2,
        distance_level=1,
        temperature_level=10,
        atmosphere_level=10,
        water_level=1,
        terrain_level=5,
        volcano_level=10,
        aurora_level=1,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_ai_image_prompt()

    # Check.
    assert (
        result
        == "a tiny planet, with low gravity, orbiting very close to its star. The planet has a scorched, volcanic surface and with a suffocating atmosphere of dense gases. Its surface is completely dry, with no visible water, with a balanced mix of hills, plains, and shallow valleys, with extreme volcanic activity and a molten landscape, and with no auroras visible in the sky. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )


def test_build_ai_image_prompt_earth():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=1,
        gravity_level=3,
        distance_level=1,
        temperature_level=6,
        atmosphere_level=9,
        water_level=8,
        terrain_level=5,
        volcano_level=6,
        aurora_level=5,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_ai_image_prompt()

    # Check.
    assert (
        result
        == "a tiny planet, with Earth-like gravity, orbiting very close to its star. The planet has a temperate climate and with an extremely thick atmosphere. Its surface is mostly covered in water with vast oceans, with a balanced mix of hills, plains, and shallow valleys, with a few active volcanoes emitting smoke, and with auroras shimmering faintly across the skies. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )


def test_build_ai_image_prompt_mars():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=1,
        gravity_level=1,
        distance_level=1,
        temperature_level=2,
        atmosphere_level=2,
        water_level=1,
        terrain_level=9,
        volcano_level=8,
        aurora_level=2,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_ai_image_prompt()

    # Check.
    assert (
        result
        == "a tiny planet, with microgravity, orbiting very close to its star. The planet has a frigid surface and with a whisper-thin atmosphere. Its surface is completely dry, with no visible water, with chaotic, heavily cratered landscapes, with lava rivers and glowing craters, and with rare, faint auroras near the poles. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )


def test_build_ai_image_prompt_jupiter():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=7,
        gravity_level=6,
        distance_level=2,
        temperature_level=2,
        atmosphere_level=10,
        water_level=1,
        terrain_level=5,
        volcano_level=1,
        aurora_level=10,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_ai_image_prompt()

    # Check.
    assert (
        result
        == "a large planet, with heavy gravity, orbiting close to its star. The planet has a frigid surface and with a suffocating atmosphere of dense gases. Its surface is completely dry, with no visible water, with a balanced mix of hills, plains, and shallow valleys, with no signs of volcanic activity, and with spectacular auroras dancing in all directions. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )


def test_build_ai_image_prompt_saturn():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=6,
        gravity_level=3,
        distance_level=3,
        temperature_level=1,
        atmosphere_level=10,
        water_level=1,
        terrain_level=5,
        volcano_level=1,
        aurora_level=10,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_ai_image_prompt()

    # Check.
    assert (
        result
        == "a medium-large planet, with Earth-like gravity, orbiting at a warm distance. The planet has a deeply frozen surface and with a suffocating atmosphere of dense gases. Its surface is completely dry, with no visible water, with a balanced mix of hills, plains, and shallow valleys, with no signs of volcanic activity, and with spectacular auroras dancing in all directions. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )


def test_build_ai_image_prompt_uranus():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=3,
        gravity_level=2,
        distance_level=6,
        temperature_level=1,
        atmosphere_level=8,
        water_level=1,
        terrain_level=4,
        volcano_level=1,
        aurora_level=10,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_ai_image_prompt()

    # Check.
    assert (
        result
        == "a small planet, with low gravity, orbiting at a cold distance. The planet has a deeply frozen surface and with a heavy atmosphere and frequent storms. Its surface is completely dry, with no visible water, with minor craters and ridges, with no signs of volcanic activity, and with spectacular auroras dancing in all directions. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )


def test_build_ai_image_prompt_neptune():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=3,
        gravity_level=3,
        distance_level=9,
        temperature_level=1,
        atmosphere_level=9,
        water_level=1,
        terrain_level=5,
        volcano_level=1,
        aurora_level=10,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_ai_image_prompt()

    # Check.
    assert (
        result
        == "a small planet, with Earth-like gravity, orbiting extremely far from its star. The planet has a deeply frozen surface and with an extremely thick atmosphere. Its surface is completely dry, with no visible water, with a balanced mix of hills, plains, and shallow valleys, with no signs of volcanic activity, and with spectacular auroras dancing in all directions. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )


def test_build_description_prompt_mercury():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=1,
        gravity_level=1,
        distance_level=1,
        temperature_level=6,
        atmosphere_level=1,
        water_level=1,
        terrain_level=9,
        volcano_level=2,
        aurora_level=1,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_description_prompt()

    # Check.
    assert (
        result
        == "あなたは子ども向けの宇宙図鑑を作る専門家です。次の情報を元に惑星「パワプロクンセイ」の小学生向け図鑑風紹介文を170文字程度で書いてください。この惑星の名前「パワプロクンセイ」から想像できる雰囲気やイメージを少しだけ紹介文に取り入れてください。名前は文の最初に紹介してください。\ndiameter: a tiny planet\ngravity: with microgravity\ndistance: orbiting very close to its star\ntemperature: a temperate climate\natmosphere: with no atmosphere, exposing the bare surface\nwater: completely dry, with no visible water\nterrain: with chaotic, heavily cratered landscapes\nvolcano: with extinct volcanoes and hardened lava fields\naurora: with no auroras visible in the sky"
    )


def test_build_description_prompt_venus():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=1,
        gravity_level=2,
        distance_level=1,
        temperature_level=10,
        atmosphere_level=10,
        water_level=1,
        terrain_level=5,
        volcano_level=10,
        aurora_level=1,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_description_prompt()

    # Check.
    assert (
        result
        == "あなたは子ども向けの宇宙図鑑を作る専門家です。次の情報を元に惑星「パワプロクンセイ」の小学生向け図鑑風紹介文を170文字程度で書いてください。この惑星の名前「パワプロクンセイ」から想像できる雰囲気やイメージを少しだけ紹介文に取り入れてください。名前は文の最初に紹介してください。\ndiameter: a tiny planet\ngravity: with low gravity\ndistance: orbiting very close to its star\ntemperature: a scorched, volcanic surface\natmosphere: with a suffocating atmosphere of dense gases\nwater: completely dry, with no visible water\nterrain: with a balanced mix of hills, plains, and shallow valleys\nvolcano: with extreme volcanic activity and a molten landscape\naurora: with no auroras visible in the sky"
    )


def test_build_description_prompt_earth():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=1,
        gravity_level=3,
        distance_level=1,
        temperature_level=6,
        atmosphere_level=9,
        water_level=8,
        terrain_level=5,
        volcano_level=6,
        aurora_level=5,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_description_prompt()

    # Check.
    assert (
        result
        == "あなたは子ども向けの宇宙図鑑を作る専門家です。次の情報を元に惑星「パワプロクンセイ」の小学生向け図鑑風紹介文を170文字程度で書いてください。この惑星の名前「パワプロクンセイ」から想像できる雰囲気やイメージを少しだけ紹介文に取り入れてください。名前は文の最初に紹介してください。\ndiameter: a tiny planet\ngravity: with Earth-like gravity\ndistance: orbiting very close to its star\ntemperature: a temperate climate\natmosphere: with an extremely thick atmosphere\nwater: mostly covered in water with vast oceans\nterrain: with a balanced mix of hills, plains, and shallow valleys\nvolcano: with a few active volcanoes emitting smoke\naurora: with auroras shimmering faintly across the skies"
    )


def test_build_description_prompt_mars():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=1,
        gravity_level=1,
        distance_level=1,
        temperature_level=2,
        atmosphere_level=2,
        water_level=1,
        terrain_level=9,
        volcano_level=8,
        aurora_level=2,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_description_prompt()

    # Check.
    assert (
        result
        == "あなたは子ども向けの宇宙図鑑を作る専門家です。次の情報を元に惑星「パワプロクンセイ」の小学生向け図鑑風紹介文を170文字程度で書いてください。この惑星の名前「パワプロクンセイ」から想像できる雰囲気やイメージを少しだけ紹介文に取り入れてください。名前は文の最初に紹介してください。\ndiameter: a tiny planet\ngravity: with microgravity\ndistance: orbiting very close to its star\ntemperature: a frigid surface\natmosphere: with a whisper-thin atmosphere\nwater: completely dry, with no visible water\nterrain: with chaotic, heavily cratered landscapes\nvolcano: with lava rivers and glowing craters\naurora: with rare, faint auroras near the poles"
    )


def test_build_description_prompt_jupiter():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=7,
        gravity_level=6,
        distance_level=2,
        temperature_level=2,
        atmosphere_level=10,
        water_level=1,
        terrain_level=5,
        volcano_level=1,
        aurora_level=10,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_description_prompt()

    # Check.
    assert (
        result
        == "あなたは子ども向けの宇宙図鑑を作る専門家です。次の情報を元に惑星「パワプロクンセイ」の小学生向け図鑑風紹介文を170文字程度で書いてください。この惑星の名前「パワプロクンセイ」から想像できる雰囲気やイメージを少しだけ紹介文に取り入れてください。名前は文の最初に紹介してください。\ndiameter: a large planet\ngravity: with heavy gravity\ndistance: orbiting close to its star\ntemperature: a frigid surface\natmosphere: with a suffocating atmosphere of dense gases\nwater: completely dry, with no visible water\nterrain: with a balanced mix of hills, plains, and shallow valleys\nvolcano: with no signs of volcanic activity\naurora: with spectacular auroras dancing in all directions"
    )


def test_build_description_prompt_saturn():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=6,
        gravity_level=3,
        distance_level=3,
        temperature_level=1,
        atmosphere_level=10,
        water_level=1,
        terrain_level=5,
        volcano_level=1,
        aurora_level=10,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_description_prompt()

    # Check.
    assert (
        result
        == "あなたは子ども向けの宇宙図鑑を作る専門家です。次の情報を元に惑星「パワプロクンセイ」の小学生向け図鑑風紹介文を170文字程度で書いてください。この惑星の名前「パワプロクンセイ」から想像できる雰囲気やイメージを少しだけ紹介文に取り入れてください。名前は文の最初に紹介してください。\ndiameter: a medium-large planet\ngravity: with Earth-like gravity\ndistance: orbiting at a warm distance\ntemperature: a deeply frozen surface\natmosphere: with a suffocating atmosphere of dense gases\nwater: completely dry, with no visible water\nterrain: with a balanced mix of hills, plains, and shallow valleys\nvolcano: with no signs of volcanic activity\naurora: with spectacular auroras dancing in all directions"
    )


def test_build_description_prompt_uranus():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=3,
        gravity_level=2,
        distance_level=6,
        temperature_level=1,
        atmosphere_level=8,
        water_level=1,
        terrain_level=4,
        volcano_level=1,
        aurora_level=10,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_description_prompt()

    # Check.
    assert (
        result
        == "あなたは子ども向けの宇宙図鑑を作る専門家です。次の情報を元に惑星「パワプロクンセイ」の小学生向け図鑑風紹介文を170文字程度で書いてください。この惑星の名前「パワプロクンセイ」から想像できる雰囲気やイメージを少しだけ紹介文に取り入れてください。名前は文の最初に紹介してください。\ndiameter: a small planet\ngravity: with low gravity\ndistance: orbiting at a cold distance\ntemperature: a deeply frozen surface\natmosphere: with a heavy atmosphere and frequent storms\nwater: completely dry, with no visible water\nterrain: with minor craters and ridges\nvolcano: with no signs of volcanic activity\naurora: with spectacular auroras dancing in all directions"
    )


def test_build_description_prompt_neptune():
    # Given.
    prompt_levels = PromptLevels(
        diameter_level=3,
        gravity_level=3,
        distance_level=9,
        temperature_level=1,
        atmosphere_level=9,
        water_level=1,
        terrain_level=5,
        volcano_level=1,
        aurora_level=10,
    )
    promptBuilder = PromptBuilder(PLANET_NAME, prompt_levels)

    # Test.
    result = promptBuilder.build_description_prompt()

    # Check.
    assert (
        result
        == "あなたは子ども向けの宇宙図鑑を作る専門家です。次の情報を元に惑星「パワプロクンセイ」の小学生向け図鑑風紹介文を170文字程度で書いてください。この惑星の名前「パワプロクンセイ」から想像できる雰囲気やイメージを少しだけ紹介文に取り入れてください。名前は文の最初に紹介してください。\ndiameter: a small planet\ngravity: with Earth-like gravity\ndistance: orbiting extremely far from its star\ntemperature: a deeply frozen surface\natmosphere: with an extremely thick atmosphere\nwater: completely dry, with no visible water\nterrain: with a balanced mix of hills, plains, and shallow valleys\nvolcano: with no signs of volcanic activity\naurora: with spectacular auroras dancing in all directions"
    )
