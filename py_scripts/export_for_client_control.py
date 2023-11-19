from geographical_features import add_Ggeographical_Features
from main import file_date, folder_path_save
from forecast import forecast

save_shp_path=r'{}\For_approval\{}_taz_for_approval.shp'.format(folder_path_save,file_date)

forecast=add_Ggeographical_Features(forecast)

forecast.to_file(save_shp_path,index=False,encoding='UTF-8')