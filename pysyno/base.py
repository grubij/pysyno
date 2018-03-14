
import requests
import json


class ApiCaller:
    def __init__(self):
        self.host = None
        self.path = None
        self.apiname = None
        self.version = None

    def _build_url(self, method: str, **params) -> str:
        """Builds a full API url based on provided arguments.

        :param method: API method name
        :type method: str
        :param params: API parameters as key-value pairs
        :type params: dict
        :return: Full API URL
        :rtype: str
        """
        # Build URL component by component
        url = '/'.join([self.host, 'webapi', self.path])
        comp_api = '='.join(['?api', self.apiname])
        url = '&'.join([url, comp_api])
        comp_version = '='.join(['version', str(self.version)])
        url = '&'.join([url, comp_version])
        comp_method = '='.join(['method', method])
        url = '&'.join([url, comp_method])

        # Combine all components and then append them to the
        comp_params = ['='.join([key, value]) for key, value in params.items()]
        url = [url]
        url.extend(comp_params)
        url = '&'.join(url)

        return url

    def request(self, method: str, verify=False, **params: str) -> dict:
        url = self._build_url(method, **params)
        result = requests.get(url, verify=verify)
        return json.loads(result.text)


class BaseApi(ApiCaller):
    def __init__(self, apiname, parent):
        super(BaseApi, self).__init__()
        self.parent = parent
        self.host = self.parent.host
        self.verify_ssl = self.parent.verify_ssl
        self.apiname = apiname
        self.api = self.parent.parent.apis['data'][self.apiname]
        self.path = self.api['path']
        self.version = self.api['maxVersion']