from pathlib import Path
from itertools import chain

folder_path = Path(r'C:\Users\IT-Academy-Gomel\Downloads')

subfolder_name_to_extension = {
    'Video': ('mp4', 'mov', 'avi', 'mpg', 'mpeg', 'm4v', 'h264'),
    'audio': ('mp3', 'wav', 'wma', 'mid', 'ogg', 'flac'),
    'image': ('png', 'jpeg', 'jpg', 'svg', 'tif', 'tiff'),
    'archive': ('zip', 'rar', '7z', 'z', 'gz', 'deb'),
    'text': ('txt', 'pdf', 'doc', 'docx', 'rtf', 'odt'),
    'spreadsheet': ('xls', 'xlsx', 'xlsm'),
    'presentation': ('pptx', 'ppt'),
    'book': ('fb2', 'epub', 'mobi'),
    'gif': ('gif',),
    'torrent': ('torrent',),
    'exe': ('exe',),
    'code': ('html', 'py', 'js', 'jar', 'cpp', 'h', 'fig', 'xml', 'css','unitypackage')
}

subfolder_names = tuple(subfolder_name_to_extension.keys())
extensions = tuple(
    chain.from_iterable(
        subfolder_name_to_extension.values()
    ))


def get_subfolder_name_by_extension(extension: str) -> str:
    """get name of subfolder,by extensions

    :param extension: Extensions of file
    :return: under-folder name
    """

    for underfolder_name, tuple_of_extensions in subfolder_name_to_extension.items():
        if extension in tuple_of_extensions:
            return underfolder_name

