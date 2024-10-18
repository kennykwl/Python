import wmi
import argparse
from datetime import datetime

def get_last_boot_time(computer_name):
    try:
        connection = wmi.WMI(computer=computer_name)
        for os in connection.Win32_OperatingSystem():
          last_boot = os.LastBootUpTime.split('.')[0]
          boot_time = datetime.strptime(last_boot, '%Y%m%d%H%M%S')
          formatted_time = boot_time.strftime('%Y-%m-%d %H:%M')

          print(f"Computer Name: {os.CSName}")
          print(f"Last Boot Time: {formatted_time}"
    except Exception as e:
          print(f"Failed to connect or retrieve data: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the last boot time of a remote Windows computer.")
    parser.add_argument('--computername', required=True, help="The name of the remote computer")

    args = parser.parse_args()

    get_last_boot_time(args.computername)
          
