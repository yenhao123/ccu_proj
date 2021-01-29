import shodan
api = shodan.Shodan("wVkMJ6tngiM1KgQ0LvLVgZXvdnPirESa")

for i in range (0 , 256 , 1):
    for j in range (0 , 256 , 1):
        ip = '140.123.' + str(i) + '.' + str(j) 
        try:
            info = api.host(ip)
            print(info['ip_str'] , end ='\t')
            print(info['os'] , end ='\t')
            print(info['ports'])
        except shodan.APIError as e:
           #continue 
           print(e)
