# Домашнее задание по теме "Многопроцессное программирование"

import datetime
import multiprocessing

def read_info(name):
    with open(name, 'r') as f:
        all_data = []
        #last_line = ""
        while True:
            line: str = f.readline()
            if line != "":
                all_data.append(line)
                #last_line = line
            else:
                break
        #print (f'{name} - {len(all_data)} строк, {last_line}')
        #return all_data


if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    time_in = datetime.datetime.now()

    for filename in filenames:
        read_info(filename)

    print(f'{datetime.datetime.now() - time_in} (линейный)')
    time_in = datetime.datetime.now()

    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)


    print(f'{datetime.datetime.now() - time_in} (многопроцессный)')