
def transform_to_upper(record: str):
    return record.upper()


def transform_remove_words(record:str):
    words = record.split()
    stop_words = ["a", "an", "and", "the", "or"]
    remaining_words = [word for word in words if word not in stop_words]
    return " ".join(remaining_words)




