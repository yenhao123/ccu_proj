import sys
import shod
import cens
import zoom
from parser import process_parser

if __name__ == "__main__":
    
    ## args prepare
    args = process_parser()
    ip = args.ip
    count = args.count
    
    print("Shodan Start")
    api_key = "839CrW4f3Omc9wYO9aMWeRq0Go4rEPfN"
    shod.shodan_engine(api_key,ip,count)

    print("Zoomeye Start")
    api_key = "7557767C-20cf-fd7d5-d848-d7a5904e8f1" 
    zoom.zoomeye_engine(api_key,ip,count)

    print("Censys Start")
    api = dict()
    api['id'] = "dc2dad4b-29e5-4328-b2f6-cc595a4ded7d"
    api['secret'] = "CDLU88ZMvhW8ZAd1ZvaOHtkqUwVLheeo"
    api['ip'] = ip
    api['count'] = count
    cens.censys_engine(api)
