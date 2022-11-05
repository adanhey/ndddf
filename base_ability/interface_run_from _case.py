import datetime
import json
import logging

from base_ability.change_exl_to_testcase import Interface_job

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)


class Interface_run(Interface_job):
    def run_case(self, exl_filepath, sheet_name="Sheet1"):
        case = self.get_excel_data(exl_filepath, sheet_name)
        nowtime = datetime.datetime.now()
        file_handler = logging.FileHandler(filename='%s.log' % nowtime, encoding='UTF-8')
        case_result = []
        for ca in case:
            logger.addHandler(file_handler)
            nowtime = datetime.datetime.now()
            logger.info('%s   %s' % (nowtime, ca))
            url = '%s%s' % (self.host, ca['请求地址'])
            data = json.loads(ca['输入数据'])
            if str(ca['请求接口类别']) == "get":
                result = self.get_request(url=url, param=data)
                return result
            elif str(ca['请求接口类别']) == "post":
                result = self.post_request(url=url, data=data)
                return result
            else:
                result = self.delete_request(url=url, data=data)
            logger.info('%s   %s' % (nowtime, result.status_code))
            logger.info('%s   %s' % (nowtime, result.text))
            result_and_except = {
                "result": result.json(),
                "except": ca['期望结果']
            }
            case_result.append(result_and_except)
            logger.removeHandler(file_handler)
        return case_result
