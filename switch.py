import csv


def switch(input_file, output_file):
    mac_dict = {"70:5a:0f:46:30:50": "Eth0", "dc:4a:3e:7e:8f:2b": "Eth1",
                "70:5a:0f:44:3d:77": "Eth2", "dc:4a:3e:7e:90:12": "Eth3", "9c:7b:ef:aa:2c:6b": "Eth4",
                "9c:7b:ef:aa:2b:b7": "Eth5", "ec:b1:d7:5b:a1:b4": "Eth6", "70:5a:0d:4a:cd:c7": "Eth7"}
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open(output_file, 'w', newline='') as new_file:
            csv_writer = csv.writer(new_file)
            for line in csv_reader:
                if line[2] in mac_dict:
                    row_to_write = [mac_dict[line[2]], line[1], line[2]]
                    csv_writer.writerow(row_to_write)
                elif line[2] == "ff:ff:ff:ff:ff:ff":
                    for mac, port in mac_dict.items():
                        if mac == line[1]:
                            continue
                        row_to_write = [port, line[1], mac]
                        csv_writer.writerow(row_to_write)
                else:
                    csv_writer.writerow(line)


if __name__ == '__main__':
    switch('input.csv', 'output.csv')
