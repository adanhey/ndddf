# coding = utf-8
import pandas
from base_ability import *


class Interface_job(Base_interface):
    def get_excel_data(self, filepath, sheet_name):
        df = pandas.read_excel(filepath, sheet_name=sheet_name)
        data = df.values
        case = []
        for line in data:
            data = {
                "用例编号": line[0],
                "用例标题": line[1],
                "请求接口类别": line[2],
                "请求地址":line[3],
                "输入数据":line[4],
                "数据格式": line[5],
                "请求方式": line[6],
                "是否需要登录": line[7],
                "期望结果": line[8],
            }
            for key, value in data.items():
                if str(value) == "nan":
                    data['%s' % key] = None
            case.append(case)
        return case


b = Interface_job()
b.get_excel_data("base.xlsx", "Sheet1")
