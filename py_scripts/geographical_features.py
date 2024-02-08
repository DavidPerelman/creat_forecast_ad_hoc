import pandas as pd
from functions import make_point, up_load_gdb, up_load_shp

def add_geographical_Features(forecast, software_data_folder_location):
    forecast_point = make_point(forecast)

    DISTRICT=up_load_gdb( r'{}\background_files\GIS_jtmt_forcast_v_3_2_Published.gdb'.format(software_data_folder_location),'TAZ_V3_2_220123_DISTRICT')
    urban=up_load_gdb( r'{}\background_files\GIS_jtmt_forcast_v_3_2_Published.gdb'.format(software_data_folder_location),'TAZ_V3_2_220123_urban')
    SCHOOLDISTRICT=up_load_gdb( r'{}\background_files\GIS_jtmt_forcast_v_3_2_Published.gdb'.format(software_data_folder_location),'TAZ_V3_2_220123_SCHOOLDISTRICT')
    PUMA=up_load_gdb( r'{}\background_files\GIS_jtmt_forcast_v_3_2_Published.gdb'.format(software_data_folder_location),'TAZ_V3_2_220123_PUMA')
    jerusalem_city=up_load_gdb( r'{}\background_files\GIS_jtmt_forcast_v_3_2_Published.gdb'.format(software_data_folder_location),'TAZ_V3_2_220123_In_jerusal')


    forecast_point_DISTRICT=forecast_point.sjoin(DISTRICT)[['Taz_num','DISTRICT']]
    forecast_point_urban=forecast_point.sjoin(urban)[['Taz_num','urban']]
    forecast_point_SCHOOLDISTRICT=forecast_point.sjoin(SCHOOLDISTRICT)[['Taz_num','SCHOOLDISTRICT']]
    forecast_point_PUMA=forecast_point.sjoin(PUMA)[['Taz_num','PUMA']]
    forecast_point_jerusalem_city=forecast_point.sjoin(jerusalem_city)[['Taz_num','In_jerusal']]

    subdistrict_il=up_load_gdb( r'{}\background_files\subdistrict2008.gdb'.format(software_data_folder_location),'subdistrict2008_ITM')

    muni_JTMT=up_load_gdb( r'{}\background_files\MUNI_border.gdb'.format(software_data_folder_location),'muni_under_JTMT_ITM')

    jeru_metro_jtmt_border=up_load_shp( r'{}\background_files\jeru_metro_jtmt_border_221114.shp'.format(software_data_folder_location))

    

    forecast_point_subdistrict_il=forecast_point.sjoin(subdistrict_il[['geometry','ENG_NAME_nafa']])[['Taz_num','ENG_NAME_nafa']]

    forecast_point_muni_JTMT=forecast_point.query('main_sector!="Palestinian"').sjoin(muni_JTMT[['Muni_Heb', 'Sug_Muni', 'CR_PNIM', 'geometry']])[['Taz_num','Muni_Heb', 'Sug_Muni', 'CR_PNIM']]

    forecast_point_jeru_metro_jtmt_border=forecast_point.sjoin(jeru_metro_jtmt_border)[['Taz_num','jeru_metro']]

    forecast = (forecast
            .merge(forecast_point_subdistrict_il, on='Taz_num', how='left')
            .merge(forecast_point_muni_JTMT, on='Taz_num', how='left')
            .merge(forecast_point_jeru_metro_jtmt_border, on='Taz_num', how='left')
            .merge(forecast_point_DISTRICT, on='Taz_num', how='left')
            .merge(forecast_point_urban, on='Taz_num', how='left')
            .merge(forecast_point_SCHOOLDISTRICT, on='Taz_num', how='left')
            .merge(forecast_point_PUMA, on='Taz_num', how='left')
            .merge(forecast_point_jerusalem_city, on='Taz_num', how='left'))


    forecast['zonetype']=forecast['ENG_NAME_nafa']

    forecast.loc[forecast['main_sector']=='Palestinian','zonetype']='Palestinian'

    forecast['in_jerusalem_metropolin']='yes'

    forecast.loc[forecast['jeru_metro']==0,'in_jerusalem_metropolin']='no'

    forecast['yosh']=0

    forecast.loc[forecast['zonetype']=='Judea and Samaria','yosh']=1

    forecast=forecast.set_index('Taz_num')

    forecast['Taz_num']=forecast.index

    return forecast