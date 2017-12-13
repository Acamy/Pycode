fr = open('records.txt', 'r', encoding='utf-8')
lines = fr.readlines()
max = 0;
min = 1494982799;
cnt = 0
for line in lines:
    try:
        items = line.strip().split(',')
        cnt = cnt + 1
        print(str(cnt) + ":" + items[1])
        tmp = int(items[1].strip())
        if tmp > max:
            max = tmp
        if tmp < min:
            min = tmp
    except:
        pass

print(str(min) + "," + str(max))