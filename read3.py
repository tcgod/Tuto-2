import urllib2,json,base64
accesstoken = "9169LT40ARJ3BWVGA84R"
institution = "10007772"
course = "U56119"
page = 0
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(
    institution,
    course
    )
request = urllib2.Request(url)
request.add_header(
    "Authorization",
    "Basic " + base64.encodestring(accesstoken+":").replace('\n','')
    )
response = urllib2.urlopen(request)
data = json.load(response)
print json.dumps(data,indent=2)
d = data[5]["Details"]
e = d[0]["Value"]
print e
d = data[6]["Details"]
e = d[1]["Value"]
print e
d = data[6]["Details"]
e = d[4]["Value"]
print e
    
