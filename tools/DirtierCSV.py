import csv
import random

def modify_csv(input_file, output_file, deletion_rate, duplication_rate):
    with open(input_file, 'r', newline='') as csv_in, open(output_file, 'w', newline='') as csv_out:
        reader = csv.reader(csv_in)
        writer = csv.writer(csv_out)
        
        header = next(reader)
        writer.writerow(header)
        
        for row in reader:
            modified_row = []
            for value in row:
                if random.random() > deletion_rate:
                    modified_row.append(value)
                else:
                    modified_row.append('')
            
            if random.random() < duplication_rate:
                writer.writerow(row)
            writer.writerow(modified_row)

input_file = 'FakeName_50K.csv'
output_file = 'dirty' + input_file
deletion_rate = 0.2
duplication_rate = 0.1

modify_csv(input_file, output_file, deletion_rate, duplication_rate)

