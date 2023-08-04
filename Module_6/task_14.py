import shutil


def unpack(archive_path, path_to_unpack):
    unpack_archive = shutil.unpack_archive(archive_path, path_to_unpack)