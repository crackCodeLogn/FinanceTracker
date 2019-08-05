# @author Vivek
# @version 1.0
# @since 30-07-2019
import calendar


class Helper:

    def get_num_total_days(self, year, month):
        return calendar.monthrange(year, month)[1]

    def get_num_days_left_in_month(self, year, month, start_day):
        return self.get_num_total_days(year, month) - start_day + 1
