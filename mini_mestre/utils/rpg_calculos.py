def calcular_bonus_proficiencia(nivel):
    if nivel <= 4:
        return 2
    elif nivel <= 8:
        return 3
    elif nivel <= 12:
        return 4
    elif nivel <= 16:
        return 5
    else:
        return 6


def calcular_modificador(valor):
    return (valor - 10) // 2