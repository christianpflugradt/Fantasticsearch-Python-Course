from concurrency import get_number_of_threads as count, wait_until_threshold_reached as wait_for
from crawler import crawl
from database import exists, restore, save
from threading import Thread
from tokenizer import tokenize

DB_FILE = 'fantasticdb.db'

jepdb = []

def add_to_jepdb(id, text, content):
    print('tokenizing jep %s' % id)
    jepdb.append((id, text, tokenize(content)))

def process(jeps):
    threshold = count()
    for id, text, content in jeps:
        wait_for(threshold + 4)
        Thread(target=add_to_jepdb, args=(id, text, content)).start()
    wait_for(threshold)

def load_data(callback):
    global jepdb
    if exists(DB_FILE):
        print('restoring jeps...')
        jepdb = restore(DB_FILE)
    else:
        print('downloading jeps...')
        jeps = crawl()
        print('tokenizing jeps...')
        process(jeps)
        save(jepdb, DB_FILE)
    callback(jepdb)
