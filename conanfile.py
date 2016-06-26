from conans import ConanFile, CMake
import os

class GumboConan(ConanFile):
    name = "GumboQuery"
    version = "latest"

    #original project url = "https://github.com/lazytiger/gumbo-query.git"
    url = "https://github.com/ruipires/conan-gumbo-query.git" # repo of this wrapper
    license = "The MIT License (MIT)"
    settings = "os", "compiler", "build_type", "arch"
    requires = "Gumbo/0.10.1@rui/stable"
    exports = ("*", "CMakeLists.txt")
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

#    def source(self):
#        self.run("git clone https://github.com/lazytiger/gumbo-query.git")

    def build(self):
        cmake = CMake(self.settings)
        self.output.info("CMake configuration")
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.output.info("CMake build")
        self.run("cmake --build . --target gumbo_query_static %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="./src")
        self.copy("*.lib", dst="lib", src=".", keep_path=False)
        self.copy("*.a", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", src=".", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", src=".", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["gq"]
