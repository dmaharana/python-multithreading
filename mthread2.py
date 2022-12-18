import threading
from datetime import datetime
import time
import os

tasks = [
    'Task1',
    'Task2',
    'Task3',
    'Task4',
    'Task5'
]

batchSize = 3

def perform_task(task_name):
    snow = datetime.now()
    time.sleep(3)
    run_os_cmd(f"mkdir {task_name}")
    enow = datetime.now()
    print(f"{snow} to {enow}: Performing task {task_name}")


def run_os_cmd(cmd):
    output = os.popen(cmd)
    while True:
        line = output.readline()

        if line:
            print(line, end='')
        else:
            break

    output.close()

def main():

    for i in range(0, len(tasks), batchSize):
        print(tasks[i:i+batchSize])
        batchTasks = tasks[i:i+batchSize]
        threadTasks = []
        for t in batchTasks:
            td = threading.Thread(target=perform_task, args=(t,))
            td.start()
            threadTasks.append(td)

        
        for t in threadTasks:
            t.join()
    
    print("~~~~~~~~~ END ~~~~~~~~")

main()

