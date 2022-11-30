import json
from decimal import *

with open('all_tiles.json') as tiles_f:
    all_tiles = json.load(tiles_f)
    
    features = []

    i=0

    for quadrant_X in range(30):
      x_start = (quadrant_X - 15) * 10
      x_end = x_start + 9
      if x_end == 149:
        x_end = 150

      for quadrant_Y in range(30):
        y_start = (quadrant_Y - 15) * 10
        y_end = y_start + 9
        if y_end == 149:
          y_end = 150

        coord_x_start = float(round(Decimal(x_start)/1000,4))
        coord_y_start = float(round(Decimal(y_start)/1000,4))
        coord_x_end = float(round(Decimal(x_end)/1000,4))
        coord_y_end = float(round(Decimal(y_end)/1000,4))

        features.append(
          {
            "type": "Feature",
            "id": i,
            "geometry": {
              "type": "Polygon",
              "coordinates": [[
                [
                  coord_x_start,
                  coord_y_start
                ],[
                  coord_x_end,
                  coord_y_start
                ],[
                  coord_x_end,
                  coord_y_end
                ],[
                  coord_x_start,
                  coord_y_end
                ],[
                  coord_x_start,
                  coord_y_start
                ]
              ]]
            },
            "properties": {
              "coord_start": f"{x_start}|{y_start}",
              "coord_end": f"{x_end}|{y_end}"
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