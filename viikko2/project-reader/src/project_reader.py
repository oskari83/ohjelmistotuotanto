from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        parsed_toml = toml.loads(content)
        name = parsed_toml["tool"]["poetry"]["name"]
        desc = parsed_toml["tool"]["poetry"]["description"]
        dic = parsed_toml["tool"]["poetry"]["dependencies"]
        dic2 = parsed_toml["tool"]["poetry"]["dev-dependencies"]
        depends = []
        devdepends = []
        for key,value in dic.items():
            depends.append(key)
        for key,value in dic2.items():
            devdepends.append(key)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, depends, devdepends)
