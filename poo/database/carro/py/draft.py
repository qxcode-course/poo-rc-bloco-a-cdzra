class Carro:
    def __init__(self):
        self.pas: int = 0
        self.km: int = 0
        self.gas: int = 0
    
    def __str__(self) -> str:
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"
    
    def embarca(self,increment: int) -> None:
        if self.pas + increment > 2:
            print(f"fail: limite de pessoas atingido")
            self.pas = 2
            return
        self.pas += increment

    def desembarca(self,increment: int) -> None:
        if self.pas - increment < 0:
            print(f"fail: nao ha ninguem no carro")
            self.pas = 0
            return
        self.pas -= increment
        
        
def main():
    carro: Carro = Carro()
    while True:

        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "enter":
            increment: int = int(args[0])
            carro.embarca(increment)
        elif args[0] == "show":
            print(carro)

main()