import time

def fun_a(t):
    for i in range(t):
        print("fun_a", end=" ")
        time.sleep(1)
    return 1

def fun_b(t):
    for i in range(t):
        print("fun_b", end=" ")
        time.sleep(1)
    return 2

def main():
    results = [fun_a(2), fun_b(3)]
    print(results)

main()