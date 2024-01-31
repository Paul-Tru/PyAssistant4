import psutil
import GPUtil
import logging


def get_sys_info():
    print("CPU Usage: ")
    print(f"    {psutil.cpu_percent(interval=1)}%")

    virtual_mem = psutil.virtual_memory()
    print("\nVirtual Memory:")
    print(f"    Total: {virtual_mem.total / (1024 ** 3):.2f} GB")
    print(f"    Used: {virtual_mem.used / (1024 ** 3):.2f} GB")
    print(f"    Free: {virtual_mem.free / (1024 ** 3):.2f} GB")

    partitions = psutil.disk_partitions()
    for partition in partitions:
        partition_info = psutil.disk_usage(partition.mountpoint)
        print(f"\nDisk Information for {partition.device}:")
        print(f"    Total Disk Space: {partition_info.total / (1024 ** 3):.2f} GB")
        print(f"    Used Disk Space: {partition_info.used / (1024 ** 3):.2f} GB")
        print(f"    Free Disk Space: {partition_info.free / (1024 ** 3):.2f} GB")

    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu = gpus[0]
            print(f"\nGPU: {gpu.name}")
            print(f"  Memory Total: {gpu.memoryTotal / 1024:.2f} GB")
            print(f"  Memory Free: {gpu.memoryFree / 1024:.2f} GB")
            print(f"  Memory Used: {gpu.memoryUsed / 1024:.2f} GB")
            print(f"  GPU Load: {gpu.load * 100:.2f}%")
        else:
            print("\nNo GPU found")
    except Exception as e:
        print(f"Error while trying to get information: {e}")


get_sys_info()
