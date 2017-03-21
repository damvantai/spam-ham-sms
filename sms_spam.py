import csv
import pandas as pd
import numpy as np
# data = pd.read_csv('train.txt', error_bad_lines=False, delimiter=' ', names=["label", "sms"])
# print(data)

# data = pd.read_csv("train",error_bad_lines=False, encoding='utf8', sep=' ')
# data = np.array
# print data

numberLine = 0
label = []
message = [[]]


with open('train.txt', 'r') as f:
	text = f.readlines()
	
for line in text:
    message[numberLine] = line.split(' ')
    label.append(message[numberLine][0])
    message[numberLine].__delitem__(0)
    numberLine += 1
    print (label)
#     for line in f:
#         message[numberLine] = line.split(' ')
#         label.append(message[numberLine][0])
#         message[numberLine].__delitem__(0)
#         numberLine += 1
#         print (label)
print(message[0])
print(label)
