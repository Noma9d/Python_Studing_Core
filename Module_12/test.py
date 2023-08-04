import pickle


some_data = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}

file_name = 'data.bin'

def read_records_from_file(self, filename:str):
        try:
            with open(filename, "rb") as file:
                content = pickle.load(file)
                self.data.update(content)
        except FileNotFoundError:
            print('File with phone book not find')

read_records_from_file(file_name)