# coding: utf-8

import sys
import httplib
import urlparse
import json


osm_header = u"""<?xml version="1.0" encoding="UTF-8"?>
<osm version="0.6" generator="fs2osm">`
"""
bounds = u'<bounds minlat="{minlat}" minlon="{minlon"} maxlat="{maxlat}" maxlon="{maxlon}" />'
node_start = u'<node id="{uid}" lat="{lat}" lon="{lon}" visible="true">'
node_end = u'</node>'
tag = u'<tag k="{key}" v="{value}" />'
osm_footer = u"</osm>"

def main(argv):
    url = urlparse.urlparse(argv[1])
    conn = httplib.HTTPSConnection(url.hostname)
    conn.request("GET", "?".join((url.path, url.query)))

    r = conn.getresponse()
    data = json.loads(r.read())

    print osm_header
    features = data['features']
    uid = 0 
    for feature in features:
        uid -= 1
        x = feature['geometry']['x']
        y = feature['geometry']['y']
        print node_start.format(uid=uid, lat=y, lon=x).encode('utf-8') #あとで
        tags = []
        for k, v in feature['attributes'].items():
            if v != None: print tag.format(key=k, value=v).encode('utf-8')
        print node_end
    print osm_footer



if __name__ == "__main__":
    main(sys.argv)
