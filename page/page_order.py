import page
from base.base import Base



class PageOrder(Base):

    # 点击首页
    def page_click_index(self):
        self.base_index()
    # 点击我的购物车

    def page_click_my_cart(self):
        self.base_click(page.order_my_cart)
    # 点击复选框

    def page_click_all_select(self):

        #  判断当前元素是否被选中
        if not self.base_find(page.order_all).is_selected():
            self.base_click(page.order_all)
    # 点击结算

    def page_click_account(self):
        self.base_click(page.order_account)

    def page_find_person(self):
        self.base_find(page.order_person)

    # 提交订单
    def page_click_submit_order(self):
        self.base_click(page.order_submit)
    # 获取预期结果

    def page_get_sumbit_result(self):
        return self.base_get_text(page.order_submit_result)

    # 组装业务方法
    def page_order(self):
        self.page_click_my_cart()
        self.page_click_all_select()
        self.page_click_account()
        self.page_find_person()
        self.page_click_submit_order()


