
import BeautifulSoup
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class AnchorView(BrowserView):
    """ Returns all anchors as list of dicts (keys=name|text)"""

    template = ViewPageTemplateFile('document_anchors.pt')

    def __call__(self, *args, **kw):
        return self.template()

    def getAnchors(self):
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
        return result
                                
