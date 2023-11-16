import pandas as pd
from main import file_date
from forecast import forecast, folder_path_save
from functions import make_point, up_load_gdb, up_load_shp

forecast_point = make_point(forecast)

subdistrict_il=up_load_gdb( r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data\needed_files\subdistrict2008.gdb','subdistrict2008_ITM')

muni_JTMT=up_load_gdb( r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data\needed_files\MUNI_border.gdb','muni_under_JTMT_ITM')

jeru_metro_jtmt_border=up_load_shp( r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data\needed_files\jeru_metro_jtmt_border_221114.shp')

forecast_point_subdistrict_il=forecast_point.sjoin(subdistrict_il[['geometry','ENG_NAME_nafa']])[['Taz_num','ENG_NAME_nafa']]

forecast_point_muni_JTMT=forecast_point.query('main_sector!="Palestinian"').sjoin(muni_JTMT[['Muni_Heb', 'Sug_Muni', 'CR_PNIM', 'geometry']])[['Taz_num','Muni_Heb', 'Sug_Muni', 'CR_PNIM']]

forecast_point_jeru_metro_jtmt_border=forecast_point.sjoin(jeru_metro_jtmt_border)[['Taz_num','jeru_metro']]

forecast=forecast.merge(forecast_point_subdistrict_il,on='Taz_num',how='left').merge(forecast_point_muni_JTMT,on='Taz_num',how='left').merge(forecast_point_jeru_metro_jtmt_border,on='Taz_num',how='left').fillna(0)

forecast['zonetype']=forecast['ENG_NAME_nafa']

forecast.loc[forecast['main_sector']=='Palestinian','zonetype']='Palestinian'

forecast['in_jerusalem_metropolin']='yes'

forecast.loc[forecast['jeru_metro']==0,'in_jerusalem_metropolin']='no'

forecast['yosh']=0

forecast.loc[forecast['zonetype']=='Judea and Samaria','yosh']=1

forecast['jerusalem_city']=1

forecast=forecast.set_index('Taz_num')

forecast['Taz_num']=forecast.index

save_shp_path=r'{}\For_approval\{}_taz_for_approval.shp'.format(folder_path_save,file_date)

# forecast.to_file(save_shp_path,index=False,encoding='UTF-8')