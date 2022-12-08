
from typing import Callable
from atk_training_tamil_p1.text_processor import transform_to_upper, transform_remove_words, transform_to_lower

function_list: dict = {"upper_case": transform_to_upper, "remove_stop_words": transform_remove_words,
                       'lower_case': transform_to_lower}


def lookup(opt: str) -> Callable[[str], str]:
    return function_list[opt]



