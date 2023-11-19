import pandas as pd
from functions import split_index_by_taz, up_load_df, up_load_shp
# from main import forecast, folder_path_save, index_file_name

def uploading_index_table(forecast, folder_path_save, index_file_name):
    borders_index=up_load_shp(r'{}\For_approval\Reference_tabels\shp\gvul_index.shp'.format(folder_path_save))

    index=up_load_df(r'{}\For_approval\Reference_tabels'.format(folder_path_save),index_file_name)

    index=pd.merge(borders_index,index,on='id',how='right')

    col=['add_uni_dorms',
    'add_old_age_home',
    'add_aprt',
    'Commerce_m2',
    'Business_m2',
    'Tourism_m2',
    'Public_m2',
    'Industry_m2',
    'emp_Public',
    'emp_Education',
    'emp_Commerce',
    'emp_Business',
    'emp_Industry',
    'emp_Tourism',
    'Classrooms',
    'add_uni_students']

    index=split_index_by_taz(index,forecast,0.05,col)
    return index