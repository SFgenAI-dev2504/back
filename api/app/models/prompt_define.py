from enum import Enum


class PromptDefine(Enum):
    DIAMETER = [
        "a tiny planet",
        "a very small planet",
        "a small planet",
        "a medium-small planet",
        "a medium-sized planet",
        "a medium-large planet",
        "a large planet",
        "a very large planet",
        "a huge planet",
        "a gigantic planet",
    ]
    GRAVITY = [
        "with microgravity",
        "with low gravity",
        "with Earth-like gravity",
        "with slightly strong gravity",
        "with strong gravity",
        "with heavy gravity",
        "with very strong gravity",
        "with crushing gravity",
        "with extreme gravity",
        "with impossible gravity",
    ]
    DISTANCE = [
        "orbiting very close to its star",
        "orbiting close to its star",
        "orbiting at a warm distance",
        "orbiting moderately far from its star",
        "orbiting far from its star",
        "orbiting at a cold distance",
        "orbiting very far from its star",
        "orbiting in deep space",
        "orbiting extremely far from its star",
        "orbiting at the edge of a solar system",
    ]
    TEMPERATURE = [
        "a deeply frozen surface",
        "a frigid surface",
        "an icy landscape",
        "a cold environment",
        "a chilly climate",
        "a temperate climate",
        "a warm, dry surface",
        "a hot surface",
        "an extremely hot surface",
        "a scorched, volcanic surface",
    ]
    ATMOSPHERE = [
        "with no atmosphere, exposing the bare surface",
        "with a whisper-thin atmosphere",
        "with a thin, dusty atmosphere",
        "with a light atmosphere and wispy clouds",
        "with a moderate atmosphere and some clouds",
        "with a thicker atmosphere and noticeable haze",
        "with a dense atmosphere and swirling winds",
        "with a heavy atmosphere and frequent storms",
        "with an extremely thick atmosphere",
        "with a suffocating atmosphere of dense gases",
    ]
    WATER = [
        "completely dry, with no visible water",
        "with a few small puddles or dried riverbeds",
        "with occasional streams or isolated lakes",
        "with scattered lakes and small rivers",
        "with rivers and modest seas",
        "with half the surface covered in water",
        "with large seas and small oceans",
        "mostly covered in water with vast oceans",
        "nearly submerged with only small landmasses visible",
        "entirely ocean-covered, like a water world",
    ]
    TERRAIN = [
        "with a perfectly smooth and flat surface",
        "with gentle rolling plains",
        "with small hills and light undulations",
        "with minor craters and ridges",
        "with a balanced mix of hills, plains, and shallow valleys",
        "with noticeable elevation changes and rock formations",
        "with rugged terrain and scattered mountains",
        "with steep cliffs and large craters",
        "with chaotic, heavily cratered landscapes",
        "with extreme topography, sharp ridges and deep canyons",
    ]
    VOLCANO = [
        "with no signs of volcanic activity",
        "with extinct volcanoes and hardened lava fields",
        "with occasional dormant volcanoes",
        "with scattered inactive volcanoes",
        "with signs of minor volcanic activity",
        "with a few active volcanoes emitting smoke",
        "with frequent volcanic eruptions",
        "with lava rivers and glowing craters",
        "with major volcanic zones and widespread eruptions",
        "with extreme volcanic activity and a molten landscape",
    ]
    AURORA = [
        "with no auroras visible in the sky",
        "with rare, faint auroras near the poles",
        "with occasional auroras in polar regions",
        "with gentle aurora glow appearing at night",
        "with auroras shimmering faintly across the skies",
        "with clearly visible auroras in motion",
        "with colorful auroras stretching across the horizon",
        "with vivid auroras swirling above the surface",
        "with brilliant auroras illuminating the sky",
        "with spectacular auroras dancing in all directions",
    ]
