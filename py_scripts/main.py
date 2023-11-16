import pandas as pd
from forecast import forecast

folder_path_save=r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data'
file_date=pd.Timestamp.today().strftime('%y%m%d')

# print(forecast)