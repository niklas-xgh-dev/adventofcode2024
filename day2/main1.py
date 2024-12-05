
import csv
import pandas as pd

txt_input_path = "./day2/input1.txt"
csv_output_path = "./day2/input1.csv"

def open_txt_store_csv_and_df():
    df = pd.read_csv(txt_input_path, delimiter=' ', header=None, names=range(8))
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.fillna(0)
    df = df.astype('Int64')
    df.to_csv(csv_output_path, index=None)
    return df

def calculate_safety():
    with open(csv_output_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    safe_counter = -1
    for row in data:
        # ladder up case
        if row[1] > row [0]:
            ladder_counter = 1
            for i in range(1,7):
                if row[i+1] > row[i]:
                    ladder_counter+=1
            if ladder_counter == 7:
                safe_counter+=1
                print("ladder up row:")
                print(row)
        # ladder down case
        else:
            ladder_counter = 1
            for i in range(1,7):
                if row[i+1] < row[i]:
                    ladder_counter+=1
            if ladder_counter == 7:
                safe_counter+=1
                print("ladder down row:")
                print(row)
    print(safe_counter)


def calculate_similarity(sorted_x,sorted_y):
    1+1

def main():
    data = open_txt_store_csv_and_df()
    calculate_safety()



if __name__ == "__main__":
    main()