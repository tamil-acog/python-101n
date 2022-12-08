import typer
from typing import Callable

from atk_training_tamil_p1.function_lookup import lookup


app = typer.Typer()


def apply_process_function(process_function: Callable[[str], str], input_file: str, output_file: str = None):
    with open(input_file) as fp, open(output_file, 'w') as op:
        line = fp.readline()
        transformed_line = process_function(line)
        print(transformed_line, file=op)


@app.command()
def process_text(input_file: str, output_file: str = None, opt: str = None):
    if output_file is None:
        output_file = input_file + ".processed"
    if opt is None:
        opt = "upper_case"
    process_func: Callable[[str], str] = lookup(opt)

    apply_process_function(process_func, input_file, output_file)


def main():
    app()
