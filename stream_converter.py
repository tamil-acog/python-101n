

class PreProcessor:
    @staticmethod
    def process(input_file: str) -> str:
        with open(input_file, 'r+') as fp:
            lines = fp.readlines()
            one_line = ' '.join([line.strip() for line in lines])
        with open("temp", 'w') as tmp:
            for i in range(0, len(one_line), 25):
                print(i)
                print(one_line[i:i+25])
                tmp.write(one_line[i:i+25] + '\n')


