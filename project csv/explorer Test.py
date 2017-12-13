import csv


with open ("example.csv") as csvfile:
    ExplorerCSV = csv.reader(csvfile, delimiter = ',')
    topics = []
    positivity_Scores = []

    for row in ExplorerCSV:
        topic = row[0]
        positivity_score = row[2]


        topics.append(topic)
        positivity_Scores.append(positivity_score)

    print(positivity_Scores)
    
    for i in range(len(topics)):
        print (topics[i])
    for i in range(len(positivity_Scores)):
        print (positivity_Scores[i])
    
