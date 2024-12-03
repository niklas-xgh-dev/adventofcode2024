import csv

csv_input_path = "./day1/input.csv"

def open_csv_store_data():
    with open(csv_input_path) as r:
        reader = csv.reader(r)
        data = list(reader)
    return data

def create_sorted_single_lists(data):
    x = []
    y = []
    i = 0
    for pair in data:
        x.append(int(data[i][0]))
        y.append(int(data[i][1]))
        i+=1
    sorted_list_x = sorted(x)
    sorted_list_y = sorted(y)
    return sorted_list_x, sorted_list_y

def calculate_distance_between_sorted_lists(sorted_x,sorted_y):
    distance =  0
    for i in range(len(sorted_x)):
        distance += abs(sorted_x[i] - sorted_y[i])
    return distance

def main():
    data = open_csv_store_data()
    sorted_x, sorted_y = create_sorted_single_lists(data)
    distance = calculate_distance_between_sorted_lists(sorted_x, sorted_y)
    print(distance)

if __name__ == "__main__":
    main()
