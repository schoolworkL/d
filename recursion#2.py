def sorter(data):
    for i in range(len(data) - 1, 0, -1):
        value = 0
        # counter = i - 1
        for j in range(1, i + 1):
            if data[j][1] > data[value][1]:  # change > to <>> to reverse sorting order
                value = j
        data[i], data[value] = data[value], data[i]
    return data


def read_in():
    with open("C:\\Users\\walkerl407\\PycharmProjects\\pythonProject3\\venv\\data") as f:
        data = f.read().splitlines()
        data = [i.split() for i in data]
        return data


class Friend:
    global info
    
    def binary_search(self):

info = read_in()
sorter(info)
print(info)
