from abc import ABC, abstractclassmethod
from pathlib import Path
from typing import Dict

import pandas as pd

from piper.core.utils import get_file_extension


class BaseLoader(ABC):
    def __init__(self, file_path: str) -> None:
        self.path = Path(file_path)
        self.extension = get_file_extension(file_path)

    @abstractclassmethod
    def load(self) -> Dict:
        pass


class CSVLoader(BaseLoader):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    def load(self, **kwargs) -> pd.DataFrame:
        return pd.read_csv(filepath_or_buffer=self.path, **kwargs)


class ExcelLoader(BaseLoader):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    def load(self, **kwargs) -> pd.DataFrame:
        return pd.read_excel(self.path, **kwargs)
