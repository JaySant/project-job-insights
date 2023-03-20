from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"

    count_python = count_ocurrences(path, "Python")
    assert count_python == 1639

    count_javascript = count_ocurrences(path, "Javascript")
    assert count_javascript == 122

# testa caso de insensitive

    count_uppercase = count_ocurrences(path, "PYTHON")
    assert count_uppercase == 1639
