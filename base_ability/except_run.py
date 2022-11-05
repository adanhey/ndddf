import datetime
import logging

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)


class Except_run():
    def except_code(self, result_and_except):
        nowtime = datetime.datetime.now()
        file_handler = logging.FileHandler(filename='%s.log' % nowtime, encoding='UTF-8')
        for res in result_and_except:
            logger.addHandler(file_handler)
            try:
                assert res['except'] == res['result']['status']
            except:
                print("状态码错误")
                logger.info('%s  状态码错误 预期结果：%s 实际结果：%s' % (
                nowtime, result_and_except['except'], result_and_except['result']['status']))
