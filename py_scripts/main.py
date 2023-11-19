import pandas as pd
from forecast import forecast

forecast_version='with_project_50_precent_bld'
folder_path_save=r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data'
file_date=pd.Timestamp.today().strftime('%y%m%d')
v_date='230818'
index_file_name='index_format_for_creating_forecast_jtmt_input_{}_{}'.format(forecast_version,v_date)
v_date='230818'

print(index_file_name)