import carro

MustangPreto = carro.Carro("Preto", 2, "Gasolina", 1.6)
help(MustangPreto.abastecer) #chamando a Docstring
MustangPreto.ligar()
print(f"Quantidade anterior: {MustangPreto.qtd_combustivel}")
MustangPreto.abastecer(50)
MustangPreto.abastecer(10)
print(f"Quantidade atual: {MustangPreto.qtd_combustivel}")
MustangPreto.acelerar(20)
print(f"A velocidade atual é de: {MustangPreto.velocidade}")
del MustangPreto #posso tanto usar o método __del__ ou, nesse caso, diretamente quando quero apagar o objeto da memória

MustangVermelho = carro.Carro("Vermelho", 2, "Gasolina", 1.0)
MustangVermelho.desligar()
print(f"A quantidade atual de combustível do Mustang Vermelho é: {MustangVermelho.qtd_combustivel}")
MustangVermelho.acelerar(50)
MustangVermelho.ligar()
MustangVermelho.acelerar(20)
print(f"A velocidade atual é de: {MustangVermelho.velocidade}")

