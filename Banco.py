
import threading
import time
 
db_semaphore = threading.Semaphore(1)
balance = 100
 
def cajero(id):
    operation_amount = 20
    print(f"Cajero {id} intentando realizar una operación")
    with db_semaphore:
        global balance
        current_balance = balance
        time.sleep(1)
        balance = current_balance + operation_amount
        print(f"Cajero {id} ha realizado un depósito. Nuevo balance: {balance}")
 
cajeros = []
 
for i in range(5):
    cajero_thread = threading.Thread(target=cajero, args=(i,))
    cajeros.append(cajero_thread)
    cajero_thread.start()
 
for cajero_thread in cajeros:
    cajero_thread.join()