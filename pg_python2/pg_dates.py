import calendar
from umalqurra.hijri_date import HijriDate
import jdatetime
from datetime import datetime
import re


def split_non_alpha(string_to_split):
    ret_val = []
    arr_spl = re.split('[^a-zA-Z0-9 ]', string_to_split)
    for s in arr_spl:
        ret_val.append(s.strip())
    return ret_val


def middle_east_parsed_date(text_date, kwargs):
    """
    :param text_date:
    :param kwargs: format : %d-%m-%Y for 12-7-1397.
    :return:
    """
    dict_month_numeric = dict((v, k) for k, v in enumerate(calendar.month_name))
    dict_month_abbr_numeric = dict((v, k) for k, v in enumerate(calendar.month_abbr))

    day = -1
    month = -1
    year = -1
    default_format = ["%d","%m","%Y"]
    tsplit = split_non_alpha(text_date)
    if "format" in kwargs:
        format = kwargs["format"]
    else:
        format = default_format
    if len(tsplit) != len(default_format):
        #TODO: likely split characters next to each other 29101394
        return None
    for idx in range(0, len(tsplit)):
        item = tsplit[idx]
        if not isinstance(item, int) and not isinstance(item, float):
            item = item.capitalize().strip()
            if item in dict_month_numeric:
                item = dict_month_numeric[item]
            elif item in dict_month_abbr_numeric:
                item = dict_month_abbr_numeric[item]
        f_value = format[idx]
        if f_value == "%d":
            day = int(item)
        elif f_value == "%m":
            month = int(item)
        elif f_value == "%Y":
            year = int(item)

    if month > 0 and day > 0 and year > 0:
        if year < 1410:
            jd = jdatetime.datetime(year, month, day)
            return jd.togregorian()
        if year < 1500:
            um = HijriDate(year, month, day)
            return datetime(um.year_gr, um.month_gr, um.day_gr)
    return None

def gregorian_parsed_date(text_date):
    return