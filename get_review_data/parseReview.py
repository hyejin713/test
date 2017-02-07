import json
import datetime

CONFIG_FILE="./data/Musical_Instruments_5.json"
CONFIG={}
now = datetime.datetime.now()
nowDatetime = now.strftime('%Y%m%d%H%M')

def readConfig(line):
    js = json.loads(line)
    repos = js['reviewText']
    return repos + "\n"

def main() :
    global CONFIG_FILE
    global CONFIG

    fw = open("./output/review_only_" + nowDatetime + ".txt", 'a')

    fr = open(CONFIG_FILE, 'r')
    lines = fr.readlines()
    for line in lines:
        #print readConfig(line)
        fw.write(readConfig(line))
    fw.close()
    fr.close()

if __name__ == "__main__":
    main()