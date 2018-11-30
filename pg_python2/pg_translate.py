"""
contains various utilities to translate dates
"""
import logging
import pg_dates


class Translate(object):
    region = None
    supported_regions = [
        "middle-east", # generic middle east
        "gregorian"
    ]

    def __init__(self, region):
        self.region = region
        self._test_region()

    def _help(self):
        logging.info("Supported Regions")
        logging.info("-----------------")
        for item in self.supported_regions:
            logging.info(item)

    def _test_region(self):
        if self.region not in self.supported_regions:
            self._help()
            raise Exception('Region not supported')

    def get_datetime(self, text, **kwargs):
        """
        :param text:
        :param kwargs: dictionary that supports "format" as a key and
        value will be as per the language. Format is a list
        :return:
        """
        if self.region == "middle-east":
            return pg_dates.middle_east_parsed_date(text, kwargs)
        if self.region == "gregorian":
            return pg_dates.gregorian_parsed_date(text, kwargs)
        return

if __name__ == "__main__":
    tr = Translate("middle-east")
    td = tr.get_datetime("1397, 8, Dec", format=["%Y", "%m", "%d"])
    print(td)




