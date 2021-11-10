from utils.formatting import datetime_to_str

def write_file(
    df
    , filetype
    , filepath = '.\\tapes\\tape_drip-{}.{}'
    ):

    filepath = filepath.format(datetime_to_str(), filetype)

    if filetype == 'csv':
        df.to_csv(filepath)
    elif filetype == 'xlsx':
        df.to_excel(filepath)
    elif filetype == 'pkl':
        df.to_pickle(filepath)
