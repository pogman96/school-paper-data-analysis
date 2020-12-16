import pandas
import plotly.express as px

# def showGraph(stateName):

# lol = pandas.read_csv("https://raw.githubusercontent.com/pogman96/covidschooldata/main/parsed/cali.csv")
# fig = px.line(lol, x='Date', y='Case increase (per 100,000)', title='Data plotting of California Coronavirus Cases')
# fig.show()


def askContinuation():
    while True:
        shouldContinue = input("Would you like to see another graph?(y/n): ")
        if shouldContinue.lower() == "y":
            return True
        elif shouldContinue.lower() == "n":
            return False
        else:
            print("Invalid input")
            continue


statesDict = {"california": ["https://raw.githubusercontent.com/pogman96/school-paper-data-analysis/main/7day-average/cali7day.csv",
                            "https://raw.githubusercontent.com/pogman96/school-paper-data-analysis/main/parsed/cali.csv"],
              "florida": ["https://raw.githubusercontent.com/pogman96/school-paper-data-analysis/main/7day-average/florida7day.csv",
                         "https://raw.githubusercontent.com/pogman96/school-paper-data-analysis/main/parsed/florida.csv"],
              "new york": ["https://raw.githubusercontent.com/pogman96/school-paper-data-analysis/main/7day-average/ny7day.csv",
                          "https://raw.githubusercontent.com/pogman96/school-paper-data-analysis/main/parsed/ny.csv"],
              "oklahoma": ["https://raw.githubusercontent.com/pogman96/school-paper-data-analysis/main/7day-average/ok7day.csv",
                          "https://raw.githubusercontent.com/pogman96/school-paper-data-analysis/main/parsed/oklahoma.csv"],
              "texas": ["https://raw.githubusercontent.com/pogman96/school-paper-data-analysis/main/7day-average/texas7day.csv",
                       "https://raw.githubusercontent.com/pogman96/school-paper-data-analysis/main/parsed/texas.csv"]}

satisfied = False
while not satisfied:
    uInput = input("State?: ").lower()

    if uInput in statesDict:
        graphChoice = int(input("What type of graph?\n1. 7-day average\n2. raw data\n"))

        while graphChoice != 1 or graphChoice != 2:

            if float(graphChoice).is_integer() and 1 <= graphChoice <= 2:
                data = pandas.read_csv(statesDict[uInput][int(graphChoice)-1])

                if graphChoice == 2:
                    yAxis = "Case increase (per 100,000)"
                    fig = px.line(data, x='Date', y=yAxis,
                                  title='Data plotting of ' + uInput.capitalize() + '\'s Coronavirus Cases')
                    fig.show()
                    if askContinuation():
                        break

                    else:
                        satisfied = True
                        break

                else:
                    yAxis = "(7 day moving average) Case increases(per 100,000)"
                    fig = px.line(data, x='Date', y=yAxis,
                                  title='Data plotting of ' + uInput.capitalize() + '\'s Coronavirus Cases')
                    fig.show()
                    if askContinuation():
                        break

                    else:
                        satisfied = True
                        break
            else:
                print("Input not valid")
                break
    else:
        print("Sorry state not found")
        print("Here is a list of all states\n")
        for i in statesDict:
            print(i.capitalize())
        print()
