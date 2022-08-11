import sys
import random
import pandas as pd
from burrows import Burrows

def generate_dataset(csv_name,rows):
    pure_str = []
    bwt_list = []

    while len(pure_str) != rows:
        genome = ''.join(random.choice(['A','T','G','C']) for _ in range(random.randint(5,9)))
        pure_str.append(genome)

        pure_str = list(set(pure_str))

    bwt_list = [Burrows(x).bwt() for x in pure_str]

    df = pd.DataFrame()
    df['String'] = pure_str
    df['BWT_string'] = bwt_list

    if '.csv' not in csv_name:
        csv_name = f'{csv_name}.csv'
    df.to_csv(csv_name,index=False)

if __name__ == '__main__':
    name = sys.argv[1]
    rows = int(sys.argv[2])
    generate_dataset(name,rows)