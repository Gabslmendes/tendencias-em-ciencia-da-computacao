# calculadora.py - versao refatorada (depois)
"""
calculadora.py - versão refatorada
Refatoração aplicada:
1. Eliminação da cadeia if/elif usando Strategy Pattern com dicionário
2. Separação de responsabilidades: lógica de cálculo vs interface de usuário
3. Tratamento de erros mais robusto
4. Código mais extensível e testável
"""

def adicionar(a: float, b: float) -> float:
    """Realiza adição de dois números."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Realiza subtração de dois números."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Realiza multiplicação de dois números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """Realiza divisão de dois números.
    
    Raises:
        ValueError: Se o divisor for zero.
    """
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b


# MELHORIA 1: Dicionário de operações substitui a cadeia if/elif
# Motivo: Mais limpo, extensível e segue o padrão Strategy
# Benefício: Adicionar novas operações é trivial (apenas um novo par chave-valor)
OPERACOES = {
    "+": adicionar,
    "-": subtrair,
    "*": multiplicar,
    "/": dividir,
}


# MELHORIA 2: Funções separadas para lógica de cálculo e interface
# Motivo: Princípio Single Responsibility - cada função tem uma responsabilidade
def calcular(num1: float, operacao: str, num2: float) -> float:
    """
    Realiza o cálculo com base na operação fornecida.
    
    Args:
        num1: Primeiro número
        operacao: Operação desejada (+, -, *, /)
        num2: Segundo número
    
    Returns:
        O resultado do cálculo
    
    Raises:
        ValueError: Se a operação não for válida ou ocorrer erro (ex: divisão por zero)
    """
    if operacao not in OPERACOES:
        raise ValueError(f"Operacao invalida: '{operacao}'")
    
    # Executa a função correspondente à operação
    funcao = OPERACOES[operacao]
    return funcao(num1, num2)


def interface_usuario() -> None:
    """
    Gerencia a interação com o usuário.
    
    Motivo da separação: A lógica de I/O (entrada/saída) é independente
    da lógica de negócio. Isso facilita testes unitários e reutilização.
    Benefício: Podemos testar calcular() sem mock de input/print.
    """
    print("Calculadora")
    
    try:
        # Coleta entrada do usuário
        num1 = float(input("Digite o primeiro numero: "))
        op = input("Digite a operacao (+, -, *, /): ")
        num2 = float(input("Digite o segundo numero: "))
        
        # Delega cálculo à função específica
        resultado = calcular(num1, op, num2)
        print("Resultado: " + str(resultado))
        
    except ValueError as e:
        # MELHORIA 3: Tratamento de erro mais explícito
        # Motivo: Captura operação inválida E divisão por zero
        # Benefício: Mensagem clara ao usuário sobre o problema
        print(f"Erro: {e}")


# MELHORIA 4: Ponto de entrada padrão Python
# Motivo: Permite importar este módulo em outros scripts sem executar código
# Benefício: Código mais profissional e reutilizável
if __name__ == "__main__":
    interface_usuario()
