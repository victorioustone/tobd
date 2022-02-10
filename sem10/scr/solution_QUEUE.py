
from multiprocessing import Pool, Queue
import csv

def get_average_n_steps_for_tag(filename):
    
    average_n_steps_for_tag = {} 
    with open('./result/' + filename,  "r+") as csvfile:
        rows = csv.reader(csvfile, delimiter=';')
        header = next(rows)
        for row in rows:
            if row[1] in average_n_steps_for_tag.keys():
                average_n_steps_for_tag[row[1]][0] += int(row[2])
                average_n_steps_for_tag[row[1]][1] += 1
            else:
                average_n_steps_for_tag[row[1]] = [int(row[2]), 1]
    return average_n_steps_for_tag

def solution(q_in, q_out):
    while True:
        link = q_in.get()
        q_out.put(get_average_n_steps_for_tag(link))
