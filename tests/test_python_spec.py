import re
import pytest


def test_object_assign():
    # jsのObject.assignのpython version
    def assign(target: dict, *args):
        for arg in args:
            target.update(arg)
        return target

    dict1 = {"a": 1}
    dict2 = {"a": 2}
    dict3 = {"a": 3}
    res = assign(dict1.copy(), dict2)
    assert res == dict2
    res = assign(dict1.copy(), dict2, dict3)
    assert res == dict3
