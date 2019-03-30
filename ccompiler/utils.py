import os
import subprocess

from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring

c_compiler = '/usr/bin/gcc'
cpp_compiler = '/usr/bin/g++'
nvcc_compiler = ''

@magics_class
class NVCCCompiler(Magics):

    def __init__(self, shell):
        super().__init__(shell)
        current_dir = os.getcwd()
        self.src_nvcc = os.path.join(current_dir, "source.cu")
        self.src_c = os.path.join(current_dir, "source.c")
        self.src_cpp = os.path.join(current_dir, "source.cpp")
        self.out = os.path.join(current_dir, "result.out")

    def compile(self, compiler, src):
        output = subprocess.check_output([compiler, src, "-o", self.out], stderr=subprocess.STDOUT)

    def run(self):
        output = subprocess.check_output([self.out], stderr=subprocess.STDOUT)
        output = output.decode('utf8')
        return output

    @magic_arguments()
    @argument('-c', '--compile', type=str, help='Compilation flags for nvcc, e.g. pkg-config')
    @cell_magic
    def nvcc(self, line='', cell=None):
        args = parse_argstring(self.nvcc, line)

        with open(self.src_nvcc, "w") as f:
            f.write(cell)

        try:
            self.compile(nvcc_compiler, self.src_nvcc)
            output = self.run()
        except subprocess.CalledProcessError as e:
            print(e.output.decode("utf8"))
            output = None

        print(output)

        return None

    @magic_arguments()
    @argument('-c', '--compile', type=str, help='Compilation flags for nvcc, e.g. pkg-config')
    @cell_magic
    def gcc(self, line='', cell=None):
        args = parse_argstring(self.nvcc, line)

        with open(self.src_c, "w") as f:
            f.write(cell)

        try:
            self.compile(c_compiler, self.src_c)
            output = self.run()
        except subprocess.CalledProcessError as e:
            print(e.output.decode("utf8"))
            output = None

        print(output)

        return None

    @magic_arguments()
    @argument('-c', '--compile', type=str, help='Compilation flags for nvcc, e.g. pkg-config')
    @cell_magic
    def gcpp(self, line='', cell=None):
        args = parse_argstring(self.nvcc, line)

        with open(self.src_cpp, "w") as f:
            f.write(cell)

        try:
            self.compile(cpp_compiler, self.src_cpp)
            output = self.run()
        except subprocess.CalledProcessError as e:
            print(e.output.decode("utf8"))
            output = None

        print(output)

        return None
