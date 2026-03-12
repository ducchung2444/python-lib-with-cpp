#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

double sum_array(py::array_t<double> arr) {
    auto buf = arr.request();
    double* ptr = static_cast<double*>(buf.ptr);

    size_t n = 1;
    for (auto s : buf.shape) {
        n *= static_cast<size_t>(s);
    }

    double sum = 0.0;
    for (size_t i = 0; i < n; ++i) {
        sum += ptr[i];
    }

    return sum;
}

PYBIND11_MODULE(_core, m) {
    m.doc() = "C++ core for numpy_cpp_add";
    m.def("sum_array", &sum_array, "Sum all elements of a NumPy array");
}
