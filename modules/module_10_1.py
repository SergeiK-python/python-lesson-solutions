# Домашнее задание по теме "Введение в потоки".
import threading
import time
from time import sleep

def write_words(word_count, file_name):
    path = "./" + file_name
    with open(path, "w") as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i + 1} \n")
            sleep(.1)
    print(f"Завершилась запись в файл {file_name}")

def get_time(seconds: float):
    return time.strftime(    "%H:%M:%S", time.gmtime(seconds))

time_in = time.time()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

print(f"Работа потоков : {get_time(time.time() - time_in)}")
time_in = time.time()

threading1 = threading.Thread(target=write_words, args=(10, "example5.txt"))
threading2 = threading.Thread(target=write_words, args=(30, "example6.txt"))
threading3 = threading.Thread(target=write_words, args=(200, "example7.txt"))
threading4 = threading.Thread(target=write_words, args=(100, "example8.txt"))

threading1.start()
threading2.start()
threading3.start()
threading4.start()

threading1.join()
threading2.join()
threading3.join()
threading4.join()

print(f"Работа потоков : {get_time(time.time() - time_in)}")