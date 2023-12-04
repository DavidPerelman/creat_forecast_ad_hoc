import pandas as pd
from division_into_traffic_zones_of_plans import division_into_traffic_zones
from export_forecast_in_format import export_forecast_format
from export_geo_layer_for_client_control import export_layer
from forecast import createForcast
from geographical_features import add_geographical_Features
from index_layer import index_layer_fun
from status_exists_for_control import export_status_exists
from uploading_index_table_elements import uploading_index_table

forecast_version='with_project_50_precent_bld'
folder_path_save=r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data'
file_date=pd.Timestamp.today().strftime('%y%m%d')
v_date='230818'
index_file_name='index_format_for_creating_forecast_jtmt_input_{}_{}'.format(forecast_version,v_date)
v_date='230818'
save_shp_path=r'{}\For_approval\{}_taz_for_approval.shp'.format(folder_path_save,file_date)
save_excel_path=r'{}\For_approval\{}_forecast_2020_For_approval.xlsx'.format(folder_path_save,file_date)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

### הכנת טבלת בסיס לחישוב
forecast=createForcast()

#### הוספת מאפיינים גיאוגרפים לאזורי תנועה
forecast=add_geographical_Features(forecast)

# #### ייצוא שכבת אזורי תנועה לבקרת לקוח
# forecast=export_layer(forecast, folder_path_save, file_date)

# #### מצב קיים לבקרה
# forecast=export_status_exists(forecast, folder_path_save, file_date)

# #### ייצוא תחזית בפורמט
# forecast=export_forecast_format(forecast, folder_path_save, file_date)

#### העלאת מרכיבי טבלת אינדקס
# forecast=uploading_index_table(forecast, folder_path_save, file_date, index_file_name)
index=uploading_index_table(forecast, folder_path_save, index_file_name)

### חלוקה לאזורי תנועה של התכניות
divided_index=division_into_traffic_zones(index,forecast)

### שכבת אינדקס
index_layer=index_layer_fun(divided_index)
# print(index_layer.to_excel(r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc/index_layer.xlsx'))
print(index_layer)


print('Done')