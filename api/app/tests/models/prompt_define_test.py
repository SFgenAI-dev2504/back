from app.models.prompt_define import PromptDefine


def test_diameter():
    # Test.
    result = PromptDefine.DIAMETER

    # Check.
    assert result is not None
    assert len(result.value) == 10
    assert result.value[0] == "a tiny planet"
    assert result.value[1] == "a very small planet"
    assert result.value[2] == "a small planet"
    assert result.value[3] == "a medium-small planet"
    assert result.value[4] == "a medium-sized planet"
    assert result.value[5] == "a medium-large planet"
    assert result.value[6] == "a large planet"
    assert result.value[7] == "a very large planet"
    assert result.value[8] == "a huge planet"
    assert result.value[9] == "a gigantic planet"


def test_gravity():
    # Test.
    result = PromptDefine.GRAVITY

    # Check.
    assert result is not None
    assert len(result.value) == 10
    assert result.value[0] == "with microgravity"
    assert result.value[1] == "with low gravity"
    assert result.value[2] == "with Earth-like gravity"
    assert result.value[3] == "with slightly strong gravity"
    assert result.value[4] == "with strong gravity"
    assert result.value[5] == "with heavy gravity"
    assert result.value[6] == "with very strong gravity"
    assert result.value[7] == "with crushing gravity"
    assert result.value[8] == "with extreme gravity"
    assert result.value[9] == "with impossible gravity"


def test_distance():
    # Test.
    result = PromptDefine.DISTANCE

    # Check.
    assert result is not None
    assert len(result.value) == 10
    assert result.value[0] == "orbiting very close to its star"
    assert result.value[1] == "orbiting close to its star"
    assert result.value[2] == "orbiting at a warm distance"
    assert result.value[3] == "orbiting moderately far from its star"
    assert result.value[4] == "orbiting far from its star"
    assert result.value[5] == "orbiting at a cold distance"
    assert result.value[6] == "orbiting very far from its star"
    assert result.value[7] == "orbiting in deep space"
    assert result.value[8] == "orbiting extremely far from its star"
    assert result.value[9] == "orbiting at the edge of a solar system"


def test_temperature():
    # Test.
    result = PromptDefine.TEMPERATURE

    # Check.
    assert result is not None
    assert len(result.value) == 10
    assert result.value[0] == "a deeply frozen surface"
    assert result.value[1] == "a frigid surface"
    assert result.value[2] == "an icy landscape"
    assert result.value[3] == "a cold environment"
    assert result.value[4] == "a chilly climate"
    assert result.value[5] == "a temperate climate"
    assert result.value[6] == "a warm, dry surface"
    assert result.value[7] == "a hot surface"
    assert result.value[8] == "an extremely hot surface"
    assert result.value[9] == "a scorched, volcanic surface"


def test_atmosphere():
    # Test.
    result = PromptDefine.ATMOSPHERE

    # Check.
    assert result is not None
    assert len(result.value) == 10
    assert result.value[0] == "with no atmosphere, exposing the bare surface"
    assert result.value[1] == "with a whisper-thin atmosphere"
    assert result.value[2] == "with a thin, dusty atmosphere"
    assert result.value[3] == "with a light atmosphere and wispy clouds"
    assert result.value[4] == "with a moderate atmosphere and some clouds"
    assert result.value[5] == "with a thicker atmosphere and noticeable haze"
    assert result.value[6] == "with a dense atmosphere and swirling winds"
    assert result.value[7] == "with a heavy atmosphere and frequent storms"
    assert result.value[8] == "with an extremely thick atmosphere"
    assert result.value[9] == "with a suffocating atmosphere of dense gases"


def test_water():
    # Test.
    result = PromptDefine.WATER

    # Check.
    assert result is not None
    assert len(result.value) == 10
    assert result.value[0] == "completely dry, with no visible water"
    assert result.value[1] == "with a few small puddles or dried riverbeds"
    assert result.value[2] == "with occasional streams or isolated lakes"
    assert result.value[3] == "with scattered lakes and small rivers"
    assert result.value[4] == "with rivers and modest seas"
    assert result.value[5] == "with half the surface covered in water"
    assert result.value[6] == "with large seas and small oceans"
    assert result.value[7] == "mostly covered in water with vast oceans"
    assert result.value[8] == "nearly submerged with only small landmasses visible"
    assert result.value[9] == "entirely ocean-covered, like a water world"


def test_terrain():
    # Test.
    result = PromptDefine.TERRAIN

    # Check.
    assert result is not None
    assert len(result.value) == 10
    assert result.value[0] == "with a perfectly smooth and flat surface"
    assert result.value[1] == "with gentle rolling plains"
    assert result.value[2] == "with small hills and light undulations"
    assert result.value[3] == "with minor craters and ridges"
    assert (
        result.value[4] == "with a balanced mix of hills, plains, and shallow valleys"
    )
    assert result.value[5] == "with noticeable elevation changes and rock formations"
    assert result.value[6] == "with rugged terrain and scattered mountains"
    assert result.value[7] == "with steep cliffs and large craters"
    assert result.value[8] == "with chaotic, heavily cratered landscapes"
    assert result.value[9] == "with extreme topography, sharp ridges and deep canyons"


def test_volcano():
    # Test.
    result = PromptDefine.VOLCANO

    # Check.
    assert result is not None
    assert len(result.value) == 10
    assert result.value[0] == "with no signs of volcanic activity"
    assert result.value[1] == "with extinct volcanoes and hardened lava fields"
    assert result.value[2] == "with occasional dormant volcanoes"
    assert result.value[3] == "with scattered inactive volcanoes"
    assert result.value[4] == "with signs of minor volcanic activity"
    assert result.value[5] == "with a few active volcanoes emitting smoke"
    assert result.value[6] == "with frequent volcanic eruptions"
    assert result.value[7] == "with lava rivers and glowing craters"
    assert result.value[8] == "with major volcanic zones and widespread eruptions"
    assert result.value[9] == "with extreme volcanic activity and a molten landscape"


def test_aurora():
    # Test.
    result = PromptDefine.AURORA

    # Check.
    assert result is not None
    assert len(result.value) == 10
    assert result.value[0] == "with no auroras visible in the sky"
    assert result.value[1] == "with rare, faint auroras near the poles"
    assert result.value[2] == "with occasional auroras in polar regions"
    assert result.value[3] == "with gentle aurora glow appearing at night"
    assert result.value[4] == "with auroras shimmering faintly across the skies"
    assert result.value[5] == "with clearly visible auroras in motion"
    assert result.value[6] == "with colorful auroras stretching across the horizon"
    assert result.value[7] == "with vivid auroras swirling above the surface"
    assert result.value[8] == "with brilliant auroras illuminating the sky"
    assert result.value[9] == "with spectacular auroras dancing in all directions"
