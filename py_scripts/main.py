import os
import pandas as pd
from adding_an_addition_following_the_index import adding_an_addition
from division_into_traffic_zones_of_plans import division_into_traffic_zones
from export_forecast_in_format import export_forecast_format
from export_geo_layer_for_client_control import export_geo_layer
from export_index_layer_for_client_control import export_index_layer
from forecast import createForcast
from geographical_features import add_geographical_Features
from index_layer import index_layer_fun
from status_exists_for_control import export_status_exists
from uploading_index_table_elements import uploading_index_table
from dotenv import load_dotenv, dotenv_values

load_dotenv()

forecast_version='with_project_50_precent_bld'
root_folder=os.getenv("root_folder")
folder_path_save=os.getenv("folder_path_save")
file_date=pd.Timestamp.today().strftime('%y%m%d')
v_date='230818'
index_file_name='index_format_for_creating_forecast_jtmt_input_{}_{}'.format(forecast_version,v_date)
v_date='230818'
save_shp_path=r'{}\For_approval\{}_taz_for_approval.shp'.format(folder_path_save,file_date)
save_excel_path=r'{}\For_approval\{}_forecast_2020_For_approval.xlsx'.format(folder_path_save,file_date)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

### הכנת טבלת בסיס לחישוב
forecast=createForcast(folder_path_save)

#### הוספת מאפיינים גיאוגרפים לאזורי תנועה
forecast=add_geographical_Features(forecast, folder_path_save)

# #### ייצוא שכבת אזורי תנועה לבקרת לקוח
# forecast=export_geo_layer(forecast, folder_path_save, file_date)

# #### מצב קיים לבקרה
forecast_2020=export_status_exists(forecast, folder_path_save, file_date)

# #### ייצוא תחזית בפורמט
forecast_2020_for_model=export_forecast_format(forecast, folder_path_save, file_date)

#### העלאת מרכיבי טבלת אינדקס
# forecast=uploading_index_table(forecast, folder_path_save, file_date, index_file_name)
index=uploading_index_table(forecast, folder_path_save, index_file_name)

### חלוקה לאזורי תנועה של התכניות
divided_index=division_into_traffic_zones(index,forecast)

### שכבת אינדקס
index_layer=index_layer_fun(divided_index)
# print(index_layer.to_excel(r'{}\index_layer.xlsx'.format(root_folder)))

#### ייצוא שכבת אינדקס לבקרת לקוח
# index_layer_for_client_control=export_index_layer(index_layer,folder_path_save,file_date,forecast_version)

### חישוב תחזית

#### הוספת תוספת בעקבות האינדקס
index_with_extension=adding_an_addition(index_layer,forecast,forecast_2020,folder_path_save,forecast_version)
# print(index_with_extension)

print('Done')