from datetime import datetime


class SafeDatetimeConverter:
    """
    A class to safely converte between strings and datetime
    """

    @staticmethod
    def string_to_datetime(datetime_str):
        """
        A method to convert a string to datetime
        :param datetime_str: a datetime as string
        :return: a datetime object
        """

        try:
            datetime_res = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%f")
        except Exception as e1:
            try:
                datetime_res = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S")
            except:
                raise Exception(f"Error converting this string: {str(datetime_str)} of type {str(type(datetime_str))}")

        return datetime_res
