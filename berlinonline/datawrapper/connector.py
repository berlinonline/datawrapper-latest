import os
import re

import requests


class Connector(object):
    base_url: str

    def __init__(self, base_url: str='https://datawrapper.dwcdn.net'):

        self.base_url = base_url

    def latest_version(self, chart_id: str) -> str:
        """Figure out the latest version of a Datawrapper chart.

        Args:
            chart_id (str): the chart id, such as 'gaYjb'

        Returns:
            str: the latest version, such as https://datawrapper.dwcdn.net/gaYjb/4/
        """
        chart_url = os.path.join(self.base_url, chart_id)
        # We have to get the response of the from the URL {BASE_URL}/{CHART_ID}/, such as
        # https://datawrapper.dwcdn.net/gaYjb/.
        # It should contain a JS-redirect to the latest version of the chart, such as
        # <script>window.location.href='https://datawrapper.dwcdn.net/gaYjb/4/'+window.location.search;</script>
        # We get the chart version from there.
        # If only they didn't use JS-redirects or had a proper API for getting the latest version.
        js_page = requests.get(chart_url)
        p = re.compile(f'{chart_url}/([0-9]+)/')
        result = re.search(p, js_page.text)
        version = result.group()
        return version
    
    def data_url(self, chart_id: str) -> str:
        """Build the URL for the latest version of the CSV-data of a
        Datawrapper chart.

        Args:
            chart_id (str): the chart id, such as 'gaYjb'

        Returns:
            str: the URL of the CSV-file, such as https://datawrapper.dwcdn.net/gaYjb/4/dataset.csv
        """
        latest_chart_url = self.latest_version(chart_id)
        data_url = os.path.join(latest_chart_url, 'dataset.csv')
        return data_url
