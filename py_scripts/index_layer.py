import pandas as pd
from main import index

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def index_layer_fun(index):

    index=index.fillna(0)

    # print(index)

    convert_dict={
    'add_old_age_home': float,
    'add_aprt': float,
    'Commerce_m2': float,
    'Business_m2': float,
    'Tourism_m2': float,
    'Public_m2': float,
    'Industry_m2': float,
    'emp_Public': float,
    'emp_Education': float,
    'emp_Commerce': float,
    'emp_Business': float,
    'emp_Industry': float,
    'emp_Tourism': float,
    'Classrooms': float,
    'F2025': float,
    'F2030': float,
    'F2035': float,
    'F2040': float,
    'F2045': float,
    'F2050': float,
    'F2050_plus': float,
    'Risk_factor': float,
    'emp_fill_factor': float}

    index = index.astype(convert_dict)

    col_to_sum=['F2025',
    'F2030',
    'F2035',
    'F2040']

    index['precent_till_2040']=index[col_to_sum].sum(axis=1)

    index['add_aprt_nominally']=index['add_aprt']

    index['add_aprt']=index['add_aprt']*index['precent_till_2040']*index['Risk_factor']

    index['Classrooms_nominally']=index['Classrooms']

    index['Classrooms']=index['Classrooms']*index['precent_till_2040']*index['Risk_factor']

    index['add_old_age_home_nominally']=index['add_old_age_home']

    index['add_old_age_home']=index['add_old_age_home']*index['precent_till_2040']*index['Risk_factor']

    index['add_uni_students_nominally']=index['add_uni_students']

    index['add_uni_students']=index['add_uni_students']*index['precent_till_2040']*index['Risk_factor']

    index['add_uni_dorms_nominally']=index['add_uni_dorms']

    index['add_uni_dorms']=index['add_uni_dorms']*index['precent_till_2040']*index['Risk_factor']

    list_category=['Commerce','Business','Industry','Tourism','Public']   #'Agriculture','Education','Public'
    for c in list_category:
        index['{}_m2_nominally'.format(c)]=index['{}_m2'.format(c)]
        index['{}_m2'.format(c)]=index['{}_m2'.format(c)]*index['Risk_factor']*index['emp_fill_factor']*index['precent_till_2040']
        index['emp_{}_nominally'.format(c)]=index['emp_{}'.format(c)]
        index['emp_{}'.format(c)]=index['emp_{}'.format(c)]*index['precent_till_2040']*index['Risk_factor']*index['emp_fill_factor']
        index['add_emp_{}'.format(c)]=index['emp_{}'.format(c)]+index['{}_m2'.format(c)]/locals()['m2_{}_to_emp'.format(c)]

        index_by_taz=index.pivot_table(index='Taz_num',aggfunc=sum).fillna(0)
        print(index_by_taz)
    return index

index_layer_fun(index)