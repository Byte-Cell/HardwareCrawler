import platform
import psutil

def print_system_info():
    # Basic system information
    print("--- System Information ---")
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Node: {platform.node()}")
    print(f"Processor: {platform.processor()}")

    # CPU information
    print("\n--- CPU Information ---")
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores: {psutil.cpu_count(logical=True)}")
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    print(f"CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")   

    # Memory information
    print("\n--- Memory Information ---") 
    svmem = psutil.virtual_memory()
    print(f"Total: {svmem.total / (1024 ** 3):.2f} GB")
    print(f"Available: {svmem.available / (1024 ** 3):.2f} GB")
    print(f"Used: {svmem.used / (1024 ** 3):.2f} GB")
    print(f"Percentage: {svmem.percent}%")

    # Disk information
    print("\n--- Memory Information ---")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"Device: {partition.device}")
        print(f"Mountpoint: {partition.mountpoint}")
        print(f"File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"Total size: {partition_usage.total / (1024 ** 3):.2f} GB")
        print(f"Used: {partition_usage.used / (1024 ** 3):.2f} GB")
        print(f"Free: {partition_usage.free / (1024 ** 3):.2f} GB")
        print(f"Percentage: {partition_usage.percent}%\n")

    # Network information
    print("\n--- Network Information ---")
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"Interface: {interface_name}")
            if str(address.family) == "AddressFamily.AF_INET":
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == "AddressFamily.AF_PACKET":
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")

if __name__ == "__main__":
    print_system_info()