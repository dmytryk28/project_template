from app.io.input import input_console, read_file, read_file_pandas
from app.io.output import output_to_console, output_to_file, output_to_file_pandas


def main():
    input_data = (input_console() + '\n'
                  + read_file('data/input_file.txt') + '\n'
                  + str(read_file_pandas('data/pandas_input_file.txt')))
    output_to_console(input_data)
    output_to_file('data/output_file.txt', input_data)
    output_to_file_pandas('data/pandas_output_file.txt', input_data.split('\n'))


if __name__ == '__main__':
    main()
