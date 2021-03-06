import json
import requests
import numpy as np  
from scipy import spatial



url = 'http://localhost:5010'

def cosineSimilarity(x1, x2):
    return  spatial.distance.cosine(x1, x2)


def getVector(array):
    myobj = {"sentences":array }
    data = json.dumps(myobj)

    resultVec = []

    x = requests.post(url, data = data)
    vector = x.json()['vector']
    for i in range(len(array)):
        resultVec.append([array[i], vector[i]])

    return resultVec

# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = cosineSimilarity(test_row[1], train_row[1])
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors


def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[0] for row in neighbors]
    return output_values


# sent = ['I love machine learning and covid-19 ', 'machine learning is fun', 'covid-19 is very dangerous', 'deep learning requires more data']
# vec = getVector(sent)
# print(predict_classification(vec[1:], vec[0], 2))
