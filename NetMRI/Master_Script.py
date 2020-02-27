from infoblox_netmri.client import InfobloxNetMRI
from getpass import getpass
import requests
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def print_menu():  # Your menu design here
    print(30 * "-", "MENU", 30 * "-")
    print("1. Print Device Group IDs")
    print("2. Print Script IDs")
    print("3. Print Config List IDs")
    print("4. Print Devices in a Device Group")
    print("5. Exit")
    print(66 * "-")
    

def checkauth(base_url, user_name):
    attempts = 3
    url = base_url + "/api/authenticate"
    api_user = user_name
    while api_user == api_user:
        for i in range(3):
            password = ""
            if not password:
                password = getpass("Enter your Infoblox password: ")
            params = {"username": api_user, "password": password}
            test = requests.get(url, params=params, verify=False)
            if test.status_code == 200:
                return password
            else:
                if i < attempts - 1:
                    print("-- Incorrect password, please try again. --")
                    continue
                else:
                    print("\n" + "X " * 30)
                    print("\n    TO MANY PASSWORD ATTEMPTS - EXITING SCRIPT   \n")
                    print("X " * 30 + "\n")
                    exit()


def netmri_defaults(password, user_name, base_url):
    hostname = base_url.split("//")[1]
    defaults = {
        "host": hostname,
        "username": user_name,
        "password": password,
    }

    client = InfobloxNetMRI(
            defaults.get("host"),
            defaults.get("username"),
            defaults.get("password"),
        )
    return client


def valueTrueFalse(userinput):
    yes = {'yes', 'y', 'YES', 'Y'}
    no = {'no', 'n', 'NO', 'N'}
    while True:
        value = input(userinput)
        if value in yes:
            return value
        elif value in no:
            break
        else:
            print("Invalid input, please try again")
            continue

