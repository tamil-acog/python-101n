from typing import Callable
from atk_training_tamil_p1.text_processor import transform_to_upper, transform_remove_words

function_list: dict = {"upper_case": transform_to_upper, "remove_stop_words": transform_remove_words}


def lookup(opt: str) -> Callable[[str], str]:
    return function_list[opt]
