def test_file_read():
    file_path = "carSale.csv"
    with open(file_path, "r") as file:
        print(file.readlines())

test_file_read()
