from concurrency import get_number_of_threads as count
from concurrency import wait_until_threshold_reached as wait_for
from re import findall
from urllib.request import urlopen
from threading import Thread

jepbaseurl = 'http://openjdk.java.net/jeps/'
jepmatch = r'<td class="jep">(\d+)</td>'
titlematch = r'<title>(.+)</title>'

jepdb = []

def get_jep(id):
	try:
		return str(urlopen('%s%s' % (jepbaseurl, str(id))).read()).replace('\\n',' ').replace('\\r',' ')
	except:
		print('could not download jep :-(')
		return None
	
def download_jep(id):
	content = get_jep(id)
	if content is not None:
		title = findall(titlematch, content)[0]
		jepdb.append((id, title, content))

def crawl_all_jeps():
	jepindex = get_jep(0)
	hits = findall(jepmatch, jepindex)
	for hit in hits:
		Thread(target=download_jep, args=(hit,)).start()

def crawl():
	threshold = count()
	crawl_all_jeps()
	wait_for(threshold)
	return jepdb
