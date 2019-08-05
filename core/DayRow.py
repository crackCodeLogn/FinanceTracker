# @author Vivek
# @version 1.0
# @since 05-08-2019


class Row:
    def __init__(self, base, roi, date, constant, days_completed, hide_base_if_month_more_1):
        self.base = base
        self.roi = roi
        self.date_display = date.strftime('%d-%m-%Y')  # 'dd-MM-yyyy' format
        self.constant = constant
        self.days_completed = days_completed
        self.exponent = 4 * days_completed / 365

        self.multiplier = pow(constant, self.exponent)
        self.amount = base * self.multiplier
        self.interest = self.amount - base

        self.marker = date.strftime('%m-%Y')  # for grouping

    def get_amount_accumulated(self):
        return self.amount

    def get_interest_earned(self):
        return self.interest

    def __repr__(self):
        return "{days_covered}. {date} {mark} {base} : {roi} : {multiplier} => {int} :: {amount}".format(
            days_covered=self.days_completed,
            date=self.date_display,
            mark=self.marker,
            base=self.base,
            roi=self.roi,
            multiplier=self.multiplier,
            int=self.interest,
            amount=self.amount
        )
