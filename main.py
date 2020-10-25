import pandas as pd
from datetime import date

table = pd.DataFrame()

table["name"] = []
table["project"] = []
table["dates"] = []
table["recur"] = []

table_complete = pd.DataFrame()


class Project:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.parent.add_child(self)

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


def ret_project(str_name, start):
    if start.get_name == str_name:
        return start
    else:
        children = start.get_children()
        for child in children:
            ret = ret_project(str_name, child)
            if ret is not None:
                return ret
        return None


cur_date = date.today()
root = Project("root", None)

func_commands = ["new_task", "new_project", "edit_task"]
disp_commands = ["project", "tags", "day"]
debug_commands = []



def new_task(args):
    print("haha nope")
    print("I restarted at 9 lmao")