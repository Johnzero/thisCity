import time


class Troop:

    def __init__(self, UA):
        self.UA = UA
        # 初始化到首页

    def run(self):
        print("-------执行兵营任务-------")
        self.onTroops()
        # self.offTroops()

    def onTroops(self):
        self.UA.home()
        # 九州
        self.UA.click(980, 1845)
        time.sleep(2)
        self.UA.click(90, 1868)
        time.sleep(4)
        self.UA.d.swipe(902, 1205, 346, 1205, duration=0.1)
        time.sleep(2)
        # 折冲营
        self.UA.click(474, 1261)
        # 训练
        self.UA.click(743, 1557)

        # 返回首页
        self.UA.click(102, 1839)
        self.UA.click(102, 1839)

        # 急救营
        self.UA.click(893, 1461)
        self.UA.click(875, 898)
        self.UA.click(751, 1557)
        self.UA.click(102, 1839)
        self.UA.click(102, 1839)

        # 互助
        self.UA.click(1008, 1367)
        self.UA.click(540, 1580)
        time.sleep(2)
        self.UA.click(872, 432)
        self.UA.click(872, 432)
        self.UA.click(872, 432)
        # 返回首页
        self.UA.click(102, 1845)

    def offTroops(self):
        self.UA.home()
        time.sleep(2)
        self.UA.click(976, 1835)
        self.UA.click(976, 1835)
        time.sleep(2)
        self.UA.click(82, 825)
        self.UA.click(76, 579)
        self.UA.click(417, 556)
        self.UA.click(424, 821)
        self.UA.click(427, 1057)
        self.UA.click(816, 660)
        self.UA.click(822, 919)
        self.UA.click(78, 677)
        self.UA.click(417, 556)
        self.UA.click(424, 821)
        self.UA.click(427, 1057)
        self.UA.click(816, 660)
        self.UA.click(822, 919)
        self.UA.click(76, 792)
        self.UA.click(417, 556)
        self.UA.click(424, 821)
        self.UA.click(427, 1057)
        self.UA.click(816, 660)
        self.UA.click(822, 919)
        self.UA.click(76, 898)
        self.UA.click(417, 556)
        self.UA.click(424, 821)
        self.UA.click(427, 1057)
        self.UA.click(816, 660)
        self.UA.click(822, 919)
