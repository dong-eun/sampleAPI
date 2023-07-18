import pytest
import requests

@pytest.mark.usefixtures('setup')
class TestSampleAPI():

  def test_poi_search(self):
    search = '카카오'
    response = requests.get(self.ENDPOINT + f'/{search}')

    assert  response.status_code == 200