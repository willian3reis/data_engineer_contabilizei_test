__author__ = 'willian.reis'
import unittest

from pandas.io.json import json_normalize

from communication_api.communication import cCommunication
from search_in_database.search import cSearch

class TestSearch(unittest.TestCase):
    dataframe = None

    def setUp(self):
        cc = cCommunication()
        data = cc.RequestData()
        self.dataframe = df = json_normalize(data, 'Products_list', ['company_Id', 'owner_name', 'owner_surname', 'owner_gender', 'owner_age', 'company_state', 'comments'],
                    record_prefix='product_list_')

    def Search1(self):
        cs = cSearch()
        cs.ProcessSearch(product='ketchup', company_state='PR')
        self.assertEqual(cs.number_f_company, 13)

        cs = cSearch()
        cs.ProcessSearch(product='water')
        self.assertEqual(cs.number_f_company, 36)

    def Search2(self):
        cs = cSearch()
        cs.ProcessSearch(product='water')
        self.assertEqual(cs.number_f_company, 131)

        cs = cSearch()
        cs.ProcessSearch(product='water', company_state='PR')
        self.assertEqual(cs.number_f_company, 22)

        cs = cSearch()
        cs.ProcessSearch(product='water', company_state='SP')
        self.assertEqual(cs.number_f_company, 29)

if __name__ == '__main__':
    unittest.main()