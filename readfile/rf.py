import csv

def read_csv_file(file_name):
    try:
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    file_name = "2010picid.png"  # Replace with the name of your CSV file
    read_csv_file(file_name)
