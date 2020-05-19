import PIL
import pytesseract
import os
from difflib import get_close_matches


class OCR:
    '''
    Uses pytesseract to return a list of tags in the doodle
    '''
    def __init__(self, imagePath: str):
        self.imagePath = imagePath
        self.real_tags = ['container', 'carousel', 'text','row', 'coloumn', 'navbar', 'col', 'image', 'card', 'container-end', 'row-end', 'coloumn-end']

    def formater(self, line: str):
        if line not in ['', ' ']:
            return line

    def builder(self, text: str) -> list:
        main_list = []
        for line in filter(self.formater, text.splitlines()):
            for i in line.strip().split():
                main_list.append(i)
        return main_list

    def fixTags(self, tags: list) -> list:
        '''
        Corrects the output from pytesseract by checking closeness to the allowed tags
        '''
        final_tags = []
        for tag in tags:
            close_match = get_close_matches(tag, self.real_tags, n = 1, cutoff = 0.6)
            if close_match[0] in self.real_tags:
                final_tags.append(close_match[0])
        return final_tags

    def readText(self) -> list:
        try:
            path = self.imagePath
            text = pytesseract.image_to_string(path)
            tags = self.builder(text)
            return self.fixTags(tags)

        except PIL.UnidentifiedImageError:
            print('Could not read the image file, check filetype.')

        except Exception as e:
            print(e)