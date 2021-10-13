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
        os.mkdir("src")
        shutil.copy("file1.txt", os.path.join("src", "file1.txt"))
        shutil.copy("file2.txt", os.path.join("src", "file2.txt"))

    def build(self):
        pass

    def package_id(self):
        self.info.header_only()

    def package(self):
        pass

    def package_info(self):
        pass
