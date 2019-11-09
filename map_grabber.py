import certifi
import json
import os
import urllib3

from pathlib import Path

map_list = []
map_json_list = []

def get_map_json(map_id):
	pass

def main():
	with open("map_index.json") as jf:
		map_index = json.loads(jf.read())

	for map in map_index["maps"]:
		map_filename = map["file"]
		map_list.append(map_filename)

	host = "https://hcmaps.net/"
	http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
	for map in map_list:
		request = http.request("GET", "%s%s" % (host,map))
		json_map = json.loads(request.data)
		map_json_list.append(json_map)
		map_local_path = map.split("/")
		nice_path = Path("C:/Users/Chad/Desktop/Projects/hc_model/%s/%s" %(map_local_path[0], map_local_path[1]))
		if not nice_path.exists():
			nice_path.mkdir(parents=True)
			print(str(nice_path) + map_local_path[2])
		with open(str(nice_path) + '\\' + map_local_path[2], 'w+') as f:
			json.dump(json_map, f)

if __name__ == '__main__':
	main()