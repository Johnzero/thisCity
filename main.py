from app.UA import UA
from app.FindRed import FindRed as RED
from task import *
from app.Book import Book
import time

if __name__ == "__main__":
    """ 主程序的入口 """
    ua = UA(pkg_name="com.chengzhu.zcylt.ewan9")
    ua.clear_app_data()
    # email.Email(ua).run()
    # zou.Zou(ua).run()
    # zou.Zou(ua).run()
    # hongbao.Hongbao(ua).run()
    # sw.Sw(ua).m()

    # while True:
        # account.Account(ua).run()
        # salaries.Salary(ua).run()
        # troop.Troop(ua).run()
        # sw.Sw(ua).run()
    # troop.Troop(ua).run()
    # while True:
    #     RED(ua).run()
    while True:
        account.Account(ua).run()

        # ua.home()
        troop.Troop(ua).run()
        salaries.Salary(ua).run()
        sw.Sw(ua).run()
        email.Email(ua).run()
        zou.Zou(ua).run()
        hongbao.Hongbao(ua).run()
        # troop.Troop(ua).offTroops()
        r = 0
        while r < 10:
            RED(ua).run()
            r = r+1
        Book(ua).run()
        # cut.Cut(ua).run()
        # cutlog.Cutlog(ua).run()

















    # ewsxv48161 1233276 17755182641
    # ewvdh74231 1233276 17725518596
    # cwe548331e 12345678*  135***6229
    # cw185476q3 a123456789
    # a3596900 a123456789 15805601822

    # ewnkc76653 ewnkc76653
    # 13668334203 13668334203
    # 15699299992 jj428515
    # ewtpj32260  123456789
    # 17362141227 zcb1253373433
    # 13007809286 123456


    # cwsr0794zt 123456789
    # ewtiu78043密码We12345678
