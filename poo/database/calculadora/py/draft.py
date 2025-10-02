class Calculadora:
    def __init__(self,batteryMax: int):
        self.batteryMax : int = batteryMax
        self.battery: int = 0
        self.display: float = 0

    def __str__(self):
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def carregar(self,increment: int):
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def soma(self, a: float, b: float) -> None:
        if self.battery > 0:
            self.display = a + b
            self.battery -= 1
        else:
            print("fail: bateria insuficiente")

    def divi(self, a: float, b: float) -> None:
        if self.battery > 0:
            if b != 0:
                self.display = a / b
                self.battery -= 1
            else:
                print("fail: divisao por zero")
                self.battery -= 1
        else:
            print("fail: bateria insuficiente")

    

def main():
    calculadora : Calculadora = Calculadora("")
    
    while True:

        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            batteryMax: int = int(args[1])
            calculadora = Calculadora(batteryMax)
        elif args[0] == "charge":
            increment: int = int(args[1])
            calculadora.carregar(increment)
        elif args[0] == "sum":
            a: float = float(args[1])
            b: float = float(args[2])
            calculadora.soma(a,b)
        elif args[0] == "div":
            a: float = float(args[1])
            b: float = float(args[2])
            calculadora.divi(a,b)
        elif args[0] == "show":
            print(calculadora)



main()