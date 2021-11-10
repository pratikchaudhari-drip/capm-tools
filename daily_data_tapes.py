import pandas as pd
from db_connector import db
from tapes import grabber
from utils import writer

df_sf = grabber.query_tape(type = 'sf')
df_scf = grabber.query_tape(type = 'scf')

writer.write_file(df_sf, 'csv')
writer.write_file(df_scf, 'csv')
