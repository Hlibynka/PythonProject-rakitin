def add(a: float, b: float) -> float:
    print("LOG: operation add started")
    return a + b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Ділення на нуль неможливе")
    return a / b