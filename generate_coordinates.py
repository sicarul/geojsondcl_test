import json
from decimal import *

with open('all_tiles.json') as tiles_f:
    all_tiles = json.load(tiles_f)
    
    features = []

    i=0
    for key in all_tiles['data']:
        tile = all_tiles['data'][key]
        base_x = round(Decimal(tile['x'])/1000,4)
        base_y = round(Decimal(tile['y'])/1000,4)
        
        features.append(
          {
            "type": "Feature",
            "id": 0,
            "geometry": {
              "type": "Polygon",
              "coordinates": [[
                [
                  float(base_x+Decimal(0.0001)),
                  float(base_y+Decimal(0.0001))
                ],[
                  float(base_x+Decimal(0.0009)),
                  float(base_y+Decimal(0.0001))
                ],[
                  float(base_x+Decimal(0.0009)),
                  float(base_y+Decimal(0.0009))
                ],[
                  float(base_x+Decimal(0.0001)),
                  float(base_y+Decimal(0.0009))
                ],[
                  float(base_x+Decimal(0.0001)),
                  float(base_y+Decimal(0.0001))
                ]
              ]]
            },
            "properties": {
              "tile_id": f"{tile['x']}|{tile['y']}"
            }
          }
        )
        i+=1

out = {
  "type": "FeatureCollection",
  "features": features
}

with open('geojson_dcl.json', 'w') as f:
    json.dump(out, f)