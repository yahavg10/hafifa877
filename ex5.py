import pickle

def save_data(file_name, data_list):
    with open(file_name, 'wb') as f:
        pickle.dump(data_list, f)


def load_data(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)


save_data(r'c:\data_file.txt', [1, 2, 3, 'string', True, False, 3.14159])
my_list = load_data(r'c:\data_file.txt')