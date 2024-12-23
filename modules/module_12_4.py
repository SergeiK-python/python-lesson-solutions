# Домашнее задание по теме "Логирование"
import unittest
import logging
import HumanMoveTest.runner_and_tournament as runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s - %(levelname)s - %(message)s')

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
    def test_walk_done(self):
        try:
            worker = runner.Runner('Vasya', 10)
            for ii in range(10):
                worker.walk()
            self.assertEqual(worker.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.error(msg=e, exc_info=True)

    def test_walk_fault(self):
        try:
            worker = runner.Runner('Vasya', -10)
            for ii in range(10):
                worker.walk()
            self.assertEqual(worker.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.error(msg=e, exc_info=True)

    @TestSwitcher.decorator(used=True)
    def test_run_done(self):
        try:
            worker = runner.Runner('Ivan', 10)
            for ii in range(10):
                worker.run()
            self.assertEqual(worker.distance, 200)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.error("msg=e, exc_info=True)", exc_info=True)

    @TestSwitcher.decorator(used=True)
    def test_run_fault(self):
        try:
            worker = runner.Runner(True, -10)
            for ii in range(10):
                worker.run()
            self.assertEqual(worker.distance, 200)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.error("msg=e, exc_info=True)", exc_info=True)


if __name__ == '__main__':
    unittest.main()

