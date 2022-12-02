import csv
import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--input_file', dest="inF")
parser.add_argument('--separator', dest="sep")
parser.add_argument('--output_file', dest="outF")

args = parser.parse_args()

data = []

with open(args.inF,'r') as o:
    reader = csv.reader(o, quotechar=args.sep)

    for line in reader:
        print(line)

        data.append(line)


with open(args.outF,'w') as o:
    json.dump(data,o,ensure_ascii=False)   
