carros = ["HRV", "Golf", "Argo", "Focus"]
carros.append("Fit")#Adiciona novos elementos dentro do array
carros.append("Fusion")
carros.append("Polo")
carros.remove("Fusion")#Remove elementos dentro do array
carros.pop()#Remove o último elemento da lista
carros2 = ["Fusca", "147", "Brasilia", "Celta"]
carros3 = carros2 + carros
print(str(len(carros3)) + " carros na lista")
print(carros3)
carros.clear()#Remove todosos elementos da lista
print(str(len(carros)) + " carros na lista")
print(carros)