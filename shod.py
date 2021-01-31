import shodan
import sys
from time import sleep
from parser import process_parser

def shodan_engine(api_key,ip,count):
    api = shodan.Shodan(api_key)

    mask = ip.split('/')[1]

    if mask == "16":
        ip_str = "".join([ip.split('.')[0],".",ip.split('.')[1]])

        for i in range (0 , 256 , 1):
            for j in range (0 , 256 , 1):
                if j == count:
                    return
                
                ip = ip_str + "." + str(i) + "." + str(j)
                try:
                    info = api.host(ip)
                    print("ip:" + str(info['ip_str']) , end ='\t')
                    print("os:" + str(info['os']) , end ='\t')
                    print("port:" + str(info['ports']))
                    #sleep(1)
                except shodan.APIError as e:
                    #continue 
                    print(e)

if __name__ == "__main__":
   
    args = process_parser()
    ip = args.ip
    count = args.count

    API_KEY = "839CrW4f3Omc9wYO9aMWeRq0Go4rEPfN" 
    shodan_engine(API_KEY,ip,count);
