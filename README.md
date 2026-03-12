# numpy_cpp_add

A simple Python package with a C++ extension using pybind11.

## Install

```bash
$ git clone https://github.com/ducchung2444/python-lib-with-cpp.git
$ uv add ./python-lib-with-cpp
```

```python
import numpy_cpp_add

result = numpy_cpp_add.sum_array([1.0, 2.0, 3.0])
print(result)
```
