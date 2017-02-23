import pandas as pd
import gzip
import json
import csv
import re
import math

def parse(path):
    with open(path, "r") as f:
        for l in f:
            yield eval(l)

def getDF(path):
    i = 0
    df = {}
    for d in parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')

userJsonData = getDF('./data/user_review_data.json')
metaDataPath = getDF("./data/meta_simple_data.json")
# print(metaDataPath["related"])

print(metaDataPath.keys())

def isNan(num):
    return num != num

relatedMetadata = {}
relatedMetadata = metaDataPath["related"]
print(relatedMetadata)
changedData = {}
changedData[len(userJsonData)] = {}
i=0
for data in relatedMetadata:
    alsoBoughtSize = 0
    alsoViewedSize = 0
    alsoBoughtTogetherSize = 0
    buyAfterViewingSize = 0

    if isNan(data) == False:
        print(data.keys())
        # also_bought
        bought = data.get("also_bought", {})
        if bought is not None:
            alsoBoughtSize = len(bought)
        else:
            alsoBoughtSize = 0
        # also_viewed
        viewed = data.get("also_viewed", {})
        if viewed is not None:
            alsoViewedSize = len(viewed)
        else:
            alsoViewedSize = 0

        # bought_together
        boughtTogether = data.get("bought_together", {})
        if boughtTogether is not None:
            alsoBoughtTogetherSize = len(boughtTogether)
        else:
            alsoBoughtTogetherSize = 0

        # buy_after_viewing
        buyAfterViewing = data.get("buy_after_viewing", {})
        if buyAfterViewing is not None:
            buyAfterViewingSize = len(buyAfterViewing)
        else:
            buyAfterViewingSize = 0

    changedData[i] = {"also_bought": alsoBoughtSize, "also_viewed" : alsoViewedSize,
                      "bought_together" : alsoBoughtTogetherSize, "buy_after_viewing" : buyAfterViewingSize}
    i+=1

changedDataFrame = pd.DataFrame.from_dict(changedData, orient='index')
del metaDataPath["related"]

metaDataPath = pd.concat([changedDataFrame, metaDataPath], axis=1)
result = pd.concat([userJsonData, metaDataPath], axis=1)
print(result)
# convert price, also_bought_count, also_viewed_count, bought_togegher_count, salesRank, brand, categories, helpful, reviewText, overall, unixReviewTime
with open('./output/make_data.csv', 'w', newline='') as csvfile:
    userDataWriter = csv.writer(csvfile, delimiter=',')
    userData = pd.DataFrame(columns=("price", "also_bought_count", "also_viewed_count", "bought_together_count",
                                     "buy_after_viewing", "salesRank", "brand", "categories", "helpful", "reviewText",
                                     "overall", "unixReviewTime"))
    #price
    priceData = []
    for data in result['price']:
        if isNan(data) == False:
            priceData.append(int(data))
        else:
            priceData.append(0)
    userData["price"] = priceData

    #also_bought_count
    alsoBoughtCountData = []
    for data in result['also_bought']:
        if isNan(data) == False:
            alsoBoughtCountData.append(int(data))
        else:
            alsoBoughtCountData.append(0)
    userData["also_bought_count"] = alsoBoughtCountData

    #also_viewed_count
    alsoViewedCountData = []
    for data in result['also_viewed']:
        if isNan(data) == False:
            alsoViewedCountData.append(float(data))
        else:
            alsoViewedCountData.append(0)
    userData["also_viewed_count"] = alsoViewedCountData

    #bought_together_count
    boughtTogetherCountData = []
    for data in result['bought_together']:
        if isNan(data) == False:
            boughtTogetherCountData.append(float(data))
        else:
            boughtTogetherCountData.append(0)
    userData["bought_together_count"] = boughtTogetherCountData

    #buy_after_viewing
    buyAfterViewingCountData = []
    for data in result['buy_after_viewing']:
        if isNan(data) == False:
            buyAfterViewingCountData.append(float(data))
        else:
            buyAfterViewingCountData.append(0)
    userData["buy_after_viewing"] = buyAfterViewingCountData

    #salesRank
    salesRank = []
    for data in result['salesRank']:
        if isNan(data) == False:
            salesRank.append(data)
        else:
            salesRank.append("")
    userData["salesRank"] = salesRank

    #brand
    brand = []
    for data in result['brand']:
        if isNan(data) == False:
            brand.append(data)
        else:
            brand.append("")
    userData["brand"] = brand

    #category
    category = []
    for data in result['categories']:
        if isNan(data) == False:
            category.append(data)
        else:
            category.append("")
    userData["categories"] = category

    #helpful
    helpfulData = []
    for data in result['helpful']:
        if isNan(data) == False:
            m = re.compile(r'\[(\d+),\s(\d+)\]')
            matching = m.match(str(data))
            if int(matching.group(1)) != 0:
                helpfulData.append(round(float(int(matching.group(1))/int(matching.group(2))),2))
            else:
                helpfulData.append(0)
        else:
            helpfulData.append(0)
    userData["helpful"] = helpfulData

    #reviewText
    # priceData = []
    # for data in result['price']:
    #     priceData.append(float(data))
    # userData["price"] = priceData

    #overall
    overallData = []
    for data in result['overall']:
        if isNan(data) == False:
            overallData.append(float(data))
        else:
            overallData.append(0)
    userData["overall"] = overallData

    #unixReviewTime
    unixReviewTimeData = []
    for data in result['unixReviewTime']:
        if isNan(data) == False:
            unixReviewTimeData.append(int(data))
        else:
            unixReviewTimeData.append(0)
    userData["unixReviewTime"] = unixReviewTimeData

    userData.to_csv(csvfile, sep=",")
