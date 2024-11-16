import unittest
import logging
from HumanMoveTest.rt_with_exceptions import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """
        тест метода walk
        создаётся объект класса Runner с произвольным именем.
        Далее вызовите метод walk у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 50.
        """
        runner = Runner('name')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """
        тест метода run
        создаётся объект класса Runner с произвольным именем.
        Далее вызовите метод run у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 100.
        """
        runner = Runner('name')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """
        совместный тест методов run и walk
        test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
        Далее 10 раз у объектов вызываются методы run и walk соответственно.
        Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
        """
        runner1 = Runner('name1')
        runner2 = Runner('name1')
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        """
        создаётся атрибут класса all_results.
        Это словарь в который будут сохраняться результаты всех тестов.
        """
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        """ создаются 3 объекта Runner """
        self.runners = [
            Runner("Усэйн", 10),
            Runner("Андрей", 9),
            Runner("Ник", 3),
        ]

    @classmethod
    def tearDownClass(cls):
        """ выводятся all_results по очереди в столбец. """
        for tournament, results in cls.all_results.items():
            print(f'{tournament}: {{{', '.join([f'{place}: {name}' for place, name in results.items()])}}}')

    def __test_tournament(self, distance:int, *people:str):
        participants = [runner for runner in self.runners if runner in people]
        tournament = Tournament(distance, *participants)
        # У объекта класса Tournament запускается метод start,
        # который возвращает словарь в переменную all_results.
        return tournament.start()

    # методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
    # Ник всегда должен быть последним.
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        """ тест tournament для двух участников """
        results = self.__test_tournament(90, 'Усэйн', 'Ник')
        self.all_results['1'] = results
        self.assertTrue(results[max(results)] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        """ тест tournament для двух других участников """
        results = self.__test_tournament(90, 'Андрей', 'Ник')
        self.all_results['2'] = results
        self.assertTrue(results[max(results)] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        """ тест tournament для трех участников """
        results = self.__test_tournament(90, 'Усэйн', 'Андрей', 'Ник')
        self.all_results['3'] = results
        self.assertTrue(results[max(results)] == 'Ник')

    """
    В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. 
    В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, 
    чем бегун с большей. Попробуйте решить эту проблему и обложить дополнительными тестами.
    """
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament4(self):
        """ тест исправления ошибки в tournament.start """
        results = self.__test_tournament(5, 'Усэйн', 'Андрей', 'Ник')
        self.all_results['4'] = results
        self.assertTrue(results[len(results)] == 'Ник')


if __name__ == '__main__':
    logging.basicConfig()
    unittest.main()
    """
    Вывод на консоль:
    {1: Усэйн, 2: Ник}
    {1: Андрей, 2: Ник}
    {1: Андрей, 2: Усэйн, 3: Ник}
    """


"""
2024/01/12 00:00|Домашнее задание по теме "Логирование"
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.
Цель: получить опыт использования простейшего логирования совместно с тестами.

Задача "Логирование бегунов":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное значение в speed.

Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
Уровень - INFO
Режим - запись с заменой('w')
Название файла - runner_tests.log
Кодировка - UTF-8
Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.

Дополните методы тестирования в классе RunnerTest следующим образом:
test_walk:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте отрицательное значение в speed.
В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".
test_run:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте что-то кроме строки в name.
В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".
Пример результата выполнения программы:
Пример полученного файла логов runner_tests.log:


Файл tests_12_4.py с классами тестов и runner_tests.log с логами тестов загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
"""