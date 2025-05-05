# Código extra criado por mim (Raíssa Robadel) para o desafio "Resolvendo Códigos em Python com o Github Copilot". O código consiste em uma Receita Interativa de Palha Italina de Casadinho!
# A receita verifica se o usuário tem os ingredientes necessários e, em seguida, fornece instruções passo a passo para preparar a sobremesa 🍫

# Como é minha primeira vez utilizando Python, utilizei o GitHub Copilot para me auxiliar na construção do código, porém, sempre pedindo explicações e entendendo ponto a ponto o que estava sendo feito.

print("🍫 Receita Interativa de Palha Italiana de Casadinho 🍫")
print("Vamos verificar os ingredientes!")

# Lista global para armazenar todos os ingredientes faltantes
todos_ingredientes_faltantes = []

# Verificação dos ingredientes do brigadeiro de chocolate
print("🤎 Para o brigadeiro de chocolate: ")
ingredientesChocolate = [
    "1 caixa/lata de leite condensado",
    "2 caixas de creme de leite",
    "3 colheres de sopa de cacau em pó",
    "1 colher de sopa de manteiga",
    "1 pacote de biscoito maisena"
]

for ingrediente in ingredientesChocolate:
    while True:
        resposta = input(f"Você tem {ingrediente}? (sim/não): ").strip().lower() # O strip() remove espaços em branco no início e no final da string, enquanto o lower() converte todos os caracteres da string para letras minúsculas.
        if resposta == "sim":
            break
        elif resposta == "não":
            if ingrediente not in todos_ingredientes_faltantes:
                todos_ingredientes_faltantes.append(ingrediente) # O método append() em Python é usado para adicionar um item ao final de uma lista.
            print(f"Você ainda não tem {ingrediente}. Digite 'continuar' para verificar os próximos ingredientes: ") # O f antes de {} é usado para criar uma f-string (formatted string literal) em Python. Ele permite que você insira o valor de variáveis ou expressões diretamente dentro de uma string, substituindo o conteúdo das chaves {} pelo valor correspondente, e evitando o uso de +
            resposta = input().strip().lower()
            if resposta == "continuar":
                break
        else:
            print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

# Exibição dos ingredientes faltantes após o brigadeiro de chocolate
if todos_ingredientes_faltantes:
    print("\n⚠️ Ingredientes faltando até agora:")
    for item in todos_ingredientes_faltantes:
        print(f"- {item}")
else:
    print("\n✅ Você tem todos os ingredientes para o brigadeiro de chocolate!")

# Verificação dos ingredientes do brigadeiro branco
print("\n🤍 Para o brigadeiro branco: ")
ingredientesBranco = [
    "mais 1 caixa/lata de leite condensado",
    "mais 2 caixas de creme de leite",
    "5 colheres de sopa de leite em pó",
    "mais 1 colher de sopa de manteiga",
    "mais 1 pacote de biscoito maisena"
]

for ingrediente in ingredientesBranco:
    while True:
        resposta = input(f"Você tem {ingrediente}? (sim/não): ").strip().lower()
        if resposta == "sim":
            break
        elif resposta == "não":
            if ingrediente not in todos_ingredientes_faltantes:
                todos_ingredientes_faltantes.append(ingrediente)
            print(f"Você ainda não tem {ingrediente}. Digite 'continuar' para verificar os próximos ingredientes: ")
            resposta = input().strip().lower() 
            if resposta == "continuar":
                break
        else:
            print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

# Exibição dos ingredientes faltantes após o brigadeiro branco
if todos_ingredientes_faltantes:
    print("\n⚠️ Ingredientes faltando até agora:")
    for item in todos_ingredientes_faltantes:
        print(f"- {item}")
else:
    print("\n✅ Você tem todos os ingredientes para o brigadeiro branco!")

# Verificação dos ingredientes para a montagem
print("\n✨ Para a montagem da palha italiana: ")
ingredientesMontagem = [
    "açúcar refinado para passar em volta",
    "papel manteiga para forrar a forma",
    "forma retangular"
]

for ingrediente in ingredientesMontagem:
    while True:
        resposta = input(f"Você tem {ingrediente}? (sim/não): ").strip().lower()
        if resposta == "sim":
            break
        elif resposta == "não":
            if ingrediente not in todos_ingredientes_faltantes:
                todos_ingredientes_faltantes.append(ingrediente)
            print(f"Você ainda não tem {ingrediente}. Digite 'continuar' para verificar os próximos ingredientes: ")
            resposta = input().strip().lower()
            if resposta == "continuar":
                break
        else:
            print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

