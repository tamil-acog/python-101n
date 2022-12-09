import typer
from typing import Callable
import yaml

from atk_training_tamil_p1.function_lookup import lookup


app = typer.Typer()


def apply_process_function(input_file: str, output_file: str = None) -> None:
    with open(input_file, 'r') as fp, open(output_file, 'w') as op:
        lines = [line.rstrip() for line in fp]
        for line in lines:
            transformed_line = yaml_config(line)
            print(transformed_line, file=op)


def yaml_config(line: str) -> str:
    processed_line: str = None
    with open("config.yml", 'r') as lines:
        tasks = yaml.safe_load(lines)
    for i in range(len(tasks['tasks'])):
        process_fun: Callable[[str], str] = lookup(tasks['tasks'][i])
        if i == 0:
            processed_line = process_fun(line)
        else:
            processed_line = process_fun(processed_line)
    return processed_line


@app.command()
def process_text(input_file: str, output_file: str = None) -> None:
    if output_file is None:
        output_file = input_file + ".processed"

    apply_process_function(input_file, output_file)


def main():
    app()
