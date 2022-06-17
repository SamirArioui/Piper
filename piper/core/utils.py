from pathlib import Path


def get_file_extension(file_name):
    path = Path(file_name)
    extension = path.suffix.split(".")[-1].upper()
    return extension