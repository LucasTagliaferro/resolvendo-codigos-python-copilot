# Módulo: calculando_media_notas.py

def calcular_media_notas():
    """
    Solicita notas ao usuário e calcula a média aritmética.
    O usuário pode digitar 'fim' a qualquer momento para terminar a entrada.
    """
    # 1. Armazenamento: Inicializa uma lista vazia para guardar as notas.
    notas = []
    
    print("--- Calculadora de Média de Notas ---")
    print("Digite as notas uma por uma.")
    print("Para finalizar a entrada e calcular a média, digite 'fim'.")
    
    # 2. Coleta (Loop): Loop infinito que só é interrompido pelo comando 'break'.
    while True:
        # Pede a entrada do usuário
        entrada = input("Digite uma nota (ou 'fim'): ").strip().lower()
        
        # Critério de Parada
        if entrada == 'fim':
            break  # Sai do loop while
        
        # 3. Tratamento de Erro (Ajuste/Variável):
        # Tenta converter a entrada para um número decimal (float).
        try:
            nota = float(entrada)
            
            # Validação simples: Ignorar notas negativas (opcional, mas boa prática)
            if nota < 0:
                print("Nota inválida. Por favor, digite um valor positivo.")
                continue  # Volta para o início do loop sem adicionar a nota
                
            # Adiciona a nota válida à lista
            notas.append(nota)
            print(f"Nota {nota} adicionada. Total de notas: {len(notas)}")
            
        except ValueError:
            # Captura o erro se a conversão para float falhar (ex: usuário digitou letras)
            print(f"Entrada inválida: '{entrada}'. Por favor, digite um número ou 'fim'.")
            
    # 4. Cálculo da Média:
    if not notas: # Verifica se a lista de notas está vazia
        print("\nNenhuma nota foi inserida. A média não pode ser calculada.")
        return # Termina a função
    
    # Usa funções embutidas do Python para o cálculo
    soma_das_notas = sum(notas)
    quantidade_de_notas = len(notas)
    media = soma_das_notas / quantidade_de_notas
    
    # 5. Resultado: Exibe os resultados finais
    print("\n--- Resultado Final ---")
    print(f"Notas inseridas: {notas}")
    print(f"Soma das notas: {soma_das_notas:.2f}")
    print(f"Quantidade de notas: {quantidade_de_notas}")
    print(f"A média das notas é: {media:.2f}")

# Bloco principal que executa a função quando o script é iniciado
if __name__ == "__main__":
    calcular_media_notas()