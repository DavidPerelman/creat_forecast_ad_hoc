from forecast import forecast
from functions import make_point, up_load_gdb

forecast_point = make_point(forecast)

subdistrict_il=up_load_gdb( r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data\needed_files\subdistrict2008.gdb','subdistrict2008_ITM')

muni_JTMT=up_load_gdb( r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data\needed_files\MUNI_border.gdb','muni_under_JTMT_ITM')

# jeru_metro_jtmt_border=up_load_shp(r'\\FILE-SRV\Jtmt\projections_team\GIS_backround\INFO\צתאל\221114_גבול_מטרופולין\jeru_metro_jtmt_border_221114.shp')
