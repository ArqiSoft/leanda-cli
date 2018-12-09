# _*_ encoding: utf-8 _*_

from parser_helper import HandlerBase
from endpoint_helper import EndPoint
from config import ME_URL


class Login(HandlerBase):
    """
    Allows to login and store the login info for an OSDR user.
    Command: login
    osdr login {username} {password}
    """
    url = 'https://api.dataledger.io/osdr/v1/api/me'
    info = '''
            name: login
            help: >
                  Allows to login and reset
                  sesion information for an OSDR user.
            params:
                -
                    names:
                        - -u
                        - --username
                    required: True
                    help: Your OSDR username
                -
                    names:
                        - -p
                        - --password
                    action: +Password
                    nargs: '?'
                    required: True
                    help: OSDR password
                -
                    names:
                        - -v
                        - --verbosity
                    default: 0
                    action: count
                    help: Set verbosity level
    '''

    def __call__(self):
        # super().__call__()
        ep = EndPoint()
        credentials = {'username': self.username, 'password': self.password, }
        session = ep.authorize_remote(credentials)
        # print(session)

        messages = []
        if self.verbosity >= 0:
            message = 'Logged in successfully with username "{username}"'
            messages.append(message)
        if self.verbosity > 1:
            message = 'User\'s OSDR root folder "{owner}"'
            messages.append(message)
            message = 'User\'s current working directory "{cwd}"'
            messages.append(message)
        if self.verbosity > 2:
            message = 'Token: {token}'
            messages.append(message)
        for message in messages:
            print(message.format(**session))


class Logout(HandlerBase):
    """
    Remove persisten storage file
    Command: logout
    osdr login {username} {password}
    """
    info = '''
            name: logout
            help: Do logout. Session data is removed.
    '''

    def __call__(self):
        # super().__call__()

        ep = EndPoint()
        ep.remove_storage()
        print('Successful logout')


class WhoAmI(HandlerBase):
    """
    osdr whoami
    """
    info = '''
            name: whoami
            help: >
                    Check athorization and explore session data.
            params:
                -
                    names:
                        - -v
                        - --verbosity
                    default: 0
                    action: count
                    help: Set verbosity level
    '''

    def __call__(self):
        # super().__call__()
        ep = EndPoint()
        ep.connect()
        resp = ep.get(url=ME_URL)
        try:
            print("Login name: {loginName}".format(**resp.json()))
        except Exception as e:
            print(e)
        messages = []
        if self.verbosity > 0:
            message = 'Logged in OSDR user "{displayName}"'
            messages.append(message)
        if self.verbosity > 1:
            message = 'OSDR user id "{id}"'
            messages.append(message)
        for message in messages:
            print(message.format(**resp.json()))
