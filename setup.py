from setuptools import setup, Extension, find_packages
import pybind11

ext_modules = [
    Extension(
        "numpy_cpp_add._core",
        ["src/numpy_cpp_add/cpp_add.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++",
    ),
]

setup(
    name="numpy_cpp_add",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages("src"),
    ext_modules=ext_modules,
)
