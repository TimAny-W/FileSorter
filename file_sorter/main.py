import os
from config import *
from typing import Iterable, Union

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from UI import Ui_MainWindow


class Sorter(QtWidgets.QMainWindow):
    def __init__(self):
        super(Sorter, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Сортировщик файлов')
        self.ui.lineEdit.setPlaceholderText('Вставьте путь к папке сортировки')
        self.ui.pushButton.clicked.connect(self.sort())

    def sort(self):
        input_path = self.ui.lineEdit.text()
        if input_path == '':
            self.ui.label_3.setText('Вставьте путь к папке сортировки')
            self.ui.label.repaint()
            return self.sort
        start_text = f'Сортировка файлов в {input_path}'
        self.ui.label_3.setText(start_text)
        folder = Folder(fr'{input_path}')
        output = folder.sort_files_by_extension()
        self.ui.label_3.setText(f'{start_text}\n{output}')
        self.ui.label.repaint()



class Folder:
    """Class for sorting files by folders"""

    def __init__(self, path: Union[Path, str]) -> None:
        self.path = path

    def _get_file_path(self) -> Iterable:
        """ Get file path

        :return: path iterator to file
        """
        return (file.path for file in os.scandir(self.path) if not file.is_dir())

    def _create_subfolder(self, underfolder_name: str) -> None:
        """ Creating under-folder

        :param underfolder_name: name under-folder
        :return: None
        """

        try:
            underfolder_path = Path(fr'{self.path}\{underfolder_name}')
            if not underfolder_path.exists():
                underfolder_path.mkdir()

        except OSError as ex:
            print(f'Ошибка создания директории -> {repr(ex)}')

    def sort_files_by_extension(self) -> str:
        """Sort files by extension

        :return: None
        """
        file_count = 0
        try:
            for filepath in self._get_file_path():
                path = Path(filepath)
                extension = path.suffix.split('.')[-1]
                if extension in extensions:
                    subfolder_name = get_subfolder_name_by_extension(extension)
                    self._create_subfolder(subfolder_name)

                    new_path = Path(self.path, subfolder_name, path.name)
                    path.rename(new_path)

                    file_count += 1
            return f'Sorted files count:{file_count}'
        except OSError as ex:
            return f'Ошибка cортировки -> {repr(ex)}'


# def sorting_files() -> None:
# folder = Folder(folder_path)
# print(f'Sorting files in {folder_path}')
# folder.sort_files_by_extension()


# if __name__ == '__main__':
# sorting_files()

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    application = Sorter()
    application.show()

    sys.exit(app.exec_())
