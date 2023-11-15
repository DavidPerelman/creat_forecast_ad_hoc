from forecast import forecast
from functions import make_point, up_load_gdb

folder_path_save=r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data'
folder_path=r'{}\needed_files'.format(folder_path_save)
gpd_name='subdistrict2008.gdb'

forecast_point = make_point(forecast)

subdistrict_il = up_load_gdb(r'{}\{}'.format(folder_path,gpd_name),'subdistrict2008_ITM')
print(subdistrict_il)
