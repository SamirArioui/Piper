import os
import sys

sys.path.insert(0, os.getcwd())

import pandas as pd
from pandas.testing import assert_frame_equal

from piper.core.loaders import CSVLoader, ExcelLoader


class TestCSVLoder:

    path = "test/test_data/test_loaders/test.csv"
    csv_loader = CSVLoader(path)

    def test_load_default(self):
        result = self.csv_loader.load()
        expected = pd.read_csv(self.path)
        assert_frame_equal(result, expected)

    def test_load_sep(self):
        result = self.csv_loader.load(sep=",")
        exepected = pd.read_csv(self.path, sep=",")
        assert_frame_equal(result, exepected)


class TestExcelLoader:

    path = "test/test_data/test_loaders/test.xlsx"
    csv_loader = ExcelLoader(path)

    def test_load_default(self):
        result = self.csv_loader.load()
        expected = pd.read_excel(self.path)
        assert_frame_equal(result, expected)

    def test_load_sh_1(self):
        result = self.csv_loader.load(sheet_name="1")
        exepected = pd.read_excel(self.path, sheet_name="1")
        assert_frame_equal(result, exepected)

    def test_load_sh_2(self):
        result = self.csv_loader.load(sheet_name="2")
        exepected = pd.read_excel(self.path, sheet_name="2")
        assert_frame_equal(result, exepected)
