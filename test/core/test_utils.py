import os
import sys

sys.path.insert(0, os.getcwd())

import piper.core.utils as util


def test_get_file_extension():
    extension = util.get_file_extension("test/test.txt")
    assert extension == "TXT"