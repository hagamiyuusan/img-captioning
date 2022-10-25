import requests

import json

# with open("./data/uitviic_captions_train2017.json", "w") as write_file:
#     json.dump(data, write_file)
# print(data.text)
# Opening JSON file
f = open('./data/uitviic_captions_train2017.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['images']:
    img_data = requests.get(i['coco_url']).content
    with open('./images/' + i['file_name'], 'wb') as handler:
        handler.write(img_data)

# coco=COCO('./data/uitviic_captions_train2017.json')
# ids = list(coco.anns.keys())
# img_info=coco.getImgIds([ids[2]])[0]
# print(img_info)
# for i in range(len(ids)):
#     print(ids[i])
#     img_i