# Exibição dos ingredientes faltantes após a montagem
if todos_ingredientes_faltantes:
    print("\n⚠️ Ingredientes faltando até agora:")
    for item in todos_ingredientes_faltantes:
        print(f"- {item}")
else:
    print("\n✅ Você tem todos os ingredientes para a montagem!")

# Mensagem final
if not todos_ingredientes_faltantes:
    print("\n✅ Ótimo! Você tem todos os ingredientes para a receita!")
else:
    print("\n⚠️ Atenção! Providencie sua lista de compras para que seja possível fazer a receita. Você ainda está sem os seguintes ingredientes:")
    for item in todos_ingredientes_faltantes:
        print(f"- {item}")

print("\n ✨ Organize todos os ingredientes na cozinha e vamos para o preparo!")

mensagem = "🍪 Quebre todos os biscoitos em pedaços pequenos e reserve."
while True:
        resposta = input(f"{mensagem} (Digite 'Feito' para continuar): ").strip().lower()
        if resposta == "feito":
            break
        else:
            print("Por favor, digite 'Feito' quando concluir este passo.")

mensagem = "🥣 Deixe a vasilha retangular forrada com papel manteiga."
while True:
        resposta = input(f"{mensagem} (Digite 'Feito' para continuar): ").strip().lower()
        if resposta == "feito":
            break
        else:
            print("Por favor, digite 'Feito' quando concluir este passo.")

mensagem = "🤎 🥣 Em uma panela, coloque o leite condensado, o creme de leite, o cacau em pó e a manteiga."
while True:
        resposta = input(f"{mensagem} (Digite 'Feito' para continuar): ").strip().lower()
        if resposta == "feito":
            break
        else:
            print("Por favor, digite 'Feito' quando concluir este passo.")

mensagem = "🤎 🔥 Misture tudo e leve ao fogo médio, mexendo sempre até desgrudar do fundo da panela. Quando estiver no ponto, retire do fogo e acrescente metade dos biscoitos quebrados."
while True:
        resposta = input(f"{mensagem} (Digite 'Feito' para continuar): ").strip().lower()
        if resposta == "feito":
            break
        else:
            print("Por favor, digite 'Feito' quando concluir este passo.")

mensagem = "🤎 🥄 Misture bem e despeje na forma forrada com papel manteiga."
while True:
        resposta = input(f"{mensagem} (Digite 'Feito' para continuar): ").strip().lower()
        if resposta == "feito":
            break
        else:
            print("Por favor, digite 'Feito' quando concluir este passo.")

print("🤎 O brigadeiro de chocolate está pronto! 🤍 Vamos fazer o brigadeiro branco. 🧽💦 Lave os ítens necessários.")

mensagem = "🤍 🔥 Agora, faça o mesmo com os ingredientes do brigadeiro branco. Coloque o leite condensado, o creme de leite, o leite em pó e a manteiga na panela."
while True:
        resposta = input(f"{mensagem} (Digite 'Feito' para continuar): ").strip().lower()
        if resposta == "feito":
            break
        else:
            print("Por favor, digite 'Feito' quando concluir este passo.")

mensagem = "🤍 🥣 Misture tudo e leve ao fogo médio, mexendo sempre até desgrudar do fundo da panela. Quando estiver no ponto, retire do fogo e acrescente a outra metade dos biscoitos quebrados."
while True:
        resposta = input(f"{mensagem} (Digite 'Feito' para continuar): ").strip().lower()
        if resposta == "feito":
            break
        else:
            print("Por favor, digite 'Feito' quando concluir este passo.")

mensagem = "🤍 🥄 Misture bem e despeje na forma forrada com papel manteiga."
while True:
        resposta = input(f"{mensagem} (Digite 'Feito' para continuar): ").strip().lower()
        if resposta == "feito":
            break
        else:
            print("Por favor, digite 'Feito' quando concluir este passo.")

mensagem = "🧊 Agora, leve a forma à geladeira por cerca de 4 horas para endurecer. Quando já estiver bem firme, retire da forma e corte em pedaços."
while True:
        resposta = input(f"{mensagem} (Digite 'Feito' para continuar): ").strip().lower()
        if resposta == "feito":
            break
        else:
            print("Por favor, digite 'Feito' quando concluir este passo.")

mensagem= "🧂 Passe os pedaços no açúcar refinado e coloque em um prato/vasilha/travessa, para servir."
while True:
        resposta = input(f"{mensagem} (Digite 'Feito' para continuar): ").strip().lower()
        if resposta == "feito":
            break
        else:
            print("Por favor, digite 'Feito' quando concluir este passo.")

print("Pronto! Sua deliciosa palha italiana de casadinho está pronta! Eu quero um pedaço hein 😋")
