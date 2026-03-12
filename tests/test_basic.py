import numpy as np
import numpy_cpp_add


def test_sum_array_simple():
    a = np.array([1.0, 2.0, 3.0], dtype=np.float64)
    result = numpy_cpp_add.sum_array(a)

    assert result == 6.0


def test_sum_array_float():
    a = np.array([1.1, 2.2, 3.3], dtype=np.float64)
    result = numpy_cpp_add.sum_array(a)

    assert np.isclose(result, 6.6)


def test_sum_array_multidim():
    a = np.array([[1, 2], [3, 4]], dtype=np.float64)
    result = numpy_cpp_add.sum_array(a)

    assert result == 10.0
