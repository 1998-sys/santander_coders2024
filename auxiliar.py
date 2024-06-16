### Funçoes auxiliares
import time

def valor_numerico(mensagem):
    """
    Solicita que o usuário digite um valor e verifica se é numérico (inteiro ou ponto flutuante).
    Continua solicitando até que um valor válido seja fornecido.

    Parâmetros:
    mensagem (str): A mensagem que será exibida ao solicitar a entrada do usuário.

    Retorna:
    float ou int: O valor numérico digitado pelo usuário.
    
    """
    while True:
        numero = input(mensagem)
        try:
            numero = float(numero)
            return numero
            break

        except:
            print('Entrada Inválida digite um valor numérico')
            time.sleep(3)
