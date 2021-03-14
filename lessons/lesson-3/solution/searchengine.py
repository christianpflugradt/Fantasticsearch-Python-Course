jeps = None

def set_database(jepdb):
	global jeps	
	jeps = jepdb
	
def has_database():
	return jeps is not None

		
def search(search_words):
	results = {}
	for word in search_words:
		results[word] = []
		for id, title, tokens in jeps:
			for token in tokens:
				if word.lower() in token:
					results[word].append((id, title))
					break
	merged_results = []
	if len(results) > 0:
		any_result = next(iter(results))
		if any_result is not None:
			for match in results[any_result]:
				found = True
				for collection in results.keys():
					if match not in results[collection]:
						found = False
						break
				if found:
					merged_results.append(match)
	return merged_results
