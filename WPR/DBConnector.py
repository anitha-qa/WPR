import pypyodbc
#global primarydesc
#primarydesc = 'TestDes11'

class DBConnector_test():

    def fetchDepartment(self, TransferDepartmentName):
        try:
            conn = pypyodbc.connect('Driver={SQL Server};'
                              'Server=SQLQA01;'
                              'Database=WPR;'
                              'Trusted_Connection=yes;')

            cursor = conn.cursor()
            #istr= "e2e14865"
            #TransferDepartmentName = istr
            print(TransferDepartmentName)
            #sql_department_query = "select * from [WPR].[dbo].[TransferDepartment] where [TransferDepartmentID]='10083'"
            sql_department_query = "select * from [WPR].[dbo].[TransferDepartment] where [TransferDepartmentName]='"+TransferDepartmentName+"'"
            cursor.execute(sql_department_query)


            sql_query = "select * from [WPR].[dbo].[DailyMetricConfiguration]"
            #cursor.execute(sql_query)

            for row in cursor:
                print(row)
            print(cursor.rowcount)

        except Exception as e:
            print ("Exception Occured :", e)
        return cursor.rowcount

    def fetchSite(self, TransferSiteName):
        try:
            conn = pypyodbc.connect('Driver={SQL Server};'
                              'Server=SQLQA01;'
                              'Database=WPR;'
                              'Trusted_Connection=yes;')

            cursor = conn.cursor()
            print(TransferSiteName)

            sql_department_query = "select * from [WPR].[dbo].[TransferSite] where [TransferSiteName]='"+TransferSiteName+"'"
            cursor.execute(sql_department_query)

            for row in cursor:
                print(row)
            print(cursor.rowcount)

        except Exception as e:
            print ("Exception Occured :", e)
        return cursor.rowcount

    def fetchVendorAccountNumber(self, accountNumber):
        try:
            conn = pypyodbc.connect('Driver={SQL Server};'
                              'Server=SQLQA01;'
                              'Database=WPR;'
                              'Trusted_Connection=yes;')

            cursor = conn.cursor()
            print("DB accNum : "+accountNumber)

            sql_venAcc_query = "select * FROM [WPR].[dbo].[PurchasingVendorAccount] where AccountNumber='"+accountNumber+"'"
            cursor.execute(sql_venAcc_query)

            for row in cursor:
                print(row)
            print(cursor.rowcount)

        except Exception as e:
            print ("Exception Occured :", e)
        return cursor.rowcount