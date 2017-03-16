


# 1. read userReviewerID folder
    # 1.1. cd userReviewerId folder
    # 1.2. read userReviewerId.csv
        # 1.2.0 make data.csv in userReviewerId.csv
        # 1.2.1 read one line (reviewerID, asin, reviewerName, helpful, reviewText, overall, summary, unixReviewTime, reviewTime
        # 1.2.2 get asin, overall
        # 1.2.3 search asin in kcore_5.json.gz
        # 1.2.4 write item csv file (asin, price, salesRank, Brand, Categories, Overall)


import os
import pandas as pd
import gzip
import csv
import json

def parse(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield eval(l)

def getAsinInformation(path, asin):
    i = 0
    df = {}
    for d in parse(path):
        if d["asin"] == asin:
            return d

def getTemp(path, asin):
    i = 0
    with open(path, 'r') as f:
        for line in f:
            dict = json.loads(line)
            if dict['asin'] == '0000031852':
                return dict

outputPath = '/storage1/data/output/'

def search(dirname):
    reviewerFolder = os.listdir(dirname)
    for filename in reviewerFolder:
        full_filename = os.path.join(dirname, filename)
        if os.path.isdir(full_filename):
             with open(full_filename + '/' + filename + '.csv', 'r') as input:
                csvReader = csv.reader(input, delimiter=',')
                userData = pd.DataFrame(columns=("asin", "price", "salesRank", "brand", "categories", "overall"))

                for row in csvReader:
                    # row[0] : reviewerID
                    # row[1] : asin
                    # row[2] : overall
                    # row[3] : unixReviewTime
                    asin = row[1]
                    overall = row[2]
                    # search asin in kcore_5.json.gz
                    df = getAsinInformation('/storage1/data/input/metadata.json.gz', asin)
                    # df = getTemp('/storage1/data/input/data.txt', asin)
                    # write item csv file (asin, price, salesRank, Brand, Categories, Overall)
                    # print(df.keys())
                    print(df)
                    if df != None:
                        if 'brand' not in df.keys():
                            df["brand"] = None
                        if 'categories' not in df.keys():
                            df["categories"] = None
                        if 'price' not in df.keys():
                            df["price"] = None
                        if 'salesRank' not in df.keys():
                            df["salesRank"] = None
                        userData.loc[len(userData)] = [asin, df["price"], df["salesRank"], df["brand"], df["categories"], overall]
                        print(userData)
                # write output folder
                outputFolder = outputPath + filename
                if not os.path.exists(outputFolder):
                    os.makedirs(outputFolder)
                with open(outputFolder + '/' + filename + '.csv', 'a+') as csvfile:
                    userData.to_csv(csvfile, sep=",", index=False)


search('/storage1/data/input/data_per_user/')