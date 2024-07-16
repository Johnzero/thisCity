import time


class Account:

    def __init__(self, UA):
        self.UA = UA
        # 初始化到首页
        UA.home()

    def run(self):
        self.UA.click(90, 1868)
        self.UA.click(90, 1868)
        self.UA.click(114, 155)
        self.UA.click(1011, 1831)
        # 退出账号
        self.UA.click(264, 1549)
        # 确定
        self.UA.click(722, 1196)
        # 下拉
        self.UA.click(909, 633)
        time.sleep(1)
        # 滑动
        self.UA.d.swipe(565, 1328, 540, 881, duration=0.2)
        time.sleep(1)
        self.UA.d.swipe(565, 1328, 540, 681, duration=0.2)
        time.sleep(1)
        # 选择账号
        self.UA.click(359, 1311)
        # self.UA.click(264, 1217)
        # 同意
        self.UA.click(126, 892)
        self.UA.click(543, 1023)  # 登录
        time.sleep(5)
        self.UA.click(522, 1443)
        self.UA.click(525, 1593)  # 进入
        time.sleep(5)

        # 事件
        self.UA.click(976, 1833)
        self.UA.click(530, 1608)
        self.UA.click(528, 1497)
        self.UA.click(97, 1848)
        self.UA.click(97, 1848)
        self.UA.click(97, 1848)
        self.UA.click(97, 1848)
        self.UA.click(97, 1848)
        self.UA.click(97, 1848)
        self.UA.click(97, 1848)
        self.UA.click(530, 1608)
