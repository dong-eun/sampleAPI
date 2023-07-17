import pytest
import requests

@pytest.mark.usefixtures('setup')
class TestSampleAPI():

  def test_poi_search(self):
    json = '카카오'
    response = requests.get(self.ENDPOINT + f'/{json}')

    assert  response.status_code == 300