import xlrd
import math

def percentage(a,b):
    try:
        percentage_calc=a/b
        return percentage_calc*100
    except:
        return 0
def report(location):
    # location=r"C:\Users\whirldata-arun\Desktop\Python training\corona report.xls"
    wb=xlrd.open_workbook(location)
    sheet=wb.sheet_by_index(0)
    print(sheet.cell_value(0, 0))
    row = sheet.nrows
    #print(row)
    #print(sheet.row_values(0))
    final_report={}
    for i in range(sheet.nrows):
        if i in [0,1]:
            pass
        else:
            calc=sheet.row_values(i)
            print(calc)
            country=calc[1]
            total_cases=calc[2]
            new_cases=calc[3]
            population=calc[13]
            print(country,total_cases,new_cases,population)
            overall_perc=percentage(total_cases,population)
            daily_perc=percentage(new_cases,population)
            final_report[country]={'overall_perc': overall_perc, 'daily_perc' : daily_perc}
    return final_report

while True:
    location=input("Enter the file location : ")
    if location == "Exit":
        break
    result = report(location)
    for k, v in result.items():
        print(k, '= Overall %', v['overall_perc'], ': Daily %', v['daily_perc'])









