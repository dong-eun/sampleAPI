import requests
from utility.commonFunction import CommonFuntion


class TestSampleAPI(CommonFuntion):

  def test_poi_search(self):
    search = '카카오'
    response = requests.get(self.ENDPOINT + f'/{search}')

    assert  response.status_code == 200