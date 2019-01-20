import xlrd
xls = xlrd.open_workbook('data_out_慢性粒细胞白血病.xls')
sheet = xls.sheets()[0]
row_values = sheet.row_values(0)
col_values=sheet.col_values(0)
for i in range(1,len(col_values)):
    print(col_values[i])
auther_values=sheet.col_values(3)
for j in range(1,len(col_values)):
    print(auther_values[j])
print('python_version')
#col_num=1
#start=1
#end=100
#n=100-1
#list_url=[]
#for x in range(1,5):
#    url=[]
#    col=sheet.col_values(x)
#    for i in range(1,5):
#            url.append(col[i])
#            list_url.append(url)
#print(list_url)