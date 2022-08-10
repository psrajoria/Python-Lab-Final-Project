import sys
import string
import random
import pandas as pd
from burrows import Burrows

def generate_dataset(csv_name,rows):
    pure_str = []
    bwt_list = []
    for i in range(0,rows):
        genome = ''.join(random.choice(string.ascii_uppercase) for _ in range(random.randint(6,8)))
        # b = Burrows(genome)
            # bwt_str = b.bwt()
        pure_str.append(genome)
            # bwt_list.append(bwt_str)

    pure_str = list(set(pure_str))
    bwt_list = [Burrows(x).bwt() for x in pure_str]

    # bwt_list = list(set(bwt_list))
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