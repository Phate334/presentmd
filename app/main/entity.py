from pathlib import Path


class IndexEntity:
    def __init__(self, url: Path):
        self.url = '/present/' + str(url).replace('\\', '/')
        self.name = url.parts[-1].replace('.md', '')
        self.is_md = url.parts[-1].endswith('.md')

    def __str__(self):
        return f'<a href="{self.url}">{self.name}</a>'