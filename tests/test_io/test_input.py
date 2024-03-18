import pytest
import pandas as pd
from pandas.errors import EmptyDataError
from os.path import exists
from app.io.input import read_file, read_file_pandas


class TestFileReading():
    def test_read_file_non_existent(self):
        with pytest.raises(FileNotFoundError):
            read_file("non_existent_file.txt")

    def test_read_file_content(self):
        with open("../../data/test_file.txt", "w") as f:
            f.write("Test content")
        assert read_file("../../data/test_file.txt") == "Test content"

    def test_read_file_empty(self):
        assert read_file("../../data/empty_file.txt") == ""

    def test_read_file_pandas_non_existent(self):
        with pytest.raises(FileNotFoundError):
            read_file_pandas("non_existent_file.csv")

    def test_read_file_pandas_content(self):
        df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        df.to_csv("../../data/test_file.csv", index=False)
        pd.testing.assert_frame_equal(read_file_pandas("../../data/test_file.csv"), df)

    def test_read_file_pandas_empty(self):
        with pytest.raises(EmptyDataError):
            read_file_pandas("../../data/empty_file.txt")


if __name__ == "__main__":
    pytest.main()
