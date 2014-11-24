osm_header = """<?xml version="1.0" encoding="UTF-8"?>
<osm version="0.6" generator="fs2osm">`
"""
bounds = '<bounds minlat="{minlat}" minlon="{minlon"} maxlat="{maxlat}" maxlon="{maxlon}" />'
node_start = '<node id="-1" lat="{lat}" lon="{lon}" visible="true">'
node_end = '</node>'
tag = '<tag k="{key}" v="{value}" />'
osm_footer = "</osm>"
