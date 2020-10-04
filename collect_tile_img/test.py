import requests
tile_z=10
tile_x=909
tile_y=403
img_number=str(tile_z)+"/"+str(tile_x)+"/"+str(tile_y)
url = "https://disaportaldata.gsi.go.jp/raster/01_flood_l2_shinsuishin_data/"+img_number+".png"


response = requests.get(url)
image = response.content
img_saved = "test/"+str(tile_x)+"_"+str(tile_y)+".png"
if response.status_code !=404:
    with open(img_saved, "wb") as aaa:
        aaa.write(image)
else:
    print("404")

print("finish")