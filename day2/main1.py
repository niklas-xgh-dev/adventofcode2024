
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
        data = list(reader)[1:]
        
    safe_counter = 0
    for row in data:
        numbers = [int(x) for x in row]
        
        seq_length = 0
        for n in numbers:
            if n == 0:
                break
            seq_length += 1
            
        if seq_length < 2:
            continue
            
        is_increasing = numbers[1] > numbers[0]
        is_safe = True
        
        for i in range(seq_length - 1):
            diff = numbers[i+1] - numbers[i]
            
            if is_increasing and (diff <= 0 or diff > 3):
                is_safe = False
                break
            if not is_increasing and (diff >= 0 or abs(diff) > 3):
                is_safe = False
                break
                
        if is_safe:
            safe_counter += 1
            print(f"{'ladder up' if is_increasing else 'ladder down'} row:")
            print(row[:seq_length])
            
    print(safe_counter)

def main():
    data = open_txt_store_csv_and_df()
    calculate_safety()

if __name__ == "__main__":
    main()