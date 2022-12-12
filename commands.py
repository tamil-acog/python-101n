import typer
from atk_training_tamil_p1.task_manager import TaskManager
from atk_training_tamil_p1.stream_converter import PreProcessor
app = typer.Typer()


def apply_process_pipeline(input_file: str, output_file: str = None) -> None:
    """This function transforms the input file using the pipeline found in yaml file."""
    my_task_manager = TaskManager("./config.yml")
    PreProcessor.process(input_file)
    with open("./temp", 'r') as fp, open(output_file, 'w') as op:
        lines = [line.rstrip() for line in fp]
        for line in lines:
            transformed_line = my_task_manager.execute_pipeline(line)
            print(transformed_line, file=op)


@app.command()
def process_text(input_file: str, output_file: str = None) -> None:
    if output_file is None:
        output_file = input_file + ".processed"

    apply_process_pipeline(input_file, output_file)


def main():
    app()


if __name__ == "__main__":
    app()
