from people import Manager, Worker, Agent
import random

names_list = []
surname_list = []


def currect_text_finder(some_line):
    temp_word = ''
    for letter in some_line:
        if letter.isalpha():
            temp_word += letter
    return temp_word


with open('names.txt', 'r') as names_file:
    for line in names_file:
        names_list.append(currect_text_finder(line))

with open('surnames.txt', 'r') as surname_file:
    for line in surname_file:
        surname_list.append(currect_text_finder(line))


manager_list = [Manager(name=random.choice(names_list), surname=random.choice(surname_list), age=random.randint(19, 99))
                for _ in range(3)]
worker_list = [Worker(name=random.choice(names_list), surname=random.choice(surname_list), age=random.randint(19, 99),
                      hours_worked=random.randint(1, 5000)) for _ in range(3)]
agent_list = [Agent(name=random.choice(names_list), surname=random.choice(surname_list), age=random.randint(19, 99),
                    sales_volume=random.randint(1500, 50000)) for _ in range(3)]

workers_list = manager_list + worker_list + agent_list

for worker in workers_list:
    print(worker.info())
