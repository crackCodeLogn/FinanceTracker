# @author Vivek
# @version 1.0
# @since 27-07-2019


class Row:
    """
    Formula for computation of the amount for given details for RD:
        amount = base * [1 + roi/4] ^ (4*monthi/12)

    -> 4: compounding frequency -- because RD interest is calc quarterly
    -> monthi: ith month for which the iteration is -- 1<=i<=total_month_RD
    """

    def __init__(self, base, roi, constant, months_completed, exp, hide_base_if_month_more_1):
        self.base = base
        self.roi = roi
        self.constant = constant
        self.months_completed = months_completed
        self.exponent = exp

        self.multiplier = pow(constant, exp)
        self.amount = base * self.multiplier
        self.interest = self.amount - base

        self.enrich_values(hide_base_if_month_more_1)

    def enrich_values(self, hide_base_if_month_more_1):
        self.base = round(self.base, 2)
        if hide_base_if_month_more_1:
            if self.months_completed > 1: self.base = ""

        self.roi = round(self.roi * 100, 6)
        self.interest = round(self.interest, 2)
        self.amount = round(self.amount, 2)

    def get_amount_accumulated(self):
        return self.amount

    def get_interest_earned(self):
        return self.interest

    def __repr__(self):
        return "{month_covered}. {base} : {roi} : {multiplier} => {int} :: {amount}".format(
            month_covered=self.months_completed,
            base=self.base,
            roi=self.roi,
            multiplier=self.multiplier,
            int=self.interest,
            amount=self.amount
        )
