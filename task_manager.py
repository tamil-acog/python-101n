from typing import List, Callable

import yaml

from atk_training_tamil_p1.file_loader import FunctionLoader

load = FunctionLoader()


class TaskManager(object):
    def __init__(self, yaml_file: str):
        self.task_list: List[Callable[[str], str]] = TaskManager.parse_yaml(yaml_file)

    def execute_pipeline(self, line: str):
        for task in self.task_list:
            line = task.exec(self, line)
        yield line

    @classmethod
    def parse_yaml(cls, yaml_file):
        with open(yaml_file) as fp:
            yaml_data = yaml.safe_load(fp)
        task_names = yaml_data["pipeline"]
        tasks = []
        for task_name in task_names:
            tasks.append(load.give_function(task_name))
        return tasks
