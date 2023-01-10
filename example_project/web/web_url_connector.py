import requests


def get_code_academy_index():
    return requests.get("https://www.codeacademy.bg")
