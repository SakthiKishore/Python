# BEGIN-SCRIPT-BLOCK
# Script-Filter:$Vendor == "Cisco"
# END-SCRIPT-BLOCK

from infoblox_netmri.easy import NetMRIEasy

defaults = {
    "api_url": api_url,
    "http_username": http_username,
    "http_password": http_password,
    "job_id": job_id,
    "device_id": device_id,
    "batch_id": batch_id
}

with NetMRIEasy(**defaults) as halo:

    result = halo.send_command('show version')
    print(result)
