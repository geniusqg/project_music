# coding=utf8

import requests

car_info = {'car_id':'99884832423',
'car_business_type':'',
'car_brand':'AC Schnitzer',
'car_models':'AC Schnitzer M3',
'car_series':'2015款 AC Schnitzer ACS3 sport',
'car_color':'红色',
'car_state':'',
'air_displacement':'222',
'car_internal_color':'红色',
'vin_code':'1213123213123',
'car_category':'轿车',
'trip_mile':'12',
'engine_num':'',
'transfer_times':'2',
'register_date':'2015-12-3',
'brand_location':'',
'car_location':None,
'owner_name':None,
'owner_tel':None,
'force_insure_date':'',
'manufacture_date':'2015-12-3',
'use_property':'',
'emission_type':'',
'check_expire':'',
'plate_num':'',
'msg_src':'',
'car_config':'',
'fix_record':'',
'car_description':'',
'carrrrr':'rrrrr',
'air_displacement_unit': 'L'
}


#url = 'http://192.168.1.249:83/erp_api/get_eval_apply'
url = 'http://127.0.0.1:8000/erp_api/get_eval_apply'
try:
    for i in range(1):
        car_info['car_id'] = 'benchi1233333'+str(i)
        r = requests.post(url,car_info)
        print r.text,type(r.text),eval(r.text),type(eval(r.text))
except:
    import traceback
    print traceback.format_exc()


'''

url = 'http://127.0.0.1:8000/basic_info/get_car_brand_byLetter'
r = requests.get(url)
print r.text

'''


