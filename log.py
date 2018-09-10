from collections import Counter


class Log:

    def __init__(self, file):
        self._file = file
        self.listResult = []
        with open('{i}'.format(i=file), 'r') as file:
            self._logs = [row.strip() for row in file]

    def counter(self, count):
        return Counter(self.listResult).most_common(count)

    def get(self):
        return self._logs

    def search(self, regexp, count=1, code=''):
        self._regexp = regexp
        self._code = code
        self.listResult = []
        if code == '':
            for i in self.get():
                if regexp.findall(i):
                    self.listResult.append(''.join(regexp.findall(i)))
        else:
            for i in self.get():
                if regexp.findall(i) and i.find(code) != -1:
                    self.listResult.append(''.join(regexp.findall(i)))
        return self.counter(count)

    def searchtime(self, regexp):
        self._regexp = regexp
        self.listResult = []
        for i in self.get():
                if regexp.findall(i):
                    self.listResult.append(''.join(regexp.findall(i))[0:2])
        return self.counter(1)
