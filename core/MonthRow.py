# @author Vivek
# @version 1.0
# @since 05-08-2019

from datetime import datetime


class Row:
    def __init__(self, base, roi, date, constant, days_completed, hide_base_if_month_more_1):
        self.base = base
        self.roi = roi
        self.date = date  # 'dd-MM-yyyy format
        self.constant = constant
        self.days_completed = days_completed
        self.exponent = 4 * days_completed / 365

        self.multiplier = pow(constant, self.exponent)
        self.amount = base * self.multiplier
        self.interest = self.amount - base

        dt = datetime.strptime(date, '%d-%m-%Y')
        self.marker = dt.strftime('%m-%Y')  # for grouping

        self.enrich_values(hide_base_if_month_more_1)

    def enrich_values(self, hide_base_if_month_more_1):
        self.base = round(self.base, 2)
        if hide_base_if_month_more_1:
            if self.days_completed > 1: self.base = ""

        self.roi = round(self.roi * 100, 6)
        self.interest = round(self.interest, 2)
        self.amount = round(self.amount, 2)

    def get_amount_accumulated(self):
        return self.amount

    def get_interest_earned(self):
        return self.interest

    def __repr__(self):
        return "{days_covered}. {date} {base} : {roi} : {multiplier} => {int} :: {amount}".format(
            days_covered=self.days_completed,
            date=self.date,
            base=self.base,
            roi=self.roi,
            multiplier=self.multiplier,
            int=self.interest,
            amount=self.amount
        )
