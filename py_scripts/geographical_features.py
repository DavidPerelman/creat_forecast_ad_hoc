from forecast import forecast
from functions import make_point, up_load_gdb, up_load_shp

forecast_point = make_point(forecast)

subdistrict_il=up_load_gdb( r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data\needed_files\subdistrict2008.gdb','subdistrict2008_ITM')

muni_JTMT=up_load_gdb( r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data\needed_files\MUNI_border.gdb','muni_under_JTMT_ITM')

jeru_metro_jtmt_border=up_load_shp( r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data\needed_files\jeru_metro_jtmt_border_221114.shp')

forecast_point_subdistrict_il=forecast_point.sjoin(subdistrict_il[['geometry','ENG_NAME_nafa']])[['Taz_num','ENG_NAME_nafa']]
print(forecast_point_subdistrict_il)
