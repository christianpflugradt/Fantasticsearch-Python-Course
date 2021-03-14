from os.path import isfile
from pickle import dump, load

def exists(filename):
	return isfile(filename)

def save(data, filename):
	with open(filename, 'wb') as file:
		dump(data, file)
		
def restore(filename):
	with open(filename, 'rb') as file:
		return load(file)
