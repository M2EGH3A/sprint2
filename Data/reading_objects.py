from Library.config import Config
import xlrd
# path = r"C:\Users\Administrator\Documents\redbus_pthelp.xlsx"
class ReadExcel:

    def read_test_data(self,sheetname):
        workbook = xlrd.open_workbook(Config.DATA_PATH)
        worksheet = workbook.sheet_by_name(sheetname)
        columns = worksheet.ncols
        print(columns)
        rows = worksheet.get_rows()
        header = next(rows)
        data = []
        for row in rows:
            values = ()
            for j in range(columns):
                values += (row[j].value,)
            data.append(values)
        return data


    def read_locators(self,sheetname):
        workbook = xlrd.open_workbook(Config.DATA_PATH)
        worksheet = workbook.sheet_by_name(sheetname)
        rows = workbook.sheet_by_name(sheetname)
        rows = worksheet.get_rows()
        header = next(rows)
        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value,row[2].value)
        return d

#
# def read_locators():
#     workbook = xlrd.open_workbook(path)
#     worksheet = workbook.sheet_by_name("mongo")
#     rows = worksheet.get_rows()        ##it creates generator obj
#     print(rows)
#     header = next(rows)
#     d = {}
#     for row in rows:
#         ## print(row[0].value,row[1].value,row[2].value)
#         ##dictionary is created to ame use of it whenever required to access the value
#         d[row[0].value] = (row[1].value,row[2].value)
#     return d
#
# # print(read_locators())
# def read_locators(self,sendkeys):
#     workbook = xlrd.open_workbook(Config.DATA_PATH)
#     workbook = workbook.sheet_by_name(sendkeys)
#     row1 = workbook.get_rows()
#     print(row1)
#     header = next(row1)
#     d= {}
#     for row2 in row1:
#         d[row2[0].value] = (row2[1].value,row2[2].value)


