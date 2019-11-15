# BEGIN-SCRIPT-BLOCK
# Script-Filter:
#   $Vendor eq "Cisco"
# Script-Timeout: 60
# END-SCRIPT-BLOCK

from infoblox_netmri.easy import NetMRIEasy
#import logging
#import logging.config
#import http.client as http_client

#from infoblox_netmri.client import InfobloxNetMRI


defaults = {
    "api_url": api_url,
    "http_username": http_username,
    "http_password": http_password,
    "job_id": job_id,
    "device_id": device_id,
    "batch_id": batch_id
}
easy = NetMRIEasy(**defaults)
issue_columns = { "name": "test", "host" : "some-host" }
easy.generate_issue(severity="Error", issue_type_id="IOSSSHSettingsFail", **issue_columns)
