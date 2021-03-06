from distutils.core import setup, Extension
from distutils.command.build_py import build_py
import novelwriting.yapps
import os
import string
from glob import glob
from types import StringType, ListType, TupleType


class build_py_yapps(build_py):

    def find_package_modules(self, package, package_dir):
        modules = build_py.find_package_modules(self, package, package_dir)
        yapps_module_files = glob(os.path.join(package_dir, "*.g"))

        for f in yapps_module_files:
            module = os.path.splitext(os.path.basename(f))[0]
            modules.append((package, module, f))
        return modules

    def build_module(self, module, module_file, package):
        if type(package) is StringType:
            package = package.split(".")
        elif type(package) not in (ListType, TupleType):
            raise TypeError, \
                "'package' must be a string (dot-separated), list, or tuple"

        if module_file.endswith(".g"):
            outfile = self.get_module_outfile(self.build_lib, package, module)
            novelwriting.yapps.generate(module_file, outfile)
            self.announce("building %s -> %s" % (module_file, outfile))
        else:
            return build_py.build_module(self, module, module_file, package)

name = "Novelwriting"
version = "0.4.1"
DOCDIR = "/tmp/%s-%s" % (name, version)
setup(
    name=name,
    version=version,
    description="Rule-based text generation",
    author="Jeff Epler",
    author_email="jepler@unpythonic.net",
    url="http://unpythonic.net/jeff/novelwriting/",
    packages=['novelwriting'],
    license="GPL",
    long_description="""
Novelwriting randomly generates structured documents from a grammar.
It is inspired by the Dada Engine, but is written in and extensible
through Python.""",
    scripts=['scripts/novelwriting', 'scripts/novelwriting.cgi'],
    data_files=[(DOCDIR + "/examples", glob("examples/*.nw")),
                (DOCDIR, ["README.html", "novelwriting/gram.g"])],
    #ext_modules=[Extension("novelwriting.gram", ["novelwriting/gram.g"])],
    cmdclass={'build_py': build_py_yapps},
)

# vim:sts=4:sw=4:et:
