#imports regexp module that will be used to find requests from years 1994 and 1995.
import re

#imports csv module that will be used to show results.
import csv

#imports counter module used to count and subsequently write number of requests to csv files
from collections import Counter

#Fetches data
import urllib.request
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
urllib.request.urlretrieve(url,'./http_access_log.txt')

#Reads log file and finds all 1994 requests
def reader(filename):
    with open(filename) as f:
        http_access_log = f.read()

        firstyear = re.findall("1994", http_access_log)

        return(firstyear)
    
#Reads log file and finds all 1995 requests
def reader2(filename):
    with open(filename) as f:
        http_access_log = f.read()

        secondyear = re.findall("1995", http_access_log)
        return(secondyear)
    
#Counts 1994 requests
def count(firstyear):
    return Counter(firstyear)

#Counts 1995 requests
def count2(secondyear):
    return Counter(secondyear)

#creates csv file for 1994
def write_csv(counter):
    with open("1994.csv", "w") as csvfile:
        writer = csv.writer(csvfile)

        header = ["Year", "Requests"]

        writer.writerow(header)

        for item in counter:
            writer.writerow( (item, counter[item]) )
            
#creates csv file for 1995
def write_csv2(counter2):
    with open("1995.csv", "w") as csvfile:
        writer = csv.writer(csvfile)

        header = ["Year", "Requests"]

        writer.writerow(header)

        for item in counter2:
            writer.writerow( (item, counter2[item]) )


if __name__ == "__main__":
    write_csv(count(reader("http_access_log.txt")))
    write_csv2(count2(reader2("http_access_log.txt")))

