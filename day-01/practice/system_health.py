import psutil

def system_health():

    CPU_threshold = int(input("Enter the CPU threshold:"))
    Disk_threshold = int(input("Enter the Disk/RAM threshold:"))
    Memory_threshold = int(input("Enter the Memory threshold:"))

    current_CPU = psutil.cpu_percent(interval=1)
    current_Disk = psutil.disk_usage('/').percent
    current_Memory = psutil.virtual_memory().percent



    print(f"Current CPU % =",current_CPU)
    print(f"Current Disk/RAM % =",current_Disk)
    print(f"Current Memory % =",current_Memory)

    if CPU_threshold > current_CPU:
        print("CPU threshold Alet, Email sent...")

    if Disk_threshold > current_Disk:
        print("Disk/RAM threshold Alet, Email sent...")
    if Memory_threshold > current_Memory:
        print("Memory threshold Alert, Email sent...")

system_health()
