def downloadFile(URL=None):
    import httplib2
    h = httplib2.Http(".cache")
    resp, content = h.request(URL, "GET")
    return content


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    depth = 0
    startDepth = None
    start = False
    input = None
    stop = None
    output = ""

    def handle_starttag(self, tag, attrs):
        self.depth = self.depth + 1

    def handle_endtag(self, tag):
        self.depth = self.depth - 1

    def handle_data(self, data):
        if data == self.stop:
            self.startDepth = None
        if data == self.input:
            self.start = True
            self.startDepth = self.depth - 2
        if self.startDepth is not None and self.depth > self.startDepth:
            self.output += data


for i in range(2, 3000):
    content = downloadFile("http://www.scp-wiki.net/scp-%0.3d" % i).decode()

    html_parser = MyHTMLParser()
    html_parser.input = 'Special Containment Procedures:'
    html_parser.stop = 'Description:'
    html_parser.feed(content)

    with open("input/contain/%0.3d.txt" % i, "w") as outputFile:
        outputFile.write(html_parser.output)

    html_parser = MyHTMLParser()
    html_parser.input = 'Description:'
    html_parser.stop = '« '
    html_parser.feed(content)
    with open("input/description/%0.3d.txt" % i, "w") as outputFile:
        outputFile.write(html_parser.output)
