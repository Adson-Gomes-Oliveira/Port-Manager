import csv


def readcsv(file):
    port_list = []
    with open(file, mode="r", encoding="utf-8-sig") as portos:
        header, *tail = csv.reader(portos, delimiter=";")

        for port in tail:
            port_dict = {}
            for index, head in enumerate(header):
                port_dict[head] = port[index].upper()

            port_list.append(port_dict)

    return port_list


def writecsv(file, header, data):
    with open(file, mode="w", newline="", encoding="utf-8-sig") as portos:
        writer = csv.writer(portos, delimiter=";")
        writer.writerow(header)
        for item in data:
            new_row_list = []
            for value in item.values():
                new_row_list.append(value)
            writer.writerow(new_row_list)
