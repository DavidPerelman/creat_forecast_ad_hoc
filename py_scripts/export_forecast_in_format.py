import pandas as pd
from functions import up_load_df
# from status_exists import forecast
# from main import folder_path_save, file_date, forecast

def export_forecast_format(forecast, software_data_folder_location, file_date):
    col=['Taz_num',
    'yosh',
    'jeru_metro',
    'jerusalem_city',
    'main_sector',
    'hh',
    'pop',
    'pop_0',
    'pop_5',
    'pop_10',
    'pop_15',
    'pop_20',
    'pop_25',
    'pop_30',
    'pop_35',
    'pop_40',
    'pop_45',
    'pop_50',
    'pop_55',
    'pop_60',
    'pop_65',
    'pop_70',
    'pop_75up',
    'total_emp',
    'Indus',
    'Com_hotel',
    'Business',
    'Public',
    'emp_Education',
    'agri',
    'student',
    'uni_students',
    'student_yeshiva_and_kollim',
    'pop_emp_employed']

    col_new_name=['TAZ',
    'yosh',
    'in_jerusalem_metropolin',
    'jerusalem_city',
    'sector',
    'hh_total',
    'pop',
    'age0_4',
    'age5_9',
    'age10_14',
    'age15_19',
    'age20_24',
    'age25_29',
    'age30_34',
    'age35_39',
    'age40_44',
    'age45_49',
    'age50_54',
    'age55_59',
    'age60_64',
    'age65_69',
    'age70_74',
    'age75up',
    'emp_tot',
    'indus',
    'com_hotel',
    'business',
    'public',
    'education',
    'agri',
    'student',
    'univ',
    'UO_Hi_Ed',
    'pop_emp_employed']

    forecast_2020_for_model=up_load_df(r'{}\needed_files'.format(software_data_folder_location),'forecast_2020_230328')

    forecast_2020_for_model=pd.merge(forecast[[]].reset_index(),forecast_2020_for_model,how='left',left_on='Taz_num',right_on='TAZ').fillna(0)

    save_excel_path=r'{}\{}_forecast_2020.csv'.format(software_data_folder_location,file_date)

    forecast_2020_for_model.to_csv(save_excel_path,index=False)
    return forecast_2020_for_model