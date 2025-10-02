class Calculadora:
    def __init__(self,batteryMax: int):
        self.batteryMax : int = batteryMax
        self.battery: int = 0
        self.display: float = 0

    def _str__(self):
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
def main():
    calculadora : Calculadora = Calculadora("")
    
    while True:

        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(calculadora)



main()