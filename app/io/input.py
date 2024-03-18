from pandas import read_csv


def input_console():
    """Reads information that the user enters into the console

    Returns:
        str. input from the user
    """
    return input()


def read_file(file_path):
    """Reads the information from the file

    Args:
        file_path (str): path to the file

    Returns:
        str. strings from the file

    Raises:
        FileNotFoundError: if the file cannot be found
    """
    with open(file_path) as file:
        content = file.read()
    return content


def read_file_pandas(file_path):
    """Reads information from the file using pandas

    Args:
        file_path (str): path to the file

    Returns:
        DataFrame. values from strings in the file

    Raises:
        Errors from read_csv
    """
    return read_csv(file_path)
