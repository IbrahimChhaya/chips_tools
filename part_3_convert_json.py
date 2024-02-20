import cc_dat_utils
import json

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file

def json_to_cclevelpack( json_data ):

    for level in json_data:
        print(level)
        print("hey")


    # return cclevelpack

input_json_file = "data/cc_level_pack.json"

with open(input_json_file, "r") as reader:
        game_json_data = json.load(reader)

json_to_cclevelpack(game_json_data)