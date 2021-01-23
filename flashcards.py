import csv
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('--file')
parser.add_argument('--start', type=int)
parser.add_argument('--end', type=int)
parser.add_argument('--subject')
args = parser.parse_args()

clues = []
with open(args.file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        clues.append({
            'clue': row['Clue'],
            'answer': row['Answer'],
            'subject': row['Subject']
        })

if args.subject:
    clues = list(filter(lambda x: x['subject'] == args.subject, clues))

if len(clues) == 0:
    print("No clues")
    raise Exception("No clues")

start = args.start if args.start else 0
end = args.end if args.end else len(clues)

while True:
    clue = clues[random.randrange(start, end)]
    val = input("Clue: {}".format(clue['clue']))
    print("Answer: {}".format(clue['answer']))
    if val == 'q' or val == 'quit':
        break