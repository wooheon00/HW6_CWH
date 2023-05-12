import csv
import matplotlib.pyplot as plt

def main():
    
    Total=[]
    Seoul=[]
    Daejeon=[]
    Busan=[]
    Jeju=[]


    f = open("Total.csv")
    data = csv.reader(f)
    next(data)
    for row in data:
        Total.append(float(row[2]))
    
    f = open("Seoul.csv")
    data = csv.reader(f)
    next(data)
    for row in data:
        Seoul.append(float(row[2]))

    f = open("Daejeon.csv")
    data = csv.reader(f)
    next(data)
    for row in data:
        Daejeon.append(float(row[2]))
    
    f = open("Busan.csv")
    data = csv.reader(f)
    next(data)
    for row in data:
        Busan.append(float(row[2]))
    
    f = open("Jeju.csv")
    data = csv.reader(f)
    next(data)
    for row in data:
        Jeju.append(float(row[2]))


    plt.title('2022 Average month temperature')
    plt.xlabel('month')
    plt.ylabel('average temperature(celsius)')

    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    plt.plot(range(13)[1:],Total,label='Total', color = "black")
    plt.plot(range(13)[1:],Seoul,label='Seoul')
    plt.plot(range(13)[1:],Daejeon,label='Daejeon')
    plt.plot(range(13)[1:],Busan,label='Busan')
    plt.plot(range(13)[1:],Jeju,label='Jeju')
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()