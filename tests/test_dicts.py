"""Sample test file."""

import pytest

from .utils import dict_approx


@pytest.mark.xfail(
    raises=AssertionError,
    reason="Because of floating point arithmetic, 0.1 + 0.2 != 0.3",
)
def test_numeric_dict():
    """Test numeric dict with floating point crumbs."""
    new_dict = {"a": 0.1, "b": 0.2, "c": 0.1 + 0.2}
    exp_dict = {"a": 0.1, "b": 0.2, "c": 0.3}

    # We expect this to fail, because of intricacies of floating point
    # arithmetic.
    assert new_dict == exp_dict


def test_numeric_dict_approx():
    """Test numeric dict with approx (much better)."""
    new_dict = {"a": 0.1, "b": 0.2, "c": 0.1 + 0.2}
    exp_dict = {"a": 0.1, "b": 0.2, "c": 0.3}

    assert new_dict == dict_approx(exp_dict)


def test_non_numeric_dict():
    """Test non-numeric dict."""
    new_dict = {}
    new_dict["three"] = "one" + "two"
    exp_dict = {"three": "onetwo"}

    assert new_dict == exp_dict


def test_non_numeric_dict_approx():
    """Test non-numeric dict, approximately.

    I kind of think this should work.
    """
    new_dict = {}
    new_dict["three"] = "one" + "two"
    exp_dict = {"three": "onetwo"}

    assert new_dict == dict_approx(exp_dict)


def test_mixed_dict():
    """With a mixed dict we run into problems!"""
    new_dict = {}
    new_dict["three"] = "one" + "two"
    new_dict["c"] = 0.1 + 0.2
    exp_dict = {"three": "onetwo", "c": 0.3}

    assert new_dict == dict_approx(exp_dict)


def test_numeric_dict_approx_toobig_diff_orig():
    """Test numeric dict with approx, when the diff is too big."""
    new_dict = {"a": 0.1, "b": 0.2, "c": 0.1 + 0.2}
    exp_dict = {"a": 0.1, "b": 0.2, "c": 0.4}

    # This really should fail
    assert new_dict == pytest.approx(exp_dict)


def test_numeric_dict_approx_toobig_diff_new():
    """Test numeric dict with approx, when the diff is too big."""
    new_dict = {"a": 0.1, "b": 0.2, "c": 0.1 + 0.2}
    exp_dict = {"a": 0.1, "b": 0.2, "c": 0.4}

    # This really should fail
    assert new_dict == dict_approx(exp_dict)
