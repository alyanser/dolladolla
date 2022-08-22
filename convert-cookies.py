#!/usr/bin/env python

import json
import pickle
import os

for file in os.listdir():
	words = file.split('.')

	if words[len(words) - 1] != "json":
		continue

	platform = words[1]
	print("found {} cookies. converting to pkl...".format(platform))

	with open(file) as f:
		content = f.read()
		js = json.loads(content)
		pickle.dump(js, open(".{}.pkl".format(platform), "wb"))
