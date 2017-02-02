import datetime
import logging

LOG = logging.getLogger(__name__)


def _get_today_date():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    week_of_year = now.isocalendar()[1]
    day_of_year = now.timetuple().tm_yday
    return year, month, week_of_year, day_of_year


def set_created_at(doc):
    y, m, woy, doy = _get_today_date()
    doc['created_at'] = {
        "year": y,
        "month": m,
        "week_of_year": woy,
        "day_of_year": doy
    }


class DateScope:
    """Helper class that provides couchdb map conditions for corresponding
    to date scopes."""

    @classmethod
    def this_year(cls):
        y, m, woy, doy = _get_today_date()
        return "doc.created_at.year == {0}".format(y)

    @classmethod
    def this_month(cls):
        y, m, woy, doy = _get_today_date()
        return "doc.created_at.month == {0} && " \
               "doc.created_at.year == {1}".format(m, y)

    @classmethod
    def this_week(cls):
        y, m, woy, doy = _get_today_date()
        return "doc.created_at.week_of_year == {0} && " \
               "doc.created_at.year == {1}".format(woy, y)

    @classmethod
    def today(cls):
        y, m, woy, doy = _get_today_date()
        return "doc.created_at.day_of_year == {0} && " \
               "doc.created_at.year == {1}".format(doy, y)
