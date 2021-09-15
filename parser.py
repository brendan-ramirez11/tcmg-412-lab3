
import re
import csv
from collections import Counter

def reader(filename):
    with open(filename) as f:
        http_access_log = f.read()

        firstyear = re.findall("1994", http_access_log)

        return(firstyear)

def reader2(filename):
    with open(filename) as f:
        http_access_log = f.read()

        secondyear = re.findall("1995", http_access_log)
        return(secondyear)

def count(firstyear):
    return Counter(firstyear)

def count2(secondyear):
    return Counter(secondyear)

def write_csv(counter):
    with open("1994.csv", "w") as csvfile:
        writer = csv.writer(csvfile)

        header = ["Year", "Requests"]

        writer.writerow(header)

        for item in counter:
            writer.writerow( (item, counter[item]) )

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
 



