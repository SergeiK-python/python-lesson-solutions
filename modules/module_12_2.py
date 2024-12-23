# Домашнее задание по теме "Методы Юнит-тестирования"

import HumanMoveTest.runner_and_tournament as runner
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


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__all_results = {}
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

    def setUp(self):
        self.__runners = []
        self.__runners.append(runner.Runner("Усэйн", 10))
        self.__runners.append(runner.Runner("Андрей", 9))
        self.__runners.append(runner.Runner("Ник", 3))

    @classmethod
    def tearDownClass(cls):
        for result in cls.__all_results.values():
            out = {u: str(v) for u, v in result.items()}
            print(f"{out}")

    @TestSwitcher.decorator(used=True)
    def test_get_winner_1(self):
        result = runner.Tournament(90, self.__runners[0], self.__runners[2]).start()
        self.__all_results["test_get_winner_1"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @TestSwitcher.decorator(used=True)
    def test_get_winner_3(self):
        result = runner.Tournament(90, self.__runners[0], self.__runners[1], self.__runners[2]).start()
        self.__all_results["test_get_winner_3"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @TestSwitcher.decorator(used=True)
    def test_get_winner_2(self):
        result = runner.Tournament(90, self.__runners[1], self.__runners[2]).start()
        self.__all_results["test_get_winner_2"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    # fault tests
    @TestSwitcher.decorator(used=False)
    def test_get_winner_4(self):
        result = runner.Tournament(3, self.__runners[0], self.__runners[1], self.__runners[2]).start()
        self.__all_results["test_get_winner_4"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @TestSwitcher.decorator(used=False)
    def test_get_winner_5(self):
        result = runner.Tournament(2, self.__runners[0], self.__runners[1], self.__runners[2]).start()
        self.__all_results["test_get_winner_5"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @TestSwitcher.decorator(used=False)
    def test_get_winner_6(self):
        result = runner.Tournament(1, self.__runners[0], self.__runners[1], self.__runners[2]).start()
        self.__all_results["test_get_winner_6"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @TestSwitcher.decorator(used=False)
    def test_get_winner_7(self):
        result = runner.Tournament(0, self.__runners[0], self.__runners[1], self.__runners[2]).start()
        self.__all_results["test_get_winner_7"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @TestSwitcher.decorator(used=False)
    def test_get_winner_8(self):
        result = runner.Tournament(-1, self.__runners[0], self.__runners[1], self.__runners[2]).start()
        self.__all_results["test_get_winner_8"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")


if __name__ == '__main__':
    unittest.main()
