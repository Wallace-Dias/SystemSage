import psutil, time

""" psutil.cpu_percent()
psutil.virtual_memory()
psutil.disk_usage('/')
psutil.net_io_counters()
psutil.pids()
psutil.Process(pid)
psutil.process_iter() """

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent
print("="*30)
print(f"Uso da CPU: {cpu} %")
print(f"Uso de RAM: {ram} %")
print(f"Espaço em disco: {disk} %")
print("="*30)
print("\n")

for proc in psutil.process_iter():
    print(proc.name())
    break


if cpu >= 50:
    print("Alerta! CPU em uso excessivo!")
