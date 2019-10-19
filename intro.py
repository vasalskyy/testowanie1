def sqrt(a, b):
    return (a+b)**2


def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


if __name__ == "__main__":

    assert sqrt(3, 6) > 20, "FAILED"
    print("FIRST PASSED")
    assert sqrt(int(input("wprowadz 1 liczbe: ")), int(input("wprowadz 2 liczbe: "))) > 10 , "FAILED"
    print("SECOND PASSED")
    print("jedziemy z koksem")

    assert factorial(5) == 120 , "FAILED"
    assert factorial(1) == 1
    assert factorial(10) == 3628800