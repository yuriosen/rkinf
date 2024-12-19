a = '101101'
b = '110011'
a_dv = int(a, 2)
b_dv = int(b, 2)
and_res = bin(a_dv & b_dv)[2:]
sum_res = bin(a_dv + b_dv)[2:]
print('AND:', and_res)
print('Summ:', sum_res)
