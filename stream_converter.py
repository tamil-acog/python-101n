

class PreProcessor:
    @staticmethod
    def process(input_file: str) -> str:
        with open(input_file, 'r+') as fp:
            while True:
                line = fp.readline()
                yield line
                if line == '':
                    return



