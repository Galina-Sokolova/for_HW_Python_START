#1 — Напишите функцию группового переименования файлов. Она должна:
#* принимать в качестве аргумента желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
#* принимать в качестве аргумента расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
#* принимать в качестве аргумента расширение конечного файла.
#Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>

from pathlib import Path

__all__ = ['rename_files']


def rename_files(new_filename: str, old_extension: str,
                 new_extension: str,):

    way = Path.cwd()
    count = 0
    for file in way.iterdir():
        if file.suffix[1:] == old_extension:
            count += 1
            old_name, _ = Path(file).name.split('.')
            Path(file).rename(f'{old_name}_{new_filename}_{count}.{new_extension}')


if __name__ == '__main__':
    rename_files('new_name', 'txt', 'pdf')