import pymysql
import pandas as pd
from db_connector import ssh_tunnel as ssh


def open_prod_cxn(
    tunnel=ssh.open_tunnel()
    , db_user=ssh.SSH_UNAME
    , db_pw=ssh.SSH_PASS
    ):
    
    cxn_prod = pymysql.connect(host='127.0.0.1'
                          , user=ssh.SSH_UNAME
                          , passwd=ssh.SSH_PASS
                          , port=tunnel.local_bind_port
#                           , db='drip_prod'
                          )
    
    return cxn_prod


def open_warehouse_cxn(
    tunnel=ssh.open_tunnel(DB_HOST=ssh.DB_WH_HOST)
    , db_user=ssh.SSH_UNAME
    , db_pw=ssh.SSH_PASS
    ):
    
    cxn_warehouse = pymysql.connect(host='127.0.0.1'
                          , user=ssh.SSH_UNAME
                          , passwd=ssh.SSH_PASS
                          , port=tunnel.local_bind_port
#                           , db='drip_warehouse'
                          )
    
    return cxn_warehouse



def get_data(sql, db='prod'):
    
    tunnel = ssh.open_tunnel()
    if db == 'prod':
        cxn = open_prod_cxn()
    elif db == 'warehouse':
        cxn = open_warehouse_cxn()
    else:
        print('Database not properly specified')
        
    df = pd.read_sql_query(sql, cxn)
    cxn.close()
    ssh.close_tunnel(tunnel)

    return df
