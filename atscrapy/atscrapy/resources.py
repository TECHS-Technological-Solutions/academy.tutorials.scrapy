class WebResource:
    url = None

    parameters = {
        'type': 'Users',
        'location': None,
        'language': None
    }

    headers = {

    }

    def __init__(self):
        self.__page = 0
        self.limit_page = 2

    def makeq(self, parameters):
        try:
            qstr = ''.join(['{0}:{1}+'.format(k, parameters.get(k) or v) for k, v in self.parameters.items()])
        except (Exception,) as err:
            raise Exception('Wrong usage of WebResource parameters')
        return qstr

    @property
    def page_limit_reached(self):
        return self.__page > self.limit_page

    def make(self, parameters):
        qstr = self.makeq(parameters)
        self.__page += 1
        return self.url.format(q=qstr, p=self.__page)


class GitHubWebResources(WebResource):
    url = 'https://github.com/search?q={q}&p={p}'
    headers = {

    }
