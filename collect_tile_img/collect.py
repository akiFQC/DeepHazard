import requests


"""
z=8
x_min=476
x_max=484
y_min=96
y_max=104
"""
"""
z=10
x_min=907
x_max=911
y_min=399
y_max=404
"""

"""
z=13
x_min=15458
x_max=15487
y_min=3203
y_max=3235
"""
#kanto
z=14
x_min=14501
x_max=14595
y_min=6397
y_max=6482

"""
z=15
x_min=61000
x_max=62370
y_min=11720
y_max=13385
"""
x_range=x_max-x_min
y_range=y_max-y_min
error_count=0

for i in range(x_range):
    for j in range(y_range):
        try:
            tile_x=i+x_min
            tile_y=j+y_min
            img_number=str(z)+"/"+str(tile_x)+"/"+str(tile_y)
            #url = "https://disaportaldata.gsi.go.jp/raster/01_flood_l2_shinsuishin_data/"+img_number+".png"
            #url = "https://disaportaldata.gsi.go.jp/raster/05_dosekiryukikenkeiryu/"+img_number+".png"
            url = "https://disaportaldata.gsi.go.jp/raster/04_tsunami_newlegend_data/"+img_number+".png"

            
            img_saved = "tunami_kanto/"+str(z)+"_"+str(tile_x)+"_"+str(tile_y)+".png"
            response = requests.get(url)
            image = response.content
            if response.status_code !=404:
                with open(img_saved, "wb") as aaa:
                    aaa.write(image)
        except:
            print('Error')
            error_count+=1
    print(i)
print("finish")