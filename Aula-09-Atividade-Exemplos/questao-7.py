convidados = ["Cavani", "Cristinao", "Messi", "Neymar", "Ronaldo"]

for mensagem in convidados:
    print("Olá {}, estamos convidando você e sua família para o nosso evento na uniesp".format(mensagem))

print("")
print("")

naoComparece = ["Messi"]
del(convidados[2])

for quemNaoComparece in naoComparece:
    print("{} não vai comparecer ao evento!".format(quemNaoComparece))

print("")

for mensagemAtualizada in convidados:
    print("Olá {}, estamos convidando você e sua família para o nosso evento na uniesp".format(mensagemAtualizada))


"""
A lista de convidados é formada.

A mensagem personalizada é enviada para cada uma delas.

Depois um dos convidados é excluído da lista e tem seu nome apresentado

No final, novas mensagens são enviadas para os convidados, exceto para aquele que não irá comparecer.

"""