# BEGIN-SCRIPT-BLOCK
# Script-Filter: true
# Script-Timeout: 60
# Script-Login: False
# END-SCRIPT-BLOCK

from netmri_easy import NetMRIEasy

defaults = {
    "api_url": api_url,
    "http_username": http_username,
    "http_password": http_password,
    "job_id": job_id,
    "device_id": device_id,
    "batch_id": batch_id
}

# Create NetMRI context manager. It will close session after execution
with NetMRIEasy(**defaults) as easy:
	brokerList = easy.broker('ConfigList')
