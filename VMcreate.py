#!/usr/bin/env python

import argparse
import atexit
import requests

from com.vmware.vmc.model_client import EsxConfig, ErrorResponse
from com.vmware.vapi.std.errors_client import InvalidRequest
from vmware.vapi.vmc.client import create_vmc_client

from samples.vmc.helpers.vmc_task_helper import wait_for_task


class AddRemoveHosts(object):
    """
    Demonstrates add and remove ESX hosts
    Prerequisites:
        - An organization associated with the calling user.
        - A SDDC in the organization
    """

    def __init__(self):
        self.sddc_id = None
        self.org_id = None
        self.vmc_client = None
        self.refresh_token = None
        self.interval_sec = None

    def options(self):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        parser.add_argument('-r', '--refresh-token',
                            required=True,
                            help='VMware Cloud API refresh token')

        parser.add_argument('-o', '--org-id',
                            required=True,
                            help='Organization identifier.')

        parser.add_argument('-s', '--sddc-id',
                            required=True,
                            help='Sddc Identifier.')

        parser.add_argument('-i', '--interval-sec',
                            default=60,
                            help='Task pulling interval in sec')

        args = parser.parse_args()

        self.refresh_token = args.refresh_token
        self.org_id = args.org_id
        self.sddc_id = args.sddc_id
        self.interval_sec = int(args.interval_sec)

    def setup(self):

        # Login to VMware Cloud on AWS
        session = requests.Session()
        self.vmc_client = create_vmc_client(self.refresh_token, session)
        atexit.register(session.close)

        # Check if the organization exists
        orgs = self.vmc_client.Orgs.list()
        if self.org_id not in [org.id for org in orgs]:
            raise ValueError("Org with ID {} doesn't exist".format(self.org_id))

        # Check if the SDDC exists
        sddcs = self.vmc_client.orgs.Sddcs.list(self.org_id)
        if self.sddc_id not in [sddc.id for sddc in sddcs]:
            raise ValueError("SDDC with ID {} doesn't exist in org {}".
                             format(self.sddc_id, self.org_id))

    def add_host(self):
        print('\n# Example: Add 1 ESX hosts to SDDC {}:'.format(self.sddc_id))
        esx_config = EsxConfig(1)

        try:
            task = self.vmc_client.orgs.sddcs.Esxs.create(org=self.org_id,
                                                          sddc=self.sddc_id,
                                                          esx_config=esx_config)
        except InvalidRequest as e:
            # Convert InvalidRequest to ErrorResponse to get error message
            error_response = e.data.convert_to(ErrorResponse)
            raise Exception(error_response.error_messages)

        wait_for_task(task_client=self.vmc_client.orgs.Tasks,
                      org_id=self.org_id,
                      task_id=task.id,
                      interval_sec=self.interval_sec)

    def remove_host(self):
        print('\n# Example: Remove 1 ESX host from SDDC {}:'.
              format(self.sddc_id))
        esx_config = EsxConfig(1)

        try:
            task = self.vmc_client.orgs.sddcs.Esxs.create(org=self.org_id,
                                                          sddc=self.sddc_id,
                                                          esx_config=esx_config,
                                                          action='remove')
        except InvalidRequest as e:
            # Convert InvalidRequest to ErrorResponse to get error message
            error_response = e.data.convert_to(ErrorResponse)
            raise Exception(error_response.error_messages)

        wait_for_task(task_client=self.vmc_client.orgs.Tasks,
                      org_id=self.org_id,
                      task_id=task.id,
                      interval_sec=self.interval_sec)


def main():
    esx_operations = AddRemoveHosts()
    esx_operations.options()
    esx_operations.setup()
    esx_operations.add_host()
    esx_operations.remove_host()


if __name__ == '__main__':
    main()
