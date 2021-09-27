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

#Reads log file and finds past 6 months 
def reader3(filename):
    with open(filename) as f:
        http_access_log = f.read()

        month1 = re.findall("May/1995", http_access_log)
        month2 = re.findall("Jun/1995", http_access_log)
        month3 = re.findall("Jul/1995", http_access_log)
        month4 = re.findall("Aug/1995", http_access_log)
        month5 = re.findall("Sep/1995", http_access_log)
        month6 = re.findall("Oct/1995", http_access_log)
        past_6_months_total = month1 + month2 + month3 + month4 + month5  + month6

        return(past_6_months_total)       
    
#Counts 1994 requests
def count(firstyear):
    return Counter(firstyear)

#Counts 1995 requests
def count2(secondyear):
    return Counter(secondyear)

#Counts past 6 months:
def count3(past_6_months_total):
    return Counter(past_6_months_total)

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

#creates csv file for past 6 months
def write_csv3(counter3):
    with open("6months.csv", "w") as csvfile:
        writer = csv.writer(csvfile)

        header = ["Past 6 Months", "Requests"]

        writer.writerow(header)

        for item in counter3:
            writer.writerow( (item, counter3[item]) )


if __name__ == "__main__":
    write_csv(count(reader("http_access_log.txt")))
    write_csv2(count2(reader2("http_access_log.txt")))
    write_csv3(count3(reader3("http_access_log.txt")))

