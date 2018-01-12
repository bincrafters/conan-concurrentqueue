#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class ConcurrentqueueConan(ConanFile):
    name = "concurrentqueue"
    version = "1.0.0-beta"
    url = "https://github.com/bincrafters/conan-concurrentqueue"
    description = "A fast multi-producer, multi-consumer lock-free concurrent queue for C++11"
    
    # Indicates License type of the packaged library
    license = "https://github.com/cameron314/concurrentqueue/blob/master/LICENSE.md"
    
    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]
    
    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    
    def source(self):
        source_url = "https://github.com/cameron314/concurrentqueue"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)


    def package(self):
        include_folder = self.source_subfolder
        self.copy(pattern="LICENSE")
        self.copy(pattern="*h", dst="include/concurrentqueue", src=include_folder)

    def package_id(self):
        self.info.header_only()
