# @author Vivek
# @version 1.0
# @since 27-07-2019
# The entry point!
from datetime import datetime
from datetime import timedelta

from core.DayRow import Row as day
from core.DepositRow import Row
from html.HtmlGenerator import HtmlGenerator


# https://www.onemint.com/2012/investments/how-to-calculate-interest-on-recurring-deposits/

class DepositInterestCalc:

    def __init__(self, monthly_installment, roi_annual, start_date, months):
        self.monthly_inst = monthly_installment
        self.roi = roi_annual / 100.0
        self.start_date = start_date
        self.months = months

        self.compounding_freq = 4

        self.headers = ["MONTH", "DEPOSIT", "RATE (% p.a.)", "MULTIPLIER", "INTEREST", "TOTAL AMOUNT"]

    def trigger_rd_calc(self):
        constant_part = (1 + self.roi / self.compounding_freq)
        start_date = '01-01-2019'
        rd_list = []
        for month in range(1, self.months + 1, 1):
            rd_list.append(Row(self.monthly_inst,
                               self.roi,
                               start_date,
                               constant_part,
                               month,
                               self.compounding_freq * month / 12,
                               False))

        total_deposit = 0.0
        total_interest = 0.0
        maturity = 0.0
        for rd in rd_list:
            print(rd)
            total_deposit += rd.base
            total_interest += rd.get_interest_earned()
            maturity += rd.get_amount_accumulated()

        total_deposit = round(total_deposit, 2)
        total_interest = round(total_interest, 2)
        maturity = round(maturity, 2)
        HtmlGenerator("RD_" + str(self.monthly_inst)).generate_html(self.headers, rd_list, total_deposit,
                                                                    total_interest, maturity)

    def trigger_fd_calc(self):
        constant_part = (1 + self.roi / self.compounding_freq)

        fd_days_list = []
        date = datetime.strptime(self.start_date, '%d-%m-%Y')
        for month in range(1, self.months + 1, 1):
            fd_days_list.append(day(self.monthly_inst,
                                    self.roi,
                                    date,
                                    constant_part,
                                    month,
                                    True))
            date = date + timedelta(days=1)

        fd_month_wise_day_list = {}
        for entry in fd_days_list:
            fd_month_wise_day_list[entry.marker] = entry

        for entry in fd_month_wise_day_list:
            month_start_date = ''
            marker = fd_month_wise_day_list[entry].marker
            for inner in fd_days_list:
                if inner.marker == marker:
                    month_start_date = inner.date_display
                    break
            fd_month_wise_day_list[entry].date_display = month_start_date
            print(fd_month_wise_day_list[entry])

        total_interest = 0.0
        maturity = 0.0
        for fd in fd_days_list:
            # print(fd)
            total_interest = fd.get_interest_earned()
            maturity = fd.get_amount_accumulated()

        total_interest = round(total_interest, 2)
        maturity = round(maturity, 2)
        # HtmlGenerator("FD_" + str(self.monthly_inst)).generate_html(self.headers, fd_list, self.monthly_inst,
        #                                                             total_interest, maturity)


if __name__ == '__main__':
    # rd = DepositInterestCalc(60000, 7.25, 12)
    # rd.trigger_rd_calc()

    fd = DepositInterestCalc(150000, 7.25, '05-08-2019', 31)
    fd.trigger_fd_calc()
