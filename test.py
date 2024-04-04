import os

from taps_aff import open_file, convert_to_celsius, cal_taps, write_file


def test_open_file():
    data = open_file()
    # test if the variable data is a list
    assert isinstance(data, list)
    # test if there is content in the data variable.
    # this tells us that the file has open and there is content in it
    assert len(data) > 0


def test_convert_to_celsius():
    assert convert_to_celsius(100) == 37.77777777777778

    assert convert_to_celsius(30) == 30


def test_cal_taps():
    assert cal_taps(10) == "jumper"

    assert cal_taps(20) == "tshirt"


def test_write_file(tmp_path):
    # Call write_file function with the path to the temporary directory
    output_file_path = os.path.join(tmp_path, 'output.csv')
    write_file([], output_file_path)  # Pass an empty list for test data

    # Check if the output file is created
    assert os.path.exists(output_file_path)
