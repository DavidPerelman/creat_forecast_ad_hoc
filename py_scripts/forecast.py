import fiona
import geopandas as gpd
import pandas as pd

# xl = pd.ExcelFile(r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data\קבצים לדוד מגדעון.xlsx') 
# df = xl.parse('גיליון1') 

# print(df['שם הקובץ'][0])

folder_path_save=r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data'
folder_path=r'{}\needed_files'.format(folder_path_save)
gpd_name='tochnit_check.gdb'

# print(r'{}\{}'.format(folder_path,gpd_name))

def up_load_gdb(path, layer_name):
    path='{}'.format(path)
    layer_list=fiona.listlayers(path)
    gpd_layer=gpd.read_file(path, layer=layer_list.index(layer_name))
    return gpd_layer

forecast = up_load_gdb(r'{}\{}'.format(folder_path,gpd_name),'TAZ_211028_V3_Published_with_client_changes')