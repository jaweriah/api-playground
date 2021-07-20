import requests
import json
from assertpy.assertpy import assert_that

url = "https://pacific-sands-48667.herokuapp.com/services"

payload = json.dumps({
  "name": "Jaweriah Service"
})

headers = {
  'Content-Type': 'application/json'
}


#************  GET API ************************************
response = requests.request("GET", url, headers=headers)
services = response.json()
assert_that(response.status_code).is_equal_to(200)   # response code 200
print(services)
service_name = {}
service_name = [service['name'] for service in services['data']]
print(service_name)
assert_that(service_name).contains("Best Buy Mobile")   # Validating the name among the first 10 service names as I don't know how to increase the limit size of API


#*************** POST API  ********************************************
response = requests.request("POST", url, headers=headers, data=payload)
service = response.json()
print(service)
assert_that(response.status_code).is_equal_to(201) # response code 201
service_name = service['name']
print(service_name)
assert_that(service_name).contains("Jaweriah Service")

#**************** DELETE API
id_to_be_deleted = 11
response = requests.request("GET", url, headers=headers)
services = response.json()
assert_that(response.status_code).is_equal_to(200)   # response code 200
service_id = {}
service_id = [service['id'] for service in services['data']]
assert_that(service_id).contains(id_to_be_deleted)
url = f'{url}/{id_to_be_deleted}'
response = requests.delete(url)
service = response.json()
print(service)
assert_that(response.status_code).is_equal_to(200) # response code 200
service_deleted = service['id']
print(service_deleted)
assert_that(service_deleted).contains(id_to_be_deleted)
