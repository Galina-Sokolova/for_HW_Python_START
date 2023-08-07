# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.
import argparse
import os
from collections import namedtuple
import logging


def get_info_about_file(dir_path=''):
    if dir_path == '':
        dir_path = os.getcwd()
    entries = os.scandir(dir_path)
    Obj = namedtuple('Item', ['name', 'extension', 'is_dir', 'parent_dir'])
    inf = []
    for entry in entries:
        name = os.path.splitext(entry.name)[0]
        ext = os.path.splitext(entry.name)[1] if not entry.is_dir() else ""
        is_dir = entry.is_dir()
        parent_dir = os.path.basename(os.path.normpath(dir_path))
        inf.append(Obj(name, ext, is_dir, parent_dir))

    logging.basicConfig(filename='info.log.', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger('Info about file:')
    logger.info(f'in:{dir_path}, out:{inf}')
    return inf


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-dir_path', metavar='dir_path', type=str, default='')
    args = parser.parse_args()
    res = get_info_about_file(args.dir_path)
    # print(res)
