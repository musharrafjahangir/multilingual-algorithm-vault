def bubbltSort(data):
    l = len(data)
    for x in range(l):
        for y in range(0,l-x-1):
            if data[y] > data[y+1]:
                temp = data[y]
                data[y] = data[y+1]
                data[y+1] = temp
if __name__ == "__main__":
    n = int(input("Enter number of data: "))
    data = [int(input()) for x in range(n)]
    bubbltSort(data)
    print(data)