

lst_desordenada = [8,9,4,7,1,3,2,1,4]
# https://www.devmedia.com.br/algoritmos-de-ordenacao-analise-e-comparacao/28261
# todo corrigir essa ordenacao
def ordenacao_bolha(wlst):
    lst = wlst.copy()
    troca = 0
    while troca < len(lst):
        start_index = troca
        for index in range(troca + 1, len(lst)):
            if lst[start_index] > lst[index]:
                print(lst[start_index], ' ')
                tmp = lst[index]
                lst[index] = lst[start_index]
                lst[start_index] = tmp

            start_index += 1
        troca += 1

    return lst

print(lst_desordenada)
lst_ordenada = ordenacao_bolha(lst_desordenada)
print(lst_ordenada)
