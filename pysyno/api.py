
from .base import ApiCaller, BaseApi
from .audiostation import AudioStation


class Info(ApiCaller):
    def __init__(self, parent):
        super(Info, self).__init__()
        self.parent = parent
        self.host = self.parent.host
        self.verify_ssl = self.parent.verify_ssl
        self.apiname = 'SYNO.API.Info'
        self.path = 'query.cgi'
        self.version = 1

    def query(self, query='ALL'):
        """Retrieves API description objects.

        :param query: The query type
        :type query: str
        :return: Request result
        :rtype: dict
        """
        params = {
            'query': query
        }
        return self.request('query', **params)


class Auth(BaseApi):
    def __init__(self, parent):
        super(Auth, self).__init__(apiname='SYNO.API.Auth', parent=parent)

    def login(self, account, passwd, session, format='cookie'):
        """Logs the specified user in for the specified session.

        :param account: User account
        :type account: str
        :param passwd: User password
        :type passwd: str
        :param session: Session type
        :type session: str
        :param format: Session format
        :type format: str
        :return: Request result
        :rtype: dict
        """
        params = {
            'account': account,
            'passwd': passwd,
            'session': session,
            'format': format
        }
        return self.request('login', **params)

    def logout(self, session: str):
        """Disables the specified session and logs the corresponding user out.

        :param session: The active session to disable
        :type session: str
        :return: Request result
        :rtype: dict
        """
        params = {
            'session': session
        }
        return self.request('logout', **params)


class API:
    def __init__(self, parent):
        self.parent = parent
        self.host = self.parent.host
        self.verify_ssl = self.parent.verify_ssl
        self.Info = Info(self)
        self.parent.apis = self.Info.query(query='ALL')
        self.Auth = Auth(self)


class SynoAPI:
    def __init__(self, host, verify_ssl=False):
        self.host = host
        self.verify_ssl = verify_ssl

        # Let us add all available APIs
        self.Api = API(self)
        self.AudioStation = AudioStation(self)
