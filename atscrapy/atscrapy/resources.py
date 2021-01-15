class WebResource:
    url = None

    parameters = None
    headers = None
    parameters_join = None

    def __init__(self, text=""):
        self.__page = 0
        self.limit_page = 2
        self.text = text

    def makeq(self, parameters):
        try:
            qstr = ''.join([self.parameters_join.format(k, parameters.get(k) or v) for k, v in self.parameters.items()])
        except (Exception,) as err:
            raise Exception('Wrong usage of WebResource parameters')
        return qstr + self.text

    @property
    def page_limit_reached(self):
        return self.__page > self.limit_page

    def make(self, parameters):
        qstr = self.makeq(parameters)
        self.__page += 1
        return self.url.format(q=qstr, p=self.__page)


class GitHubWebResources(WebResource):
    url = 'https://github.com/search?q={q}&p={p}'

    parameters = {
        'type': 'Users',
        'location': None,
        'language': None
    }
    parameters_join = '{0}:{1}+'


class GoogleSearchWebResources(WebResource):
    url = 'https://google.com/search?q={q}&p={p}'

    parameters = {
        'site': None
    }
    parameters_join = ':{0} {1}+'
