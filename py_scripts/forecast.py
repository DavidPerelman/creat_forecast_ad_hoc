from functions import up_load_gdb

# xl = pd.ExcelFile(r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data\קבצים לדוד מגדעון.xlsx') 
# df = xl.parse('גיליון1') 

# print(df['שם הקובץ'][0])

def createForcast(folder_path_save):
    print(folder_path_save)
    folder_path=r'{}\needed_files'.format(folder_path_save)
    gpd_name='tochnit_check.gdb'

    forecast = up_load_gdb(r'{}\{}'.format(folder_path,gpd_name),'TAZ_211028_V3_Published_with_client_changes')
    return forecast

# forecast=createForcast(folder_path_save)
