

class Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

print("Qual a cor e o tamanhoqq da sua toalha")
color=input()
size=input()

towel : Towel = Towel(color,size)
print(f"Sua toalha é {towel.color} e {towel.size}")