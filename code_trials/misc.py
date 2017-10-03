# coding=utf-8

import json

message_file = "../misc/strings.json"

with open(message_file, 'r') as jsfile:
    data = json.load(jsfile)

err_msg = data["error_messages"]["existing_material"]

print(err_msg % ('aaaaa', 'bbbbb'))
