__author__ = 'willian.reis'

import sys

from communication_api.communication import cCommunication
from pandas.io.json import json_normalize
from search_in_database.search import cSearch
import argparse


parser = argparse.ArgumentParser(description='Process search company and produts.')
parser.add_argument('--product', metavar='N', type=str, nargs='+')
parser.add_argument('--company_state', metavar='N', type=str, nargs='+')

args = parser.parse_args()

vProduct = ''
vCompany_state = ''

try:
    if len(args.product)> 0:
        vProduct = args.product[0]
except:
    pass

try:
    if len(args.company_state) > 0:
        vCompany_state = args.company_state[0]
except:
    pass

cCommunication = cCommunication()
data = cCommunication.RequestData()

if data == '':
    print 'Web service does not consumed'
    exit()

df = json_normalize(data, 'Products_list', ['company_Id', 'owner_name', 'owner_surname', 'owner_gender', 'owner_age', 'company_state', 'comments'],
            record_prefix='product_list_')

cSearch = cSearch(df)
cSearch.ProcessSearch(vProduct, vCompany_state)

