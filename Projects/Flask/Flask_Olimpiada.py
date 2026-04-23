from flask import Flask, request
import os


site = Flask(__name__)

@site.route('/capacity')
def capacity():
	weights = {}
	word = request.args.get('value', ' ')
	with open('input.txt', 'r') as data:
		for line in data:
			char_size = line.split()
			if len(char_size) == 2:
				char = char_size[0]
				weight = int(char_size[1])
				weights[char] = weight
	total = 0
	for letter in word:
		if letter in weights:
			total += weights[letter]
	return str(total)



if __name__ == '__main__':
	site.run(debug = True)

