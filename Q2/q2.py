import random
import csv
import matplotlib.pyplot as plt

def main():
    
    file_name = 'practice.csv'

    with open(file_name,'w', newline='') as f1:
    
        wr = csv.writer(f1)

        for i in range(100000):
            a = random.randrange(1,7)
            b = random.randrange(1,7)
            c = random.randrange(1,7)
            d = random.randrange(1,7)
            if(0<=i & i<100):
                wr.writerow(str(a)+str(b)+str(c)+str(d))
            if(100<=i & i<1000):
                wr.writerow(str(a)+str(b)+str(c))
            if(1000<=i & i<10000):
                wr.writerow(str(a)+str(b))
            if(10000<=i & i<100000):
                wr.writerow(str(a))
                    
    f1.close()

    f2 = open('practice.csv')
    data = csv.reader(f2)

    roll1 = []
    roll2 = []
    roll3 = []
    roll4 = []

    for row in data:
        if len(row) == 4:
            roll1.append(row[0])
            roll2.append(row[1])
            roll3.append(row[2])
            roll4.append(row[3])
        if len(row) == 3:
            roll1.append(row[0])
            roll2.append(row[1])
            roll3.append(row[2])
        if len(row) == 2:
            roll1.append(row[0])
            roll2.append(row[1])
        if len(row) == 1:
            roll1.append(row[0])
        
    f2.close()
        
    roll1.sort()
    roll2.sort()
    roll3.sort()
    roll4.sort()
    
    plt.subplot(2,2,1)
    plt.hist(roll1, bins=range(0, 7), align='left', rwidth=0.5)
    plt.xlabel('dice value')
    plt.ylabel('time')
    plt.title('roll 100,000')
    plt.xticks(range(0, 7))

    
    plt.subplot(2,2,2)
    plt.hist(roll2, bins=range(0, 7), align='left', rwidth=0.5)
    plt.xlabel('dice value')
    plt.ylabel('time')
    plt.title('roll 10,000')
    plt.xticks(range(0, 7))

        
    plt.subplot(2,2,3)
    plt.hist(roll3, bins=range(0, 7), align='left', rwidth=0.5)
    plt.xlabel('dice value')
    plt.ylabel('time')
    plt.title('roll 1,000')
    plt.xticks(range(0, 7))
   

    plt.subplot(2,2,4)
    plt.hist(roll4, bins=range(0, 7), align='left', rwidth=0.5)
    plt.xlabel('dice value')
    plt.ylabel('time')
    plt.title('roll 100')
    plt.xticks(range(0, 7))
    
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    
    plt.show()
    
if __name__ == '__main__':
    main()
    
