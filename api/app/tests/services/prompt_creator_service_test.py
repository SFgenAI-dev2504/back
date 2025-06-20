from app.models.prompt_levels import PromptLevels
from app.services.prompt_creator_service import PromptCreatorService


def test_create_all_prompt_mercury():
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
    promptCreatorService = PromptCreatorService(prompt_levels)

    # Test.
    result = promptCreatorService.create_all_prompt()

    # Check.
    assert (
        result
        == "A tiny planet with microgravity, orbiting very close to its star. The planet has with a temperate climate and with no atmosphere, exposing the bare surface. Its surface is completely dry, with no visible water, with chaotic, heavily cratered landscapes, with extinct volcanoes and hardened lava fields, and with no auroras visible in the sky. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )


def test_create_all_prompt_venus():
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
    promptCreatorService = PromptCreatorService(prompt_levels)

    # Test.
    result = promptCreatorService.create_all_prompt()

    # Check.
    assert (
        result
        == "A tiny planet with low gravity, orbiting very close to its star. The planet has with a scorched, volcanic surface and with a suffocating atmosphere of dense gases. Its surface is completely dry, with no visible water, with a balanced mix of hills, plains, and shallow valleys, with extreme volcanic activity and a molten landscape, and with no auroras visible in the sky. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )


def test_create_all_prompt_earth():
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
    promptCreatorService = PromptCreatorService(prompt_levels)

    # Test.
    result = promptCreatorService.create_all_prompt()

    # Check.
    assert (
        result
        == "A tiny planet with Earth-like gravity, orbiting very close to its star. The planet has with a temperate climate and with an extremely thick atmosphere. Its surface is mostly covered in water with vast oceans, with a balanced mix of hills, plains, and shallow valleys, with a few active volcanoes emitting smoke, and with auroras shimmering faintly across the skies. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )


def test_create_all_prompt_mars():
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
    promptCreatorService = PromptCreatorService(prompt_levels)

    # Test.
    result = promptCreatorService.create_all_prompt()

    # Check.
    assert (
        result
        == "A tiny planet with microgravity, orbiting very close to its star. The planet has with a frigid surface and with a whisper-thin atmosphere. Its surface is completely dry, with no visible water, with chaotic, heavily cratered landscapes, with lava rivers and glowing craters, and with rare, faint auroras near the poles. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )


def test_create_all_prompt_jupiter():
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
    promptCreatorService = PromptCreatorService(prompt_levels)

    # Test.
    result = promptCreatorService.create_all_prompt()

    # Check.
    assert (
        result
        == "A large planet with heavy gravity, orbiting close to its star. The planet has with a frigid surface and with a suffocating atmosphere of dense gases. Its surface is completely dry, with no visible water, with a balanced mix of hills, plains, and shallow valleys, with no signs of volcanic activity, and with spectacular auroras dancing in all directions. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )


def test_create_all_prompt_saturn():
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
    promptCreatorService = PromptCreatorService(prompt_levels)

    # Test.
    result = promptCreatorService.create_all_prompt()

    # Check.
    assert (
        result
        == "A medium-large planet with Earth-like gravity, orbiting at a warm distance. The planet has with a deeply frozen surface and with a suffocating atmosphere of dense gases. Its surface is completely dry, with no visible water, with a balanced mix of hills, plains, and shallow valleys, with no signs of volcanic activity, and with spectacular auroras dancing in all directions. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )


def test_create_all_prompt_uranus():
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
    promptCreatorService = PromptCreatorService(prompt_levels)

    # Test.
    result = promptCreatorService.create_all_prompt()

    # Check.
    assert (
        result
        == "A small planet with low gravity, orbiting at a cold distance. The planet has with a deeply frozen surface and with a heavy atmosphere and frequent storms. Its surface is completely dry, with no visible water, with minor craters and ridges, with no signs of volcanic activity, and with spectacular auroras dancing in all directions. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )


def test_create_all_prompt_neptune():
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
    promptCreatorService = PromptCreatorService(prompt_levels)

    # Test.
    result = promptCreatorService.create_all_prompt()

    # Check.
    assert (
        result
        == "A small planet with Earth-like gravity, orbiting extremely far from its star. The planet has with a deeply frozen surface and with an extremely thick atmosphere. Its surface is completely dry, with no visible water, with a balanced mix of hills, plains, and shallow valleys, with no signs of volcanic activity, and with spectacular auroras dancing in all directions. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
    )
