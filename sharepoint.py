from shareplum import Site
from requests_ntlm import HttpNtlmAuth
import certifi
import json
import os

config_path = "config.json"

with open(config_path) as config_files:
        config = json.load(config_files)
        config = config['share_point']


USERNAME = config['user']
PASSWORD = config['password']
SHAREPOINT_SITE = config['site']


class SharePoint:
    def auth(self):
        cred = HttpNtlmAuth(USERNAME, PASSWORD)
        self.site = Site(
            SHAREPOINT_SITE,
            auth=cred
        )
        return self.site

    def connect_to_list(self, ls_name):
        self.auth_site = self.auth()

        list_data = self.auth_site.List(list_name=ls_name).GetListItems()

        return list_data
