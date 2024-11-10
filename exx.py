import xlwt
from xlwt import Workbook
wb = Workbook()
sheet1 = wb.add_sheet('sheet 1')
sheet1.write(1,0,'id')
sheet1.write(2,0,'name')
sheet1.write(0,1,'1')
sheet1.write(0,2,'2')
wb.save('C://Users//PC//Desktop//learn//ex.xls')