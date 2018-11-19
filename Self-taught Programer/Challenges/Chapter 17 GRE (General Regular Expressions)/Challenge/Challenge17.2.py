# come up with a regular expression that matches all the digits in the string
import re

List = "Arizona, 479, 501, 870. California 209, 213, 650"

m = re.findall("\d\d\d", List, re.IGNORECASE)


def __repr__():
    return "{}"


for match in m:
    print(match.__repr__())
