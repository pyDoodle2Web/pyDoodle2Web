from ocr import OCR
from htmlGenerator import HTMLGenerator


class pyDoodle2Web:
    def __init__(self, path:str, darkMode:bool = True):
        self.path = path
        self.darkMode = True

    def generate(self):
        tags = OCR(self.path).readText()
        html, _ = HTMLGenerator(tagsList=tags, darkMode=self.darkMode).generateHTML()
        return html