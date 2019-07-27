# @author Vivek
# @version 1.0
# @since 27-07-2019

from DepositRow import Row
from HtmlGenerator import HtmlGenerator


# https://www.onemint.com/2012/investments/how-to-calculate-interest-on-recurring-deposits/

class DepositInterestCalc:

    def __init__(self, monthly_installment, roi_annual, months):
        self.monthly_inst = monthly_installment
        self.roi = roi_annual / 100.0
        self.months = months

        self.compounding_freq = 4

        self.headers = ["MONTH", "DEPOSIT", "RATE (% p.a.)", "MULTIPLIER", "INTEREST", "TOTAL AMOUNT"]

    def trigger_rd_calc(self):
        constant_part = (1 + self.roi / self.compounding_freq)

        rd_list = []
        for month in range(1, self.months + 1, 1):
            rd_list.append(Row(self.monthly_inst,
                               self.roi,
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

        fd_list = []
        for month in range(1, self.months + 1, 1):
            fd_list.append(Row(self.monthly_inst,
                               self.roi,
                               constant_part,
                               month,
                               self.compounding_freq * month / 12,
                               True))

        total_interest = 0.0
        maturity = 0.0
        for fd in fd_list:
            print(fd)
            total_interest = fd.get_interest_earned()
            maturity = fd.get_amount_accumulated()

        total_interest = round(total_interest, 2)
        maturity = round(maturity, 2)
        HtmlGenerator("FD_" + str(self.monthly_inst)).generate_html(self.headers, fd_list, self.monthly_inst,
                                                                    total_interest, maturity)


if __name__ == '__main__':
    rd = DepositInterestCalc(60000, 7.25, 12)
    rd.trigger_rd_calc()

    fd = DepositInterestCalc(150000, 7.25, 22)
    fd.trigger_fd_calc()
