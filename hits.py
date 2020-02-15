f = open("/Users/veraivanova/Downloads/hits.txt", 'r')
f1 = f.readlines()
f.close()
ips = dict()
for line in f1:
    ip = line[line.find("\t")+1]
    i = line.find("\t")+2
    while (line[i].isdigit() or line[i] == '.') and line:
        ip += line[i]
        i += 1
    if ip not in ips.keys():
        ips[ip] = 0
    else:
        ips[ip] += 1
for i in range(5):
    for key, val in ips.items():
        if val == max(ips.values()):
            print(key)
            ips[key] = min(ips.values())
            break


# Ответ:
# 154.157.157.156
# 82.146.232.163
# 194.78.107.33
# 226.247.119.128
# 21.143.243.182
