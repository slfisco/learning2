#API Practice
import urllib.request
import json
#url = 'https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json?api_key=Q485Vx0qGkwGePxGnVAeqaUifFn2fJU0tdaHJf55'
#locHeader = '&location='
#location = 'Seattle+WA'
#requestobj = urllib.request.urlopen(url+locHeader+location)
testdict = {'foods':[
                {'food':
                     {'name' : 'ryeBread',
                      'type' : 'bread'}
                 },
                {'food':
                     {'name' : 'wheatBread',
                      'type' : 'bread'}
                 }]
            }
#print(testdict)
newdict = [x for x in testdict['foods'] if x['food']['name'] == 'ryeBread']

print(newdict)
#url = 'https://api.nal.usda.gov/ndb/V2/reports?ndbno=45352199&ndbno=45352200&api_key=3H6WGsKHJp5y71ywZO8KHZUtkQt1rF5qlruwiE94'
##url = 'https://api.nal.usda.gov/ndb/list?api_key=3H6WGsKHJp5y71ywZO8KHZUtkQt1rF5qlruwiE94'
#requestobj = urllib.request.urlopen(url)
#jsonobj = json.load(requestobj)

#output_dict = [x for x in jsonobj if x['name'] == 'energy']
##print(jsonobj)
##print(jsonobj['foods'][0]['food']['sr'])