if __name__ == '__main__':
    loop = True
    netmri_pass = ""
    choice = ""
    netmri_base_url = "https://10.192.34.16" # DON'T include a trailing "/", just URL or IP.
    username = "admin"  # Your username
    print_menu()  # Displays menu

    while loop:  # While loop which will keep going until loop = False
        if not choice:
            choice = input("Enter your choice [1-5]: ")
            continue
        if not choice == "5":
            if not netmri_pass:
                netmri_pass = checkauth(netmri_base_url, username)
            else:
                while choice == "1":

                    print("\n\nOption 1 has been selected\n")
                    search_value = input("Enter a search string, or just press enter to get all results: ")

                    dev_broker = netmri_defaults(netmri_pass, username, netmri_base_url).get_broker("DeviceGroup")
                    devices = dev_broker.index()

                    '''
                    Valid values for broker "DeviceGroup" - "index", "show" and "select" are:
                    DeviceGroupID, ParentDeviceGroupID, DeviceGroupDefnID, DeviceGroupStartTime, DeviceGroupEndTime,
                    DeviceGroupChangedCols, DeviceGroupTimestamp, DataSourceID, GroupID, GroupName, Criteria, Rank, SNMPPolling,
                    CLIPolling, SNMPAnalysis, FingerPrint, CCSCollection, VendorDefaultCollection, ConfigPolling, PortScanning,
                    StandardsCompliance, MemberCount, ConfigLocked, PolicyScheduleMode, PerfEnvPollingInd, SPMCollectionInd,
                    NetBIOSScanningInd, ARPCacheRefreshInd, SAMLicensedInd, AdvancedGroupInd, IncludeEndHostsInd
                    '''

                    if search_value:
                        print("\nIf there are any matching values from your search, the will print below.\n")
                        for value in devices:
                            if re.search(search_value, value.GroupName, re.IGNORECASE):
                                print("{}   {}".format(value.GroupName, value.GroupID))

                        search_value = ""
                        choice = ""
                        print_menu()  # Displays menu

                    else:
                        for value in devices:
                            print("{}   {}".format(value.GroupName, value.GroupID))

                        search_value = ""
                        choice = ""
                        print_menu()  # Displays menu

                while choice == "2":

                    print("\n\nOption 2 has been selected\n")
                    search_value = input("Enter a search string, or just press enter to get all results: ")

                    script_broker = netmri_defaults(netmri_pass, username, netmri_base_url).get_broker("Script")
                    scripts = script_broker.index(limit=1000)

                    if search_value:
                        print("\nIf there are any matching values from your search, the will print below.\n")
                        for value in scripts:
                            if re.search(search_value, value.name, re.IGNORECASE):
                                print(value.name, value.id)

                        search_value = ""
                        choice = ""
                        print_menu()  # Displays menu

                    else:
                        for value in scripts:
                            print(value.name, value.id)

                        search_value = ""
                        choice = ""
                        print_menu()  # Displays menu

                while choice == "3":

                    print("\n\nOption 3 has been selected\n")
                    search_value = input("Enter a search string, or just press enter to get all results: ")

                    script_broker = netmri_defaults(netmri_pass, username, netmri_base_url).get_broker("ConfigList")
                    index = script_broker.index(limit=1000)

                    if search_value:
                        print("\nIf there are any matching values from your search, the will print below.\n")
                        for value in index:
                            if re.search(search_value, value.name, re.IGNORECASE):
                                print(value.name, value.id)

                        search_value = ""
                        choice = ""
                        print_menu()  # Displays menu

                    else:
                        for value in index:
                            print(value.name, value.id)

                        search_value = ""
                        choice = ""
                        print_menu()  # Displays menu

                while choice == "4":

                    print("\n\nOption 4 has been selected\n")

                    groupid_known = valueTrueFalse("Do you know the Device Group ID you want to print the info about? (yes/no): ")

                    if groupid_known:
                        devgroup_id = input("\nEnter the Device Group ID you want to print the info for (enter 0 for all devices): ")
                        dev_broker = netmri_defaults(netmri_pass, username, netmri_base_url).get_broker("Device")
                        devices = dev_broker.index(GroupID=devgroup_id)

                        search_value = input("\nEnter a search string, or just press enter to get all results: ")
                        if search_value:
                            print("\nIf there are any matching values from your search, they will print below.\n")
                            for device in devices:
                                if re.search(search_value, device.DeviceName, re.IGNORECASE):
                                    print(f"{device.DeviceName}, {device.DeviceIPDotted}, {device.DeviceID}")

                            search_value = ""
                            choice = ""
                            print_menu()  # Displays menu

                        else:
                            for device in devices:
                                print(f"{device.DeviceName}, {device.DeviceIPDotted}, {device.DeviceID}")

                            search_value = ""
                            choice = ""
                            print_menu()  # Displays menu

                    else:
                        print("\nWithout knowing the Device Group ID, all devices will be pulled.")
                        dev_broker = netmri_defaults(netmri_pass, username, netmri_base_url).get_broker("Device")
                        devices = dev_broker.index(GroupID="0")

                        search_value = input("\nEnter a search string, or just press enter to get all results: ")
                        if search_value:
                            print("\nIf there are any matching values from your search, the will print below.\n")
                            for device in devices:
                                if re.search(search_value, device.DeviceName, re.IGNORECASE):
                                    print(f"{device.DeviceName}, {device.DeviceIPDotted}, {device.DeviceID}")

                            search_value = ""
                            choice = ""
                            print_menu()  # Displays menu

                        else:
                            for device in devices:
                                print(f"{device.DeviceName}, {device.DeviceIPDotted}, {device.DeviceID}")

                            search_value = ""
                            choice = ""
                            print_menu()  # Displays menu


        elif choice == "5":

            print("\n\nOption 5 has been selected")
            print("Now exiting the script\n\n")
            # You can add your code or functions here
            loop = False  # This will make the while loop to end as not value of loop is set to False

        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

            choice = ""
            print_menu()  # Displays menu
