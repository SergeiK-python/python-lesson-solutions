# Домашнее задание по теме "Простые Юнит-Тесты"
import unittest

import HumanMoveTest.runner as runner


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


class RunnerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__is_frozen = False
        TestSwitcher.setUpClass(off=cls.__is_frozen, name=f"{__name__}.{cls.__name__}")
        if getattr(cls, f'_{cls.__name__}__was_locked', None) is not None:
            cls.lockTests()

    @classmethod
    def lockTests(cls):
        cls.__is_frozen = True
        cls.__was_locked = True
        TestSwitcher.setUpClass(off=cls.__is_frozen)
        return cls

    @TestSwitcher.decorator(used=True)
    def test_walk(self):
        worker = runner.Runner('Vasya')
        for ii in range(10):
            worker.walk()
        self.assertEqual(worker.distance, 50)

    @TestSwitcher.decorator(used=True)
    def test_run(self):
        worker = runner.Runner('Vasya')
        for ii in range(10):
            worker.run()
        self.assertEqual(worker.distance, 100)

    @TestSwitcher.decorator(used=True)
    def test_challenge(self):
        worker1 = runner.Runner('Vasya')
        worker2 = runner.Runner('Petya')
        for ii in range(10):
            worker1.run()
            worker2.walk()
        self.assertNotEqual(worker1.distance, worker2.distance)


if __name__ == '__main__':
    unittest.main()
