import os
import tqdm
import glob
import pandas as pd
import datetime as dt

cwd = os.getcwd()

data_dir = cwd + '\\__data__\\'

df = pd.read_csv(data_dir + 'tapes\\tape_drip-20190831.csv', index_col=0)
df = df.iloc[0:0]

for f in sorted(glob.glob(data_dir + 'tapes\\tape_drip-*.csv')):
    df1 = pd.read_csv(f, index_col=0)
    df = pd.concat([df, df1])

df.to_csv(data_dir + 'asset_level_monthly-{}.csv'.format(df['cutoff_date'].max().replace('-', '')))