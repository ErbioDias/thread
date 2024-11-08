import threading
import time

# Função que simula uma tarefa demorada
def tarefa1():
    for i in range(3):
        print("Tarefa 1 - Passo", i + 1)
        time.sleep(1)
    print("Tarefa 1 concluída!")

def tarefa2():
    for i in range(3):
        print("Tarefa 2 - Passo", i + 1)
        time.sleep(1.5)
    print("Tarefa 2 concluída!")

def tarefa3():
    for i in range(3):
        print("Tarefa 3 - Passo", i + 1)
        time.sleep(2)
    print("Tarefa 3 concluída!")

# Cria as threads
thread1 = threading.Thread(target=tarefa1)
thread2 = threading.Thread(target=tarefa2)
thread3 = threading.Thread(target=tarefa3)

# Inicia as threads
thread1.start()
thread2.start()
thread3.start()

# Aguarda todas as threads terminarem
thread1.join()
thread2.join()
thread3.join()

print("Todas as tarefas foram concluídas!")
