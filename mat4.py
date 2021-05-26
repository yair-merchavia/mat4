import requests

dic_dis ={}
def get_lat_lng(address):
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ','+'), api_key))
    response = requests.get(url)
    resp_json_payload = response.json()
    lat = resp_json_payload['results'][0]['geometry']['location']['lat']
    lng = resp_json_payload['results'][0]['geometry']['location']['lng']
    return lat, lng

api_file = open("api-key.txt","r")
api_key = api_file.read()
api_file.close()

home = "תל%אביב"

dests = open('dests.txt',encoding="utf8")
dests = dests.readlines()
size = len(dests)
list_of_all_dests =list()
list_of_all_dests1=list()
i = 0 
for line in dests:
    if i >5 :
        break
    location = dests[i]
    i += 1

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&"
    u = (url + "origins=" + home + "&destinations=" + location + "&key=" + api_key) 

    r = requests.get(url + "origins=" + home + "&destinations=" + location + "&key=" + api_key)    
    time = r.json()["rows"][0]["elements"][0]["duration"]["text"]       
    distance = r.json()["rows"][0]["elements"][0]["distance"]["text"]
    distance = distance.replace(" ","")
    distance =distance.replace("km","")
    city = {location: (distance, time,get_lat_lng(location)[0],get_lat_lng(location)[1])} 
    list_of_all_dests.append(city)
    dic_dis[location] =distance
    city1=[location,distance, time,get_lat_lng(location)[0],get_lat_lng(location)[1]] 
    list_of_all_dests1.append(city1)
 
for i in list_of_all_dests1:
    print(i[0])
    print("Distance from Tel Aviv (in kilometers): ",i[1])
    print("Travel time from Tel Aviv (hours and minutes): ",i[2])
    print("Longitude of the target: ",i[3])
    print("Latitude of the target: ",i[4])
    print()
    
print("The 3 cities furthest from Tel Aviv are: ")

distance_list=list()
for i in list_of_all_dests1:
    distance_list.append(i[1])
distance_list.sort()
distance_list=distance_list[2:]

for i in list_of_all_dests1:
    for t in distance_list:
        if i[1]==t:
            print(i[0])
