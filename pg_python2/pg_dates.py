import re


def split_non_alpha(string_to_split):
    ret_val = []
    arr_spl = re.split('[^a-zA-Z0-9 ]', string_to_split)
    for s in arr_spl:
        ret_val.append(s.strip())
    return ret_val


def middle_east_parsed_date(text_date):
    tsplit = split_non_alpha(text_date)
    print(tsplit)
    return

def gregorian_parsed_date(text_date):
    return