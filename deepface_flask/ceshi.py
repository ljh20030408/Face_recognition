# import requests
# import base64
# # img_path = 'C:/Users/DELL/Desktop/deepface_suite-main/media/pic_folder/aishwarya__3.jpg'
# img_path = 'C:/Users/DELL/Desktop/deepface_suite-main/media/pic_folder/SeanConnery_1.jpg'
# with open(img_path, 'rb') as f:
#     img_data = base64.b64encode(f.read()).decode('utf-8')
#
# data = {
#     'name': 'clz',
#     # 'name': 'test2.jpg',
#     'img_base64': f'data:image/jpeg;base64,{img_data}'
# }
# response = requests.post('http://localhost:5000/delete', json=data)
#
# # response = requests.post('http://49.51.245.122:5000/write', json=data)
# print(response.text)


#

# import requests
# import base64
#
# # open the JPEG image file and read its contents
# with open('C:/Users/DELL/Desktop/deepface_suite-main/media/pic_folder/aishwarya__3.jpg', 'rb') as f:
#     image_data = f.read()
#
#
# image_b64 = base64.b64encode(image_data).decode('utf-8')
#
# headers = {'Content-Type': 'application/json'}
# data = {'img_base64': 'data:image/jpeg;base64,' + image_b64}
#
#
# response = requests.post('http://49.51.245.122:5000/verify', headers=headers, json=data)
#
# # print the response
# print(response.json())




import requests
import base64

img_name = 'clz'
headers = {'Content-Type': 'application/json'}
# create the request data
data = {
    'name': img_name,
}

# send the delete request to the API
response = requests.post('http://127.0.0.1:5000/delete', headers=headers, json=data)

# print the response status code and message
print(response.status_code)
print(response.json())






