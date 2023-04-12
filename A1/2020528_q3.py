import pandas as pd
import socket

File = open('2020528_q3.txt', 'w')
#reading the data
url = "https://crt.sh/?q=iiitd.edu.in"
page = pd.read_html(url)
table = page[2]

#forming a list of all the domains
sub_domains1 = table.iloc[:,5].values
sub_domains1 = list(sub_domains1)
sub_domains2 = table.iloc[:,4].values
sub_domains2 = list(sub_domains2)
sub_domains = sub_domains1 + sub_domains2
list1 = []

#spliting the domains
for i in sub_domains:
    if(" " in i):
        a = i.split(" ")
        list1 = list1 + a
    else:
        list1.append(i)
    
#removing the duplicates
res = [*set(list1)]

#printing the domains with Ip Addresses 
for i in res:
    try:
        print(i," : ", socket.gethostbyname(i),file = File)
    except:
        pass
