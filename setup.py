
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cc-extension",
    version="0.0.1",
    author="Durasov Nikita",
    author_email="yassnda@gmail.com",
    description="Jupyter magic for C code compilation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/NikitaDurasov/dstorch",
    py_modules=['cc_plugin', 'ccompiler.utils'],
)