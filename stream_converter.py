

class PreProcessor:
    def process(self, input_file: str) -> str:
        with open(input_file, 'r+') as fp, open("temp", 'w') as op:
            lines = fp.readlines()
            temp = self.stream_input(lines)
            return temp

    @staticmethod
    def stream_input(stream: str):
        for lin in stream:
            yield lin


