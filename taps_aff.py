import csv


def open_file():
    try:

        with open('input.csv', mode='r') as content:
            content = csv.DictReader(content)
            data = [row for row in content]

    except FileNotFoundError:
        print("Error: File 'input.csv' not found.")
    except csv.Error as e:
        print(f"Error: CSV parsing failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print(data)

    return data


def process_data(data):
    for row in data:
        temp = int(row['temperature'])
        temp = convert_to_celsius(temp)
        taps = cal_taps(temp)
        row['what_to_wear'] = taps


def convert_to_celsius(temp):
    """
    it is set to 42 because that is the temp that people
    can get brain damage @, so i am assuming that it is
    false data, and it should be converted to degrees
    Celsius
    """
    if temp > 42:
        temp = (temp - 32) * 5.0 / 9.0
    return temp


def cal_taps(temps):
    if temps < 15:
        return "jumper"
    else:
        return "tshirt"


def write_file(data, output_file_path):
    try:

        with open(output_file_path, mode='w', newline='') as output_file:
            fieldnames = ['location', 'temperature', 'what_to_wear']
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)

            writer.writeheader()
            for row in data:
                writer.writerow(row)

    except FileNotFoundError:
        print(f"Error: Output file '{output_file_path}' not found.")
    except csv.Error as e:
        print(f"Error: CSV writing failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


output_file_path = r"output.csv"

data = open_file()
process_data(data)
write_file(data, output_file_path)
