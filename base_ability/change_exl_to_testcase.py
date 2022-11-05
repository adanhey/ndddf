
# coding = utf-8
import pandas
from base_ability import *

class Interface_job(Base_interface):
    def get_excel_data(self,filepath,sheet_name):
        df = pandas.read_excel(filepath,sheet_name=sheet_name)
        data = df.values
        # print(data[0])
        for line in data:
            c = str(line)
            print(c)
            # c = c.replace('[','')
            # c = c.replace(']','')
            # c = c.replace("'","")
            # linelist = c.split(' ')
            # print(linelist)
                # with open('12222.py','w') as sd:
                #     sd.write(st.range('A%i' % row).value)
                #     sd.close()
b = Interface_job()
b.get_excel_data("base.xlsx","Sheet1")
