import requests

def sum_two_numbers(a, b):
    """
    Should not work with invalid SUM data types.

    :param a: any number type (int, float, Decimal)
    :param b: any number type (int, float, Decimal)
    :return: sum of a & b
    """

    try:
        str_a, str_b = str(a), str(b)
        return int(eval(f"{str_a} + {str_b}"))
    except:
        return


def inner_func():
    pass


def print_something(*args):
    for arg in args:
        print(arg)

    inner_func()


def request_some_site_info(url):
    response = requests.get(url)
    if not response.raise_for_status():
        raise Exception("Server did not return status")

    response_json = response.json()
    if response_json["today_views"] < 1000:
        return response, "Site has too vew daily visits"
    elif 1000 <= response_json["today_views"] < 10000:
        return response, "Site has good amount of daily visits"
    else:
        return response, "Super SITE!!!!!!!!!!!!!"


def request_book_site():
    response = requests.get("http://scrapethisbooks.alabala")
    return response.text
