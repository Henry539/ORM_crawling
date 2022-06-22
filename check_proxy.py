import requests
import csv
import concurrent.futures


def main_2():
    proxylist = []
    with open('proxy.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            sli = row[0].split()
            proxylist.append(sli[0])



    def extract(proxy):
        try:
            r = requests.get('https://httpbin.org/ip', proxies={'http' : proxy,'https': proxy}, timeout=2)
            print(r.json(), ' --- working')
            return proxy
        except:
            pass

    list_use = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        list_use += executor.map(extract, proxylist)

    list_use2 = []
    for i in list_use:
        if i != None:
            list_use2.append(i)


    with open('data_proxy.txt', 'w') as wf:
        for text in list_use2:
            wf.write(text + '\n')
    print("PROCESSING 2 - CHECK PROXIES: DONE!")
    print("---------------------------------")

if __name__ == "__main__":
    main_2()