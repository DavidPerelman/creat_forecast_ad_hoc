import pandas as pd
from functions import split_index_by_taz, up_load_df, up_load_shp
# from main import forecast, folder_path_save, index_file_name

def uploading_index_table(forecast, folder_path_save, index_file_name):
    borders_index=up_load_shp(r'{}\For_approval\Reference_tabels\shp\gvul_index.shp'.format(folder_path_save))

    index=up_load_df(r'{}\For_approval\Reference_tabels'.format(folder_path_save),index_file_name)

    index=pd.merge(borders_index,index,on='id',how='right')
   
    return index