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
















