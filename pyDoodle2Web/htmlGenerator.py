from .components.html.html import HTML
from .components.container.container import Container
from .components.navbar.navbar import Navbar
from .components.card.card import Card
from .components.row.row import Row
from .components.coloumn.coloumn import Coloumn
from .components.jumbotron.jumbotron import Jumbotron
from .components.carousel.carousel import Carousel
from .components.image.image import Image
from .components.text.text import Text
import os
from math import floor


class HTMLGenerator:
    def __init__(self, tagsList = [], darkMode=False):
        self.html = HTML(darkMode=darkMode)
        self.elementDict = {
            'container': lambda **kw: Container(**kw),
            'navbar': lambda **kw: Navbar(**kw),
            'card': lambda **kw: Card(**kw),
            'row': lambda **kw: Row(**kw),
            'coloumn': lambda **kw: Coloumn(**kw),
            'jumbotron': lambda **kw: Jumbotron(**kw),
            'carousel': lambda **kw: Carousel(**kw),
            'image': lambda **kw: Image(**kw),
            'text': lambda **kw: Text(**kw)
        }
        self.darkModeTags = ['navbar', 'card']
        self.darkMode = darkMode
        self.tagsList = tagsList

    def generateHTML(self, parent = None,  tagName: str = 'html', index=0):
        parent = self.html if not parent else parent
        i = index
        while i < len(self.tagsList):
            elementTag = self.tagsList[i]
            element = self.elementDict.get(elementTag, Container)
            element = element(darkMode=self.darkMode) if elementTag in self.darkModeTags else element()

            if elementTag == 'coloumn':
                col_count = 0
                for j in range(index, len(self.tagsList)):
                    if self.tagsList[j] == 'coloumn':
                        col_count += 1
                    if self.tagsList[j] != 'coloumn':
                        break
                for coloumnNumber in range(col_count):
                    elementTag = self.tagsList[i]
                    element = self.elementDict.get(elementTag, Container)(
                        cols=floor(12/col_count))
                    currentColChildIndex = index + col_count + coloumnNumber
                    appendedElement, new_i = self.generateHTML(
                        element, elementTag, currentColChildIndex)
                    parent.appendElement(appendedElement.template)
                i = i + new_i + 1
                continue

            if elementTag == 'coloumn-end' or elementTag == 'row-end':
                return (parent, i)

            if elementTag == f'{tagName}-end':
                return (parent, i)

            if element.isParentLike:
                appendedElement, new_i = self.generateHTML(element, elementTag, i+1)
                parent.appendElement(appendedElement.template)
                i = new_i
                pass

            else:
                parent.appendElement(element.template)

            if parent.name == 'coloumn':
                return (parent, i)

            i = i + 1

        return (parent, i)
