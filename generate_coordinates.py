import json
from decimal import *


with open('all_tiles.json') as tiles_f:
    all_tiles = json.load(tiles_f)

tile_ids = set([id.replace(',','|') for id in all_tiles['data']])
tiles_added = set()

tiles_mapping = []
features = []

i=0

GRID_SIZE = 5
GRID_LENGTH = int(300 / GRID_SIZE)

for quadrant_X in range(GRID_LENGTH):
    x_start = int((quadrant_X - (GRID_LENGTH / 2)) * GRID_SIZE)

    for quadrant_Y in range(GRID_LENGTH):
        y_start = int((quadrant_Y - (GRID_LENGTH / 2)) * 5)
        x_end = int(x_start + GRID_SIZE - 1)
        y_end = int(y_start + GRID_SIZE - 1)
        if x_end == 149:
            x_end = 150
        if y_end == 149:
            y_end = 150
        
        # Top aetherian border
        if x_start >= 60 and y_end == 150:
            y_end = 158
        if y_start >= 55 and x_end == 150:
            x_end = 163

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
                "grid_id": i,
                "grid_name": f"{x_start},{y_start} to {x_end},{y_end}",
                "coord_start": f"{x_start}|{y_start}",
                "coord_end": f"{x_end}|{y_end}"
            }
            }
        )
        for x in range(x_start, x_end+1):
            for y in range(y_start, y_end+1):
                tile_id = f"{x}|{y}"
                if tile_id in tile_ids:
                    tiles_mapping.append([str(i),tile_id])

        i+=1

out = {
  "type": "FeatureCollection",
  "features": features
}

with open('geojson_dcl.json', 'w') as f:
    json.dump(out, f)

with open('tiles_mapping.csv', 'w') as f:
    f.write("grid_id, tile_id\n")
    for t in tiles_mapping:
        f.write("{}\n".format(",".join(t)))