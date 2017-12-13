import csv


with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print (dates)
    print (colors)


    whatColor = input ('what color do you wish to know of?:')
    colordex = colors.index(whatColor)
    theDate = dates [colordex]
    print ("The Date of", whatColor, 'is:', theDate)


    
