from burner import __version__
from burner.burner_sum import burner_sum

def test_version():
    assert __version__ == '0.1.0'


assert burner_sum(2,3) == 5