# import sys 

N = int(input())

numbers = input()
number_list = [int(x) for x in numbers.split()]
# print(number_list)
calcs = input()
calc_list = [int(x) for x in calcs.split()]

result_list = []
order = 1 

def calculate_everything(number_list, result, idx, plus, minus, mult, div, result_list, equation):
    # number_list : 입력으로 받은 수들의 리스트 
    # result : a_i의 값(a_i까지 연산한 결과 값, 초기 값은 a_1)
    # a_i : i번째 숫자 
    # idx : a_i와 a_(i+1)이 연산할 때 i+1 (2부터 시작)
    # calc_list : 현재 남아있는 연산자들의 list 
    # result_list : 마지막 수까지 연산한 결과들을 저장하는 list 
    
    if plus > 0: # +가 남아있는 경우 
        equation_plus = equation + '+' + str(number_list[idx+1])
        result_plus = result + number_list[idx+1]
        if idx + 1 == len(number_list)- 1:
            # print(equation_plus+ '=' + str(result_plus))
            result_list.append(result_plus)
        else:
            calculate_everything(number_list, result_plus, idx + 1, plus-1, minus, mult, div, result_list, equation_plus)
    
    if minus > 0: # -가 남아있는 경우 
        equation_minus = equation + '-' + str(number_list[idx+1])
        result_minus = result - number_list[idx+1]
        if idx + 1 == len(number_list)- 1:
            # print(equation_minus+ '=' + str(result_minus))
            result_list.append(result_minus)
        else:
            calculate_everything(number_list, result_minus, idx + 1, plus, minus-1, mult, div, result_list, equation_minus)

    if mult > 0: # -가 남아있는 경우 
        # 곱하기 연산을 수행 
        equation_mult = equation + '*' + str(number_list[idx+1])
        result_mult = result * number_list[idx+1]

        # 끝까지 모두 연산한 경우 
        if idx + 1 == len(number_list) - 1 :
            # print(equation_mult + '=' + str(result_mult))
            result_list.append(result_mult)
        else:
            calculate_everything(number_list, result_mult, idx + 1, plus, minus, mult-1, div, result_list, equation_mult)
    
    if div > 0: # / 가 남아있는 경우 
        equation_div = equation + '/' + str(number_list[idx+1])
        if result < 0:
            result_div = (-1 * result) // number_list[idx+1]
            result_div = result_div * -1
        else:
            result_div = result // number_list[idx+1]

        if idx + 1 == len(number_list)- 1:
            # print(equation_div+ '=' + str(result_div))
            result_list.append(result_div)
        else:
            calculate_everything(number_list, result_div, idx + 1, plus, minus, mult, div-1, result_list, equation_div)


calculate_everything(number_list, number_list[0], 0, calc_list[0],calc_list[1],calc_list[2],calc_list[3], result_list, str(number_list[0]))
result_list = sorted(result_list)
print(result_list[-1])
print(result_list[0])
