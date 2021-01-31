from censys.ipv4 import *
from censys.base import *
from parser import process_parser

'''
Output
'''
fields = ["ip", "metadata.os", "protocols"]

def format(page):
    ip = page.get("ip","None")
    os = page.get("metadata.os","None")
    protocols = page.get("protocols","None")
    protocols = ", ".join([str(p.encode('UTF-8'), errors='ignore') for p in protocols])
    print("ip:" + ip, end = '\t')
    print("os:" + os, end = '\t')
    print("port:" + protocols)
    

def censys_engine(api):
    q = CensysIPv4(api_id=api['id'], api_secret=api['secret'])
    
    #total number for the ip
    #total = q.report(api['ip'],"80.http.get.headers.server.raw")['metadata']['count']
    #print('total:' + str(total))

    #search the ip
    cur_page = 1
    for page in q.search(api['ip'],fields):
        if cur_page > api['count']:
            return
        format(page)
        cur_page += 1

if __name__ == "__main__":

    args = process_parser()

    api = dict()
    api['id'] = "dc2dad4b-29e5-4328-b2f6-cc595a4ded7d"
    api['secret'] = "CDLU88ZMvhW8ZAd1ZvaOHtkqUwVLheeo"
    api['ip'] = args.ip
    api['count'] = args.count

    censys_engine(api)
