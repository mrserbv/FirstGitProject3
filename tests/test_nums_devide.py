from first.nums import devide
import pytest

# вариант 1
def test_devision():
    assert devide(10, 2) == 5


# вариант 2
def test_devision2():
    assert devide(10, 2) == 5
    assert devide(10, 10) == 1
    assert devide(10, -2) == -5


# вариант 3 - использование модуля pytest
@pytest.mark.parametrize("a, b, result", [(10, 2, 5),
                                          (20, 10, 2),
                                          (30, -3, -10),
                                          (5, 2, 2.5)])
def test_devision3(a, b, result):
    assert devide(a, b) == result

# вариант 4 - Проверка вывода ошибки при делении на 0
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        devide(10, 0)


# вариант 5 - Проверка типа
def test_type_error():
    with pytest.raises(TypeError):
        devide(10, "0")

# вариант 6 - Проверка на ошибки с использованием модуля pytest
@pytest.mark.parametrize("exept, a, b", [(ZeroDivisionError, 10, 0),
                                         (TypeError, 10, "str"),
                                         (TypeError, "str", 1)])
def test_error(exept, a, b):
    with pytest.raises(exept):
        devide(a, b)

