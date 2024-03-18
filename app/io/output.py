from pandas import DataFrame


def output_to_console(data):
    """Print data into console

    Args:
        data (Any): the information that will be printed
    """
    print(data)


def output_to_file(file_path, data):
    """Outputs information to the file
    by adding it into the end of the file

    Args:
        file_path (str): path to the file
        data (str): data that will be added to the file

    Raises:
        FileNotFoundError: if the file cannot be found
    """
    with open(file_path, 'w') as file:
        file.write(data)


def output_to_file_pandas(file_path, data):
    """Outputs information to the file using Pandas

    Args:
        file_path (str): path to the file
        data (Any): data that will be added to the file

    Raises:
        Errors from to_csv
    """
    df = DataFrame(data)
    df.to_csv(file_path, mode='a')
