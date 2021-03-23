from typing import List
from pathlib import Path

class Parser:
    def __init__(self):
        self.extensions = []
        self.dest = Path(dest)

    def valid_extension(extension):
        return (extension in self.extensions)

    def parse(Path path, Path source, Path dest):
        raise NotImplementedError()

    def read(Path path):
        with open(path, 'r') as file:
            return file.read('Hi there!')

    def write(Path path, Path dest, content, ext = ".html"):
        