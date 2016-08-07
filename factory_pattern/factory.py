import os

from zipfile import ZipFile
import tarfile


class BaseArchive(object):
    EXTENSION = None

    def __init__(self, location_path, files_to_pack):
        self.location_path = location_path
        self.files_to_pack = files_to_pack

    def generate(self):
        raise NotImplementedError()


class ZIPArchive(BaseArchive):
    EXTENSION = '.zip'

    @classmethod
    def check_extenstion(cls,extension):
        if extension == cls.EXTENSION:
            return True
        else:
            return False

    def generate(self):
        with ZipFile(self.location_path, 'w') as zip_file:
            for file_ in self.files_to_pack:
                zip_file.write(file_)


class TARArchive(BaseArchive):
    EXTENSION = '.tar'

    @classmethod
    def check_extenstion(cls,extension):
        if extension == cls.EXTENSION:
            return True
        else:
            return False

    def generate(self):
        with tarfile.open(self.location_path, 'w') as tar_file:
            for file_ in self.files_to_pack:
                tar_file.add(file_)

class ArchiveManager(object):
    ARCHIVE_ENGINES = [ZIPArchive, TARArchive]

    def __init__(self, location_path, files_to_pack):
        self.location_path, self.extension = os.path.splitext(location_path)
        self.files_to_pack = files_to_pack
        self.archive_engine = self.choose_archive_engine()

    def choose_archive_engine(self):
        for engine in self.ARCHIVE_ENGINES:
            if engine.check_extenstion(self.extension):
                return engine(self.location_path, self.files_to_pack)

    def create_archive(self):
        self.archive_engine.generate()


if __name__ == '__main__':
    zip_archive = ZIPArchive(os.path.join(os.getcwd(), 'zip.zip'), ['for_zip.txt'])
    zip_archive.generate()
    tar_archive = TARArchive(os.path.join(os.getcwd(), 'tar.tar'), ['for_tar.txt'])
    tar_archive.generate()

    archive = ArchiveManager(os.path.join(os.getcwd(), 'zips.zip'), ['for_zip', 'for_tar.txt'])
    archive.create_archive()
