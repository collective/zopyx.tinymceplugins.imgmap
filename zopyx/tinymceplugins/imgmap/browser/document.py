
import demjson
import BeautifulSoup
from Products.Five.browser import BrowserView


class AnchorView(BrowserView):
    """ Returns all anchors as JSON data structure """


    def __call__(self):
        """ return all anchors """

        html = self.context.getText()
        result = list()
        soup = BeautifulSoup.BeautifulSoup(html)
        for anchor in soup.findAll('a'):
            try:
                name = anchor['name']
            except KeyError:
                name = None

            if name:
                result.append(dict(name=name, text=name))
        return demjson.encode(result) 
                                
