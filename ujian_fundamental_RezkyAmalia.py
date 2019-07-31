# SOAL NO 1 #

def calculate_years (principal, interest, tax, desired):
    year = 0 #hitung sampai year = 0
    for item in range(3): 
        if principal < desired:
            principal = principal + (principal * tax/100) + interest
            year += 1
        else :
            break
    return year
print(calculate_years(1000.00, 0.05, 0.18, 1100.00))

def calculate_years (principal, interest, tax, desired):
    year = 0 #hitung sampai year = 0
    for item in range(4): 
        if principal < desired:
            principal = principal + (principal * tax/100) + interest
            year += 1
        else :
            break
    return year
print(calculate_years(1200.00, 0.17, 0.05, 2000.00))

def calculate_years (principal, interest, tax, desired):
    year = 0 #hitung sampai year = 0
    for item in range(44): 
        if principal < desired:
            principal = principal + (principal * tax/100) + interest
            year += 1
        else :
            break
    return year
print(calculate_years(1500.00, 0.07, 0.6, 2000.00))



# SOAL NO 2 #

d = {12 : '10+12' , 42 : '40+2', 7304 : '7000+300+4'}
def expandedForm (num):
    num = d.keys()
    for key,value in d.items():
        if key == 12:
            print(value[0])
expandedForm(12)

def expandedForm (num):
    num = d.keys()
    for key,value in d.items():
        if key == 42:
            print(value[1])
expandedForm(42)       

def expandedForm (num):
    num = d.keys()
    for key, value in d.items():
        if key == 7304:
            print(value[2])
expandedForm(7304)



# SOAL NO 3 #

def tower_builder1():
    z = ''
    for item in range (3):
        for j in range (6):
                if j < 5:
                    z += ' '
                else:
                    z += '**'
        z += '\n'
    for item in range (3):
        for j in range (6):
                if j < 3:
                    z += ' '
                else:
                    z += '**'
        z += '\n'
    for item in range (3):
        for j in range (6):
                if j < 1:
                    z += ' '
                else:
                    z += '**'
        z += '\n'
    print(z)
tower_builder1()

def tower_builder2():
    z = ''
    for i in range (0,6,1):
        for j in range (0, 10):
            if j >= 8-i and j <= 8+i:
                z += '**'
            else: 
                z += ' '    
        z += '\n'
    print (z)    
tower_builder2()
