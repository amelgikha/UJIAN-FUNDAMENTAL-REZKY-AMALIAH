# # 1
# def calculate_years(principal, interest, tax, desired):
#     years = 0
#     while principal < desired:
#         principal += (principal*interest)*(1-tax)
#         years += 1
#     return print(years)
# calculate_years(1000.00,0.05,0.18,1100.00)
# calculate_years(1200.00,0.17,0.06,2000.00)
# calculate_years(1500.00,0.07,0.6,5000.00)



# # 2 
# def expandedForm(num):
#     y = str(num)
#     a = []
#     b = []
#     c = []
#     d = ''

#     for loop in range (len(y)):
#         a.append(y[loop])
#     for loop1 in range(len(y)-1,-1,-1):
#         b.append(10**loop1)
#     for loop2 in range(len(a)):
#         c.append(int(a[loop2])*b[loop2])
#     for loop3 in range(len(c)):
#         if c[loop3] != 0:
#             if loop3 == 0:
#                 d += str(c[loop3])
#             else:
#                 d += ' + ' + str(c[loop3])
#     return print(d)

# expandedForm(12)
# expandedForm(42)
# expandedForm(70304)



# # 3
# def tower_builder (n_floor, block_size):
#     w, h = block_size
#     z = ''
#     for loop1 in range (n_floor):
#         for loop2 in range(h):
#             for loop3 in range (((n_floor-1)*2)-(loop1*2)):
#                 z += ' '
#             for loop4 in range (w+(loop1*4)):
#                 z += '*'
#             z += '\n'
#     return print(z)

# tower_builder(3,(2,3))
# tower_builder(6,(2,1))

z = ''
for item in range (5):
    if item < 4 :
        for item1 in range (11):
            if item1 == 5-item or item1 == 5+item:
                z += '*'
            else :
                z += ' '
        z += '\n'
    else :
        for item2 in range (11):
            if item2 > 0 and item2 < 10:
                z += '*'
            else:
                z += ' '
print (z)