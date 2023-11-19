import pandas as pd
from functions import up_load_df, up_load_shp
from main import folder_path_save, file_date, index_file_name

borders_index=up_load_shp(r'{}\For_approval\Reference_tabels\shp\gvul_index.shp'.format(folder_path_save))

index=up_load_df(r'{}\For_approval\Reference_tabels'.format(folder_path_save),index_file_name)

index=pd.merge(borders_index,index,on='id',how='right')
