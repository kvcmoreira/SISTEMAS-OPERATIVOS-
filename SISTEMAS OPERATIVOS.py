import threading
import time

# Función que será ejecutada por los hilos
def print_numbers(name, delay, count):
    for i in range(count):
        time.sleep(delay)
        print(f"{name}: {i+1}")

# Crear dos hilos
thread1 = threading.Thread(target=print_numbers, args=("Hilo 1", 2, 3))
thread2 = threading.Thread(target=print_numbers, args=("Hilo 2", 2, 3))

# Iniciar los hilos
thread1.start()
thread2.start()

# Esperar a que los hilos terminen
thread1.join()
thread2.join()

print("Finalizando el programa principal")
