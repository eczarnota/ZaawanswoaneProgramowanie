import csv
from movie import Movie
objects =[]
def opens(files, classRef) -> str:
    with open(files,'r', encoding='utf-8') as f:
        csvreader = csv.reader(f, delimiter=',')
        headers = next(csvreader)
        print(headers)
        for line in csvreader:
            if len(line) == len(headers):
                classObj = {}
                for i, header in enumerate(headers):
                    classObj[header] = line[i]

                object = classRef(**classObj)
                objects.append(object.__dict__)
        return objects


