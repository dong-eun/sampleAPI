import pytest

def pytest_addoption(parser):
  parser.addoption(
    '--environment', action='store', default='stage'
  )

@pytest.fixture(scope="class")
def setup(request):
  # ENDPOINT = "https://map.kakao.com/link/search"
  test_environment = request.config.getoption("environment")

  if test_environment == "stage":
    ENDPOINT = "https://map.kakao.com/link/search"
  elif test_environment == "init":
    ENDPOINT = "https://todo.pixegami.io"
  elif test_environment == "real":
    ENDPOINT = "https://todo.pixegami.io"
  #
  request.cls.ENDPOINT = ENDPOINT
