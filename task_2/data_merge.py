import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./formatted_data.csv"

with open(OUTPUT_FILE_PATH, "w", newline="") as output_file:
    writer = csv.writer(output_file)

    writer.writerow(["sales", "date", "region"])

    for file_name in os.listdir(DATA_DIRECTORY):
        with open(f"{DATA_DIRECTORY}/{file_name}", "r", newline="") as input_file:
            reader = csv.reader(input_file)

            row_index = 0
            for input_row in reader:
                if row_index > 0:
                    product = input_row[0]
                    raw_price = input_row[1]
                    quantity = input_row[2]
                    transaction_date = input_row[3]
                    region = input_row[4]

                    if product == "pink morsel":
                        price = float(raw_price[1:])
                        sale = price * int(quantity)
                        writer.writerow([sale, transaction_date, region])

                row_index += 1

print("Done. Created formatted_data.csv")
