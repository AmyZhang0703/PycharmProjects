import unittest
import requests
import HtmlTestRunner
import json

__author__ = u'zhang-Aimei'

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.host = "https://api.worldbank.org/v2/countries/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        self.response = requests.get(self.host, params=None, headers=self.headers)
        self.List_countries = {'format': 'json', 'per_page': '3', 'page': '2'}
        self.example_url = "https://api.worldbank.org/v2/countries/?format=json&per_page=3&page=2"
        self.List_countries_using_per_response = requests.get(self.host,params=self.List_countries,headers=self.headers)

        self.filter_region_data = {'format': 'json', 'region': 'LCN'}
        self.region_example_url = "https://api.worldbank.org/v2/countries/?format=json&region=LCN"
        self.filter_region_response = requests.get(self.host,params=self.filter_region_data,headers=self.headers)

        self.countries_detail = "https://api.worldbank.org/v2/countries/FI?format=json"
        self.countries_detail_response = requests.get(self.countries_detail,params=None,headers=self.headers)

        self.query_country_name = 'Finland'
        self.query_country_id = 'FIN'

        self.Chinese_url = "https://api.worldbank.org/v2/zh/countries/?format=json&per_page=4"
        self.Chinese_response = requests.get(self.Chinese_url,params=None,headers=self.headers)
        self.Chinese_response.encoding = 'gbk'

        self.Chinese_data = "阿富汗"


    def test_countries(self):
        self.assertEqual(self.response.status_code, 200)
        print('countries url:')
        print(self.response.url)
        self.assertEqual(self.response.url,self.host)
        print(str(self.response.content).encode('utf-8'))


    def test_List_countries_API_using_per(self):
        self.assertEqual(self.List_countries_using_per_response.status_code, 200)
        print(self.List_countries_using_per_response.url)
        self.assertEqual(self.List_countries_using_per_response.url, self.example_url)
        print(str(self.List_countries_using_per_response.content).encode('utf-8'))

    def test_filter_by_region(self):
        self.assertEqual(self.filter_region_response.status_code, 200)
        print(self.filter_region_response.url)
        self.assertEqual(self.filter_region_response.url, self.region_example_url)
        print(str(self.filter_region_response.content).encode('utf-8'))

    def test_countries_detail(self):
        self.assertEqual(self.countries_detail_response.status_code, 200)
        print(self.countries_detail)
        resonse_data= json.loads(str(self.countries_detail_response.content, 'utf-8'))
        print(resonse_data)
        for detail in resonse_data[1]:
            print(detail['id'])
            print(detail['name'])
            self.assertEqual(detail['id'],self.query_country_id)
            self.assertEqual(detail['name'],self.query_country_name)

    def test_parse_jason(self):
        resonse_data = json.loads(str(self.countries_detail_response.content, 'utf-8'))
        print(resonse_data)
        for detail in resonse_data[1]:
            # print(detail)
            for k,v in detail.items():
                print(k,v)

    def test_query_Chinese(self):
        self.assertEqual(self.Chinese_response.status_code,200)
        print(self.Chinese_response.content)
        resonse_data = json.loads(self.Chinese_response.content)
        self.assertEqual(resonse_data[1][2]['name'], self.Chinese_data)


    def tearDown(self):
        print("execute tearDown")


if __name__ == '__main__':
    suite = unittest.makeSuite(UnitTests)
    filename = r'../TestResults/result.html'
    print(filename)
    fp = open(filename,'wb')
    runner = testRunner = HtmlTestRunner.HTMLTestRunner(output=r'../TestResults/')
    runner.run(suite)
    # unittest.main()
    fp.close()
