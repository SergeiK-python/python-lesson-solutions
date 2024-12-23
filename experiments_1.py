# wrapper for unittest
import unittest

class TestSwitcher:

    @classmethod
    def setUpClass(cls, off: bool or None = None, name: str or None = None):
        if off is not None:
            cls.__all_switched_off = off
        if name is not None:
            cls.__name = name

    def decorator(used=True):

        def inner(function):

            def wrapper(*args, **kwargs):
                if TestSwitcher.__all_switched_off:
                    raise unittest.SkipTest(f"Тесты в кейсе {TestSwitcher.__name} заморожены")
                elif used:
                    function(*args, **kwargs)
                else:
                    raise unittest.SkipTest(f'Данный тест {function.__name__} в кейсе {TestSwitcher.__name} заморожен')

            return wrapper

        return inner
