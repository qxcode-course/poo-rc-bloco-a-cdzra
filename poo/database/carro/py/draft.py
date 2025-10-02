class Carro:
    def __init__(self, pas: int = 0, km: int = 0, gas: int = 0):
        self.pas = pas
        self.km = km
        self.gas = gas
    
    def __str__(self) -> str:
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"
    
    def maxPas(self):
        if self.pas < 2:
            self.pas += 1
        else:
            print("fail: limite de pessoas atingido")
        
    def sair(self):
        if self.pas == 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.pas -= 1

    def maxGas(self,increment: int):
        self.gas += increment
        if self.gas > 100:
            self.gas = 100

    def viagem(self,distance: int):
        if self.pas == 0:
            print("fail: nao ha ninguem no carro")
        elif self.gas == 0:
            print("fail: tanque vazio")
        else:
            if distance > self.gas:
                print(f"fail: tanque vazio apos andar {self.gas} km")
                self.km += self.gas
                self.gas = 0
            else:
                self.km += distance
                self.gas -= distance

        
def main():
    carro: Carro = Carro()
    while True:

        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "enter":
            carro.maxPas()
        elif args[0] == "leave":
            carro.sair()
        elif args[0] == "fuel":
            increment = int(args[1])
            carro.maxGas(increment)
        elif args[0] == "drive":
            distance = int(args[1])
            carro.viagem(distance)
        elif args[0] == "show":
            print(carro)

main()