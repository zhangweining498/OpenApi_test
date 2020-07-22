import unittest
from HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner
import readConfig
from common.Log import MyLog
import os

localReadConfig = readConfig.ReadConfig()

class RunTest:
    def __init__(self):
        global log, logger, resultPath, on_off
        log = MyLog.get_log()
        logger =  log.get_logger()
        resultPath = log.get_report_path()
        self.caseListFile = os.path.join(readConfig.proDir,'caselist.txt')
        self.caseFile = os.path.join(readConfig.proDir,'test_case')
        self.caseList = []

    def set_case_list(self):
        '''
        set case list
        :return:
        '''
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith('#'):
                self.caseList.append(data.replace('\n',''))
        fb.close()

    def set_case_suite(self):
        '''
        set case suite
        :return:
        '''
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suit_module = []
        for case in self.caseList:
            case_name = case.split('/')[-1]
            print(case_name + '.py')
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suit_module.append(discover)
        if len(suit_module) > 0:
            for suite in suit_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        try:
            suit = self.set_case_suite()
            if suit is not None:
                logger.info("********TEST START********" + '\n')
                # with open(resultPath,'wb') as fp:
                #     runner = HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                #     runner.run(suit)
                runner = unittest.TextTestRunner()
                runner.run(suit)
            else:
                logger.info('Have no case to test.')
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("*********TEST END*********")
            # fp.close()



if __name__ == '__main__':
    aa = RunTest()
    aa.run()

