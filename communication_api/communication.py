__author__ = 'willian.reis'

from urllib2 import Request, urlopen
import json

class cCommunication:

    def RequestData(self):
        try:
            request=Request('https://api-sandbox.contabilizei.com/ds/customers')
            response = urlopen(request)
            elevations = response.read()
            data = json.loads(elevations)
            return data
        except:
            return ''
