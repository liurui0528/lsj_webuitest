import unittest

from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page_login import PageLogin
from page.page_order import PageOrder
log=GetLogger.get_logger()


class TestOrder(unittest.TestCase):
    def setUp(self):
        # 实例化driver
        self.drver=GetDriver.get_driver()
        # 订单实例化
        self.order = PageOrder(self.drver)
        # 调用登录依赖
        PageLogin(self.drver).page_login_success()
        # 回到首页
        self.order.base_index()

    def tearDown(self):

        # 关闭浏览器
        self.drver.quit()

    # 调用组合业务方法，并断言
    def test_order(self):

        self.order.page_order()
        msg = self.order.page_get_sumbit_result()
        print(msg)
        try:
            self.assertIn('提交成功',msg)
            print('订单提交成功')

        except Exception as e:

            log.error('错误内容为{}'.format(e))

            self.order.base_get_image()
