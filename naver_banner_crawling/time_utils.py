import datetime

class TimeUtils:

    def get_now_string(self):
        KST = datetime.timezone(datetime.timedelta(hours=9))
        now = datetime.datetime.now(tz=KST)
        today = now.strftime('%Y-%m-%d %H:%M')

        return today

    def get_today_string(self):
        KST = datetime.timezone(datetime.timedelta(hours=9))
        now = datetime.datetime.now(tz=KST)
        today = now.strftime('%Y%m%d_%H%M')

        return today

    def get_timestamp_string(self):
        KST = datetime.timezone(datetime.timedelta(hours=9))
        now = datetime.datetime.now(tz=KST)
        today = now.strftime('%Y%m%d%H%M%S%f')

        return today