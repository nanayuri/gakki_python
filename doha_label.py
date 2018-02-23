import openpyxl
import os

cur_dir = 'D:\\Doha_svg'
file_name = 'M010-MSI-INM-13-ICD - Doha Metro SCADA IO LIST SCD-CIVS (stations_in_1).xlsx'
file_sour = cur_dir + '\\' + file_name
ws_name = '2-Instance List'
col_location = 1
col_sub_loc = 2
col_class_name = 3
col_eqp_name = 4
col_short_name = 5
col_eqp_label = 6
col_unq_id = 8

eqp_list = ['ACS']

wb = openpyxl.load_workbook(file_sour)
ws = wb[ws_name]

for each_rows in ws.rows:
    if not each_rows[col_class_name].value:
        continue
    if each_rows[col_class_name].value in eqp_list:
        print(each_rows[col_unq_id].value + " : " + each_rows[col_eqp_label].value + '\n')



