from dataloader import load_data
from jepana import serve
from searchengine import set_database
from threading import Thread

def launch():
	Thread(target=serve, args=()).start()
	Thread(target=load_data, args=(set_database,)).start()
		
launch()
