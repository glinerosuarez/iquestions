"""
Write a function that returns a list of all the duplicate files. We'll check them by hand before actually deleting them,
since programmatically deleting files is really scary. To help us confirm that two files are actually duplicates, return
a list of tuples where:

the first item is the duplicate file
the second item is the original file
For example:

  [
    ('/tmp/parker_is_dumb.mpg', '/home/parker/secret_puppy_dance.mpg'),
    ('/home/trololol.mov', '/etc/apache2/httpd.conf')
 ]
You can assume each file was only duplicated once.
"""
import sys
from collections import defaultdict
from pathlib import Path
from typing import Tuple, List


class DuplicatesFinder:

    @staticmethod
    def _walk(_dir):
        for p in Path(_dir).iterdir():
            if p.is_dir():
                yield from DuplicatesFinder._walk(p)
            else:
                yield p.resolve()

    def _build_hash_table(self):
        pass

    def get_duplicate_files(self, path: str) -> List[Tuple[str, str]]:
        path = Path(path)
        hashes_by_size = defaultdict(list)

        for file in DuplicatesFinder._walk(path):
            hashes_by_size[file.stat().st_size].append(file.absolute())
            print(hashes_by_size)


if __name__ == "__main__":
    path = sys.argv[1]
    if path:
        finder = DuplicatesFinder()
        finder.get_duplicate_files(path)
    else:
        print("Please pass the path to check as parameter to the script")
