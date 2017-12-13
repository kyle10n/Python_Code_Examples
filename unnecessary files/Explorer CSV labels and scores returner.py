#place this file inside the same folder as your CSV results file
#from explorer. >save as>csv file

#this script will take from each csv the topic and the corresponding sentiment and prevelance
#then output for easy copy pasting into excel for a nice table

import csv

#change the csvnames to the names of the files with quotes surrounding
#with a comma seperating the names
csvnames = ['bangkok_1_jwmarriott.csv',"bangkok_2_sheraton.csv","bangkok_3_mandarin.csv","bangkok_4_stregis.csv", "bangkok_5_shangrila.csv",
            "hongkong_1_fourseasons.csv","hongkong_2_grandhyatt.csv","hongkong_3_intercontinental.csv","hongkong_4_mandarin.csv","hongkong_5_sheraton.csv",
            "london_1_claridges.csv", "london_2_mandarin.csv","london_3_taj.csv","london_4_dorchester.csv","london_5_goring.csv","london_6_ritz.csv","london_7_savoy.csv"]
            

#list of labels you want to compare
#then just run the program
listoflabels = ["General_Feelings", "Service_Staff", "Staff", "Service", "Food", "Breakfast", "Bedroom_Bath_Bed", "Bedrooms", "Bathrooms", "Beds", "Decor", "lounge", "Location", "Pool_Spa_Gym", "Gym", "Pool", "Spa", "Cost", "Cleanliness"]
for names in csvnames:
    with open(names, encoding = 'utf-8') as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ',')


        labels = []
        scores = []
        prevelances = []

        for row in readCSV:
            label = row[1]
            score = row[8]
            prevelance = row[3]

            labels.append(label)
            scores.append(score)
            prevelances.append(prevelance)




    
    print(names)

    print("topic prevelance sentiment")
    for topics in listoflabels:

        j = [pos for pos, char in enumerate(labels) if char == topics]
        k = [pos for pos, char in enumerate(labels) if char == topics]

        print(topics, prevelances[k[0]], scores[j[0]])

    
