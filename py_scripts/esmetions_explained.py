import pandas as pd

folder_path_save=r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data'
folder_path=r'{}\needed_files'.format(folder_path_save)

def up_load_df(folder_path,file_name):
    
    path_df=r'{}\{}.xlsx'.format(folder_path,file_name)
    df=pd.read_excel(path_df)
    df=df.dropna(how='all')
    return df

esmetions_explained=up_load_df(folder_path,'esmetions_explained').set_index('esmetions')

