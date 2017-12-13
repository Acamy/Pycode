import matplotlib.pyplot as plot

if __name__ == '__main__':
    x = [521677, 521580, 521520, 521452, 521433, 521411, 521400]
    y = [58109, 57466, 57059, 56668, 54855, 54822, 53988]

    datasets_X = []
    datasets_Y = []
    fr = open('cars.txt', 'r', encoding='utf-8')
    lines = fr.readlines()
    for line in lines:
        items = line.strip().split(',')
        datasets_X.append(float(items[2].strip()))
        datasets_Y.append(float(items[3].strip()))

    plot.ylabel('X')
    plot.xlabel("Y")
    plot.scatter(x,y,color='green')
    plot.plot(datasets_X, datasets_Y, color='red', marker='.', linestyle='solid')
    plot.title('')
    plot.show()