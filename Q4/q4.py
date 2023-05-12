import csv
import matplotlib.pyplot as plt

def main():
  
        
    f = open('subway.csv')
    data = csv.reader(f)
    
    next(data)
    next(data)
    
    in_dict = {}
    
    for row in data:
        in_dict[int(row[10])+int(row[12])] = '[' + row[1] + ']  ' +row[3]
        
    in_k = list(in_dict.keys())
    in_k.sort()
    in_k.reverse()
    
    max_in = []
    max_in_station =[]
    
    for i in range(30):
        max_in.append(in_k[i])
        max_in_station.append(in_dict.get(in_k[i]))
    
    f.close()
    
    
    f = open('subway.csv')
    data = csv.reader(f)
    
    next(data)
    next(data)
    
    out_dict = {}
    
    for row in data:
        out_dict[int(row[11])+int(row[13])] = '[' + row[1] + ']  ' +row[3]
        
    out_k = list(out_dict.keys())
    out_k.sort()
    out_k.reverse()
    
    max_out = []
    max_out_station =[]
    
    for i in range(30):
        max_out.append(out_k[i])
        max_out_station.append(out_dict.get(out_k[i]))
    
    f.close()


    f = open('subway.csv')
    data = csv.reader(f)
    
    next(data)
    next(data)
    
    total_dict = {}
    
    for row in data:
        total_dict[int(row[10])+int(row[11])+int(row[12])+int(row[13])] = '[' + row[1] + ']  ' +row[3]
    
    total_k = list(total_dict.keys())
    total_k.sort()
    total_k.reverse()

    max_total = []
    max_total_station =[]
    
    for i in range(30):
        max_total.append(total_k[i])
        max_total_station.append(total_dict.get(total_k[i]))
    
    f.close()

    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.rc('axes', labelsize=10)
    plt.rc('font', family = 'Malgun Gothic', size=15)
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("2023년 3월 출근시간 최대 승차역 Top 30")
    plt.xlabel("지하철 역")
    plt.ylabel("승차 승객 수 (명)")
    plt.bar(max_in_station, max_in)
    plt.xticks(rotation=90)
    plt.show()
    
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.rc('axes', labelsize=10)
    plt.rc('font', family = 'Malgun Gothic', size=15)
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("2023년 3월 출근시간 최대 하차역 Top 30")
    plt.xlabel("지하철 역")
    plt.ylabel("하차 승객 수 (명)")
    plt.bar(max_out_station, max_out)
    plt.xticks(rotation=90)
    plt.show()

    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.rc('axes', labelsize=10)
    plt.rc('font', family = 'Malgun Gothic', size=15)
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("2023년 3월 출근시간 최대 승하차역 Top 30")
    plt.xlabel("지하철 역")
    plt.ylabel("승하차 승객 수 (명)")
    plt.bar(max_total_station, max_total)
    plt.xticks(rotation=90)
    plt.show()
    
if __name__ == '__main__':
    main()

