import json


with open('all_tiles.json') as tiles_f:
    all_tiles = json.load(tiles_f)
    
    features = []

    for key in all_tiles['data']:
        tile = all_tiles['data'][key]
        base_x = float(tile['x'])/1000
        base_y = float(tile['x'])/1000
        features.append(
{
      "type": "Feature",
      "id": 0,
      "geometry": {
        "type": "Polygon",
        "coordinates": [[
          [
            base_x+0.0001,
            base_y+0.0001
          ],[
            base_x+0.0009,
            base_y+0.0001
          ],[
            base_x+0.0009,
            base_y+0.0009
          ],[
            base_x+0.0001,
            base_y+0.0009
          ],[
            base_x+0.0001,
            base_y+0.0001
          ]
        ]]
      },
      "properties": {
        "tile_id": "1|1"
      }
    }
        )

out = {
  "type": "FeatureCollection",
  "features": features
}

with open('geojson_dcl.json', 'w') as f:
    json.dump(out, f, indent=2)