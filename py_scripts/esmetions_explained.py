import pandas as pd

folder_path_save=r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data'
folder_path=r'{}\needed_files'.format(folder_path_save)
file_date=pd.Timestamp.today().strftime('%y%m%d')

def up_load_df(folder_path,file_name):
    
    path_df=r'{}\{}.xlsx'.format(folder_path,file_name)
    df=pd.read_excel(path_df)
    df=df.dropna(how='all')
    return df

esmetions_explained=up_load_df(folder_path,'esmetions_explained').set_index('esmetions')

lst=list(esmetions_explained.index)

# print(lst)

lsts = ['x', 'y', 'z']
x = 42
y = 56
z = 78

for l in lsts:
    print(locals())
    print(['{}'.format(l)])
    # print(locals()['{}'.format(l)])

# for l in lst:
#     print(lst)
    # print(esmetions_explained.loc['{}'.format(l),'explanation'])
    # print(locals()['{}'.format(l)])
    # esmetions_explained.loc['{}'.format(l),'value'] = locals()['{}'.format(l)]

# save_shp_path=r'{}\For_approval\Reference_tabels\{}_Coefficients_and_estimates_for_approval.xlsx'.format(folder_path_save,file_date)

# esmetions_explained.to_excel(save_shp_path)

# save_shp_path=r'{}\For_approval\{}_taz_for_approval.shp'.format(folder_path_save,file_date)
