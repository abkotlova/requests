from collections import OrderedDict, namedtuple

from pip._vendor import requests

od = OrderedDict ([
    ("apple", 4),
    ("banana", 3),
    ("orange", 2),
    ("pear", 1)
])

response = requests.get ("https://vk.com")