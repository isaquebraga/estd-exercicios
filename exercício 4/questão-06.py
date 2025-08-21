def fibonacci(numero):
    if numero == 1:
        return 0
    elif numero == 2:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)
        
print(fibonacci(10))