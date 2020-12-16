import csv
import os

statePopulations = {"california": 39510000, "florida": 21480000, "new york": 19450000, "texas": 29000000, "oklahoma":3957000}


def readLines(stateCsv, output, state):
    rows = []
    field = ["Date", "Case increase (per 100,000)"]

    if os.path.exists(output):

        os.remove(output)

    with open(stateCsv) as cali:
        lines = csv.reader(cali)
        for i, k in enumerate(lines):

            newlist = []

            if i != 0:
                casesPerDay = int(k[22])

                statePopDivided = statePopulations[state]/100000

                per100 = casesPerDay/statePopDivided

                newlist.append(k[0])

                newlist.append(per100)

                rows.append(newlist)
        print(rows)
    with open(output, "w") as pog:
        writer = csv.writer(pog)
        writer.writerow(field)
        writer.writerows(rows)
    return rows


def getAllDataValues(inputList):
    allRows = inputList
    newList = []
    for i in range(len(allRows)):
        newList.append(allRows[i][1])
    return newList


def getAllDates(inputList):
    allRows = inputList
    newList = []
    for i in range(len(allRows)):
        newList.append(allRows[i][0])
    return newList


def movingAverage(unParsed, size=7):
    listNums = unParsed
    averagePeriod = size
    i = 0
    averages = []
    while i < len(listNums) - averagePeriod + 1:
        currentWindow = listNums[i:i+averagePeriod]

        averageOfPeriod = sum(currentWindow)/averagePeriod
        averages.append(averageOfPeriod)
        i += 1

    return averages


def linkAverages(dates, newValues):
    print(dates)
    print(newValues)
    finalList = []
    for i in range(len(newValues)):
        tempList = []
        date = dates[i]
        values = newValues[i]
        tempList.append(date)
        tempList.append(values)
        finalList.append(tempList)
    return finalList


def formNewDataSet(originalCsv, outputLocation, state):
    lol = linkAverages(getAllDates(readLines(originalCsv, outputLocation, state)), movingAverage(getAllDataValues(readLines(originalCsv, outputLocation, state))))
    return lol


def sevenDayCSV(inputList, outputLocation):
    field = ["Date", "(7 day moving average) Case increases(per 100,000)"]
    if os.path.exists(outputLocation):
        os.remove(outputLocation)
    with open(outputLocation, "w") as pog:
        writer = csv.writer(pog)
        writer.writerow(field)
        writer.writerows(inputList)


dir = "C:/Users/doget/PycharmProjects/data/parsed/"
baseDir = "C:/Users/doget/PycharmProjects/data/raw historical/"
readLines(baseDir + "california-history.csv", dir + "/cali.csv", "california")
readLines(baseDir + "texas-history.csv", dir + "/texas.csv", "texas")
readLines(baseDir + "new-york-history.csv", dir + "/ny.csv", "new york")
readLines(baseDir + "oklahoma-history.csv", dir + "/oklahoma.csv", "oklahoma")
readLines(baseDir + "florida-history.csv", dir + "/florida.csv", "florida")

caliNewList = formNewDataSet(baseDir + "california-history.csv", dir + "cali.csv", "california")

florNewList = formNewDataSet(baseDir + "florida-history.csv", dir + "florida.csv", "florida")

nyNewList = formNewDataSet(baseDir + "new-york-history.csv", dir + "ny.csv", "new york")

okNewList = formNewDataSet(baseDir + "oklahoma-history.csv", dir + "oklahoma.csv", "oklahoma")

texasNewList = formNewDataSet(baseDir + "texas-history.csv", dir + "texas.csv", "texas")


newListsForCSV = [caliNewList, florNewList, nyNewList, okNewList, texasNewList]
fileNames = ["cali7day.csv", "florida7day.csv", "ny7day.csv", "ok7day.csv", "texas7day.csv"]
directory = "C:/Users/doget/PycharmProjects/data/7day-average/"

for i in range(len(newListsForCSV)):
    sevenDayCSV(newListsForCSV[i], directory + fileNames[i])

