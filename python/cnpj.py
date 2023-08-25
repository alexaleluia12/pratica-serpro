

def valida_cnpj(entrada):
    """
    1 - tamaho 14 digitos
    2 - 12 primeiros base, 2 ultimos verificadores
    3 - multiplicar cada numeroda da base por: 5,4,3,2,9,8,7,6,5,4,3,2 respectivamente
    4 - soma cada um dos numeros multiplicados na base
    5 - resto da divisao do passo 4 por 11 => R
    6 - R = 0 ou 1 entao primeiro digito deve ser 0
    6 - R != 0 ou 1 entao primeiro digito deve ser 11 - R
    7 - confirmar segundo digito verificador - multiplica base+primeiro digito verificador por
        6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2 respectivamente
    8 - soma de todos numero do passo 7
    9 - resto da divisao do passo 8 por 11 => S
    10 - S = 0 ou 1 entao segundo digito deve ser 0
    10 - S != 0 ou 1 entao segundo digito deve ser 11 - S
    Referencia: https://blog.dbins.com.br/como-funciona-a-logica-da-validacao-do-cnpj
    """
    assert len(entrada) == 14, "cnpj invalido"

    first_digit_check = False
    second_digit_check = False

    multi_primeiro_digito = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    multi_segundo_digito = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    digitos_cnpj = [int(e) for e in entrada]
    base = digitos_cnpj[:12]
    primeiro_verificador = digitos_cnpj[-2]
    segundo_verificador = digitos_cnpj[-1]

    sum_primeiro_digito = sum([iv*base[i] for i,iv in enumerate(multi_primeiro_digito)])
    r = sum_primeiro_digito % 11
    if r in (0, 1):
        if primeiro_verificador == 0:
            first_digit_check = True
    elif primeiro_verificador == 11 - r:
        first_digit_check = True
    else:
        return False # falha ao checar primeiro digito

    #segundo digito
    base.append(primeiro_verificador)
    sum_segundo_digito = sum([iv*base[i] for i,iv, in enumerate(multi_segundo_digito)])
    s = sum_segundo_digito % 11
    if s in (0, 1):
        if segundo_verificador == 0:
            second_digit_check = True
    elif segundo_verificador == 11 - s:
        second_digit_check = True
    else:
        return False

    return first_digit_check and second_digit_check



cnpj1 = "58577114000189"
print(valida_cnpj(cnpj1))

print(valida_cnpj("51665450000134"))

print(valida_cnpj("51665410000134")) # invalido

print(valida_cnpj("02332886000104"))