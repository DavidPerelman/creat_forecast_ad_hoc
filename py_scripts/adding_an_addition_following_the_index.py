from functions import up_load_df

def adding_an_addition(index_by_taz,forecast,forecast_2020):
    print(forecast)
    col=[ 'add_aprt','add_uni_dorms', 'add_emp_Business',
    'add_emp_Commerce',
    'add_emp_Industry',
    'add_emp_Public',
    'add_emp_Tourism','add_uni_students','add_old_age_home','Classrooms']

    forecast=forecast.merge(index_by_taz[col],left_index=True,right_index=True,how='left')

    forecast=forecast.fillna(0)

    col=['aprt_20','student','uni_students','student_dorms','student_yeshiva','emp_not_okev']

    forecast_2020=forecast_2020.set_index('Taz_num')

    forecast=forecast.merge(forecast_2020[col],left_index=True,right_index=True,how='left')

    forecast=forecast.rename(columns={'student':'student_20','uni_students':'uni_students_20','student_dorms':'student_dorms_20','student_yeshiva':'student_yeshiva_and_kollim_20','emp_not_okev':'emp_not_okev_20'})

    age_des_types=up_load_df(r'C:\Users\dpere\Documents\JTMT\creat_forecast_ad_hoc\data\backround_files','age_des_types')

    forecast=forecast.merge(age_des_types,on='classification_name',how='left').fillna(0)

    return forecast