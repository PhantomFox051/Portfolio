import json as js
import os
class JsonReader:
	def __init__(self, json_name: str):
		self.json_name = json_name

	def check_json(self):
		return self.json_name.endswith(".json") and os.path.isfile(self.json_name)

	def load_json(self):
		if self.check_json():
			try:
				with open(self.json_name, "r", encoding = "utf-8") as file:
					return js.load(file)
			except js.JSONDecodeError as e:
				print(f"{e} - ЭТО НЕ JSON А КОШМАР!!!!")
				return {
				"radius": 12,
				"change_x": 5,
				"change_y": 7,
				"width": 800,
				"height": 600
				}

		else:
			print("JSON нет")
			return {
				"radius": 12,
				"change_x": 5,
				"change_y": 7,
				"width": 800,
				"height": 600
				}

