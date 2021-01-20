import operator

import pytest

from threadop import fp


def test_threadop_rewrites_functions():
    @fp
    def example():
        return 42 | operator.add(2) | operator.mul(5)

    assert example() == 220


def test_threadop_fails_if_rhs_is_not_a_fn_call():
    with pytest.raises(RuntimeError):
        @fp
        def example():
            return 42 | operator.add
