str_p = """
    with open("f") as f:
        f.read
"""


class Bustr(str):
    def __init__(self, s=""):
        str.__init__(s)

    def replace_all(self, dic, count=...):
        text = self
        for i, j in dic.items():
            text = text.replace(i, j, count)
        return text

from auto_pip.util.builtins import BuList
tab = {"\t": "", " " * 4: ""}
mylist = str_p.split("\n")
funk = lambda s: Bustr(s).replace_all(tab, 1)
f = list(map(funk, mylist))
print(*f, sep="\n")
