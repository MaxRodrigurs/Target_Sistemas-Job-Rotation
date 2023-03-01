string = input("Digite a string que deseja inverter:")
invertida = ""

for i in range(len(string)-1, -1, -1):
    invertida += string[i]

print(invertida)
