import simplejson, urllib

GEOCODE_BASE_URL = 'http://maps.google.com/maps/api/geocode/json'

def geocode(address="Zaragoza,Spain",sensor="false", **geo_args):
    geo_args.update({
        'address': address,
        'sensor': sensor  
    })

    url = GEOCODE_BASE_URL + '?' + urllib.urlencode(geo_args)
    result = simplejson.load(urllib.urlopen(url))
       
    print simplejson.dumps([s['geometry']['location'] for s in result['results']], indent=2)

if __name__ == '__main__':
    geocode(address="Madrid",sensor="false")
