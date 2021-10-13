from conans import ConanFile, tools
import shutil
import os.path


class Package(ConanFile):
    name = "barbarian-test_pkg_export_sources"
    license = "BSL-1.0"
    author = "Rene Ferdinand Rivera Morell"
    url = "https://barbarian.bfgroup.xyz/"
    description = "Barbarian test for packaging with `export_sources`."
    topics = ('**test**')
    exports_sources = "file1.txt", "file2.txt"
    settings = "os", "compiler", "build_type", "arch", "cppstd"
    version = "0.0.0"

    def source(self):
        shutil.copy(os.path.join("file1.txt"), os.path.join("src", "FILE1"))
        shutil.copy(os.path.join("file2.txt"), os.path.join("src", "FILE2"))

    def build(self):
        pass

    def package_id(self):
        self.info.header_only()

    def package(self):
        pass

    def package_info(self):
        pass
