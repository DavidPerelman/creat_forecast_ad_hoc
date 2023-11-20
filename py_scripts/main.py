import pandas as pd
from forecast import forecast
from geographical_features import add_geographical_Features
from uploading_index_table_elements import uploading_index_table
# from index_layer import index_layer_fun

forecast_version='with_project_50_precent_bld'
folder_path_save=r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data'
file_date=pd.Timestamp.today().strftime('%y%m%d')
v_date='230818'
index_file_name='index_format_for_creating_forecast_jtmt_input_{}_{}'.format(forecast_version,v_date)
v_date='230818'

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#### הוספת מאפיינים גיאוגרפים לאזורי תנועה
forecast=add_geographical_Features(forecast)
folder_path_save=r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data'
index=uploading_index_table(forecast, folder_path_save, index_file_name)

# index_layer=index_layer_fun(index)
# print(index_layer)