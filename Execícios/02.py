import psutil
#01
for proc in psutil.process_iter(['pid'], ['name']):
    try:
        print(proc.info['name'])
    except:
        continue


# 02
for proc in psutil.process_iter(['pid', 'name']):
    try:
        uso = proc.cpu_percent(interval=0.1)
        if uso > 0:
            print(f"{proc.info['name']} está usando {uso}% da CPU")
    except:
        continue

# 03

for proc in psutil.process_iter(['pid'], ['name']):
    try:
        print(proc.memory_info().rss)
    except:
        continue
