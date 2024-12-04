
import csv
import pandas as pd

txt_input_path = "./day2/input1.txt"
csv_output_path = "./day2/input1.csv"

def open_txt_store_csv_and_df():
    with open(txt_input_path, 'r') as file:
        rows = []
        for line in file:
            rows.append(line.strip().split())
        max_cols = max(len(row) for row in rows)

    df = pd.read_csv(txt_input_path, delimiter=' ', header=None, names=range(max_cols))
    df = df.astype('Int64')
    df.to_csv(csv_output_path, index=None)
    return df

def read_csv_data():
    with open(csv_output_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    safe_counter = 0
    previous_element = 0
    for row in data:
        # numbers going up
        if row[1] > row [0]:
            for i in range(len(row)):
                if row[i] != '':
                    print("ladderup")
                    print(element)
        # numbers going down
        #else:

def calculate_similarity(sorted_x,sorted_y):
    1+1

def main():
    data = open_txt_store_csv_and_df()
    read_csv_data()



if __name__ == "__main__":
    main()