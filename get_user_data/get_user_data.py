import csv
import os

with open("/storage1/data/input/item_dedup.csv", 'r') as input:
    csvReader = csv.reader(input)
    for row in csvReader:
        # make reviewerID folder
        folderPath = r'/storage1/data/input/data_per_user/'
        reviewerID = row[0]
        folderPath += reviewerID
        if not os.path.exists(folderPath):
            os.makedirs(folderPath)
        # row[0] : reviewerID
        # row[1] : asin
        # row[2] : overall
        # row[3] : unixReviewTime
        with open(folderPath + "/" + reviewerID + ".csv", 'a') as userDataFile:
            csvWriter = csv.writer(userDataFile)
            csvWriter.writerow(row)