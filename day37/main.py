import requests
from datetime import datetime
USERNAME = "testingkun99"
TOKEN = "vjjkgoongnhbjnfjngjen"
pixela_endpoint ="https://pixe.la/v1/users"
GraphID = "graph1"

#Create account--------------------------------
# user_params ={
#         "token":TOKEN,
#         "username":USERNAME,
#         "agreeTermsOfService":"yes",
#         "notMinor":"yes"
#         }
# # response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
headers = {
        "X-USER-TOKEN":TOKEN
}
#Create graph--------------------------------
# graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config={
#         "id":"graph1",
#         "name" : "Reading Graph",
#         "unit": "pages",
#         "type": "int",
#         "color": "sora"
# }
# response =requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

#upload a value to graph-----------------------------------
# graph1_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GraphID}"
# current_day = datetime.now().strftime("%Y%m%d")
# graph_value_config ={
#         "date":f"{current_day}",
#         "quantity":"1"
# }
# response =requests.post(url=graph1_endpoint, json=graph_value_config, headers=headers)
# print(response.text)


# #update a existed value in graph-----------------------------------
# update_day = "20220616"
# graph1_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GraphID}/{update_day}"
# graph_value_config ={
#         "quantity":"20"
# }
# response =requests.put(url=graph1_endpoint, json=graph_value_config, headers=headers)
# print(response.text)

#delete a existed value in graph-----------------------------------
# update_day = "20220616"
# graph1_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GraphID}/{update_day}"
#
# response =requests.delete(url=graph1_endpoint, headers=headers)
# print(response.text)