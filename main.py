import pandas as pd
from datetime import datetime

table = pd.DataFrame()

table["name"] = []
table["project"] = []
table["date"] = []
table["tags"] = []


table_complete = pd.DataFrame()


class Project:
    name = ""
    parent = None
    children = []

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        if name != "root":
            self.parent.add_child(self)

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


# Debugged, works now
def ret_project(str_name, start):
    if start.get_name() == str_name:
        return start
    else:
        children = start.get_children()
        for child in children:
            ret = ret_project(str_name, child)
            if ret is not None:
                return ret
        return None


def print_projects(start):
    print("Lmaooo you thought this was done")


# cur_date = datetime.date.today()      # Currently broken
root = Project("root", None)

func_commands = ["new_task", "new_project", "edit_task", "complete"]
disp_commands = ["project", "tags", "day", "projects"]
debug_commands = []


# Currently no recurrence
def new_task(args):
    # args is a list, first one is name, second one is project, third one is date, rest are tags
    name = args[0]
    project = ret_project(args[1], root)
    if project is None:
        project = Project(args[1], root)

    date = None
    try:
        date = datetime.strptime(args[2], '%m/%d/%y')
    except ValueError:
        date = None

    tags = None
    if len(args) > 3:
        tags = args[3:]
    task = {"name": name, "project": project, "date": date, "tags": tags}
    return task


table = table.append(new_task(["test1", "proj1", "10/25/20", "tag1", "tag2"]), ignore_index=True)
table = table.append(new_task(["test2", "proj1", "no"]), ignore_index=True)

print(table.head())
