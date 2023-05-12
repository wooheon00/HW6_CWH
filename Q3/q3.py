import csv
import matplotlib.pyplot as plt

def main():
    f08 = open('Jeju08.csv')
    data08 = csv.reader(f08)
    f12 = open('Jeju12.csv')
    data12 = csv.reader(f12)
    f16 = open('Jeju16.csv')
    data16 = csv.reader(f16)
    f20 = open('Jeju20.csv')
    data20 = csv.reader(f20)

    next(data08)
    next(data08)  
    next(data08)
    next(data12)
    next(data12)
    next(data12)
    next(data16)
    next(data16)
    next(data16)
    next(data20)
    next(data20)
    next(data20)
    
    rate08=[]
    rate12=[]
    rate16=[]
    rate20=[]

    row08 = next(data08)
    row12 = next(data12)
    row16 = next(data16)
    row20 = next(data20)

    for i in range(12):
        rate08.append(round(float(row08[(i*4 + 5)])/float(row08[(i*4 + 2)]), 4))
    for i in range(12):
        rate12.append(round(float(row12[(i*4 + 5)])/float(row12[(i*4 + 2)]), 4))
    for i in range(12):
        rate16.append(round(float(row16[(i*4 + 5)])/float(row16[(i*4 + 2)]), 4))
    for i in range(12):
        rate20.append(round(float(row20[(i*4 + 5)])/float(row20[(i*4 + 2)]), 4))
        
    
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    plt.title("Jeju Female Rate")
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],rate08,'r.',label = '2008')
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],rate12,'b.',label = '2012')
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],rate16,'y.',label = '2016')
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],rate20,'g.',label = '2020')
    plt.plot(range(13)[1:13:1],[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5], 'black')
    plt.xlabel("month")
    plt.ylabel("Female Rate")
    plt.legend()
    plt.show
    
if __name__ == '__main__':
    main()
   