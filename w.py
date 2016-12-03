import urllib2

def search(q):
	full_url = "https://suggestqueries.google.com/complete/search?client=firefox&q=";
	data = urllib2.urlopen(full_url+q)
	return eval(data.read())[1]
print search("pyt")[:5]