from app.models.frame import Frame


def test_select_frame():
    # Test.
    result = Frame.select_frame()

    # Check.
    assert result is not None
    assert result in [Frame.RED, Frame.BLUE, Frame.YELLOW]


def test_get_file_name():
    # Given.
    frames = [Frame.RED, Frame.BLUE, Frame.YELLOW]
    colors = ["red", "blue", "yellow"]

    # Test, Check.
    for index, frame in enumerate(frames):
        result = frame.get_file_name()
        assert result is not None
        assert result == f"frame_{colors[index]}.png"


def test_get_shadow_color():
    # Given.
    frames = [Frame.RED, Frame.BLUE, Frame.YELLOW]
    colors = [(255, 0, 0, 100), (0, 0, 255, 100), (255, 255, 0, 100)]

    # Test, Check.
    for index, frame in enumerate(frames):
        result = frame.get_shadow_color()
        assert result is not None
        assert result == colors[index]
