import csv
import pprint
import numpy as np

N=120
M=160
F_STEP=2
STEP=3

with open('gazou-4.csv') as f:
    reader = list(csv.reader(f))

sheet_num = len(reader)
#print(sheet_num)
#empty_list = [ [0]*M ]*N

k=0
while ( F_STEP + ( N + STEP )*k  ) < sheet_num - (N + STEP) :
#while k < 10 :
    empty_list = [ [0]*M ]*N
    for i in range(N):
        for j in range(M):
            temper = int( reader[ i + F_STEP + ( STEP + N )*k ] [ j ] )  - 27315  
            #temper =float( ( int(reader[ i + F_STEP + ( STEP + N )*k ][j]) - 27315 ) / 100)
            empty_list[i][j] = temper

        with open('gazou_04.csv', 'a') as ff:
            writer = csv.writer(ff)
            writer.writerow(empty_list[i])
    
    k = k +1

