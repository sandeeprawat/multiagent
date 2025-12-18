"""
Tests for the multiagent module.
"""

from multiagent import hello_world, __version__


def test_hello_world():
    """Test the hello_world function."""
    result = hello_world()
    assert result == "Hello from multiagent!"
    assert isinstance(result, str)


def test_version():
    """Test that version is defined."""
    assert __version__ == "0.1.0"
