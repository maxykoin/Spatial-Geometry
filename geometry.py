import sympy

def start():
    solid = int(input('''Choose which solid do you want to calculate:
            [ 1 ] PYRAMID
            [ 2 ] CONE
            [ 3 ] CYLINDER
            [ 4 ] SPHERE
            Enter here: '''))
    return solid

def square(l):
    return l**2 

def rectangle(b, h):
    return b * h

def hexagon(l, sqrt):
    return 3 * (l)**2 * sqrt / 2

def triangle(b, h, l):
    return (b * h / 2) * l  

def circle(pi, r):
    return pi * r**2
        
def pyramid():
    print('~'*10, "PYRAMID", '~'*10)
    formula =  input('Write A for area or V for volume: ').lower()
            
    if formula == 'a':
        print('~'*10, "PYRAMID'S AREA", '~'*10)

        print("Area of the triangle")
        b = float(input("Value of the edge: "))
        h = float(input("Value of the height: "))
        print('~'*30)
        
        base = int(input('''Area of the base
            [ 1 ] SQUARE
            [ 2 ] RETANGLE
            [ 3 ] HEXAGON
            Enter here: '''))
        print('~'*30)
        
        
        match base:
            case 1: 
                l = float(input("Value of the edge: "))
                ab = square(l)
                al = triangle(b, h, 4)
            case 2:
                b = float(input("Value of the edge: "))
                h = float(input("Value of the height: "))
                ab = rectangle(b, h)
                al = triangle(b, h, 4)
            case 3:
                definition = input('Is the value of √3 defined (Y/N)? ').lower()
                if definition == 'y':
                    l = float(input("Value of the edge: "))
                    sqrt = float(input("Value of the √3: "))
                    ab = hexagon(l, sqrt)
                if definition == 'n':
                    l = float(input("Value of the edge: "))
                    sqrt = sympy.sqrt(3)
                    ab = hexagon(l, sqrt)
                al = triangle(b, h, 6)
            case _: print("This command doesn't exist, try again.")
            
        print(f"\n This pyramid's base has the are of {ab}cm and the lateral area of {al}. \n -> The total value of the area is {ab + al}cm \n", '~'*100)

    if formula == 'v':
        print('~'*10, "PYRAMID'S VOLUME", '~'*10)
        definition = input('Is there any undefined square roots (Y/N)? ').lower()
        if definition == 'y':
            sqrt = int(input('The number under the sqrt (w/o sqrt): '))
            ab = float(input('Value of the area of the base (w/o sqrt): '))
            h = float(input('Value of the height (w/o sqrt): '))
            print(f'-> The volume of this pyramid is {ab * h / 3} {sympy.sqrt(sqrt)} cm')
            print('~'*100)
    
        if definition == 'n':
            ab = float(input('Value of the area of the base: '))
            h = float(input('Value of the height: '))
            print(f'-> The volume of this pyramid is {ab * h / 3}cm')
            print('~'*100)

def cone():
    print('~'*10, "CONE", '~'*10)
    formula =  input('Write A for area or V for volume: ').lower()
    
    if formula == 'a':
        print('~'*10, "CONE'S AREA", '~'*10)
        definition = input('Is the value of π defined (Y/N)? ').lower()
        if definition == 'n':
            print("Area of the base")
            r = float(input('Value of the radius: '))
            pi = sympy.pi
            ab = circle(pi, r)
            
            print("Lateral area")
            g = float(input('Value of the geratrix: '))
            al = sympy.pi * r * g
            
            
        if definition == 'y':
            print("Area of the base")
            pi = float(input('Value of π: '))
            r = float(input('Value of the radius: '))
            ab = circle(pi, r)
            
            print("Lateral area")
            g = float(input('Value of the geratrix: '))
            al = pi * r * g
    
        print(f"This cone's base has the area of {ab}cm and the lateral area of {al}. \n -> The total value of the area is {ab + al}cm\n", '~'*100)

    if formula == 'v':
        print('~'*10, "CONE'S VOLUME", '~'*10)
        definition = input('Is the value of π undefined (Y/N)? ').lower()
        if definition == 'n':
            ab = float(input('Area of the base: '))
            h = float(input('Value of the height: '))
            print(f'The volume of this cone is {ab * h / 3} {sympy.pi}', '~'*100)
            
        if definition == 'y':
            ab = float(input('Area of the base: '))
            h = float(input('Value of the height: '))
            print(f'The volume of this cone is {ab * h / 3}', '~'*100)

def cylinder():
    print('~'*10, "CYLINDER", '~'*10)
    formula =  input('Write A for area or V for volume: ').lower()
    
    if formula == 'a':
        print('~'*10, "CYLINDER'S AREA", '~'*10)
        definition = input('Is the value of π defined (Y/N)? ').lower()
        if definition == 'y':
            pi = float(input('Value of π: '))
            r = float(input('Value of the radius: '))
            h = float(input('Value of the height: '))
            ab = 2 * circle(pi, r)
            al = 2 * pi * r * h

            
        if definition == 'n':
            r = float(input('Value of the radius: '))
            h = float(input('Value of the height: '))
            pi = sympy.pi
            ab = 2 * circle(pi, r)
            al = 2 * pi * r * h
    
        print(f"\n This cylinder's base has the are of {ab}cm and the lateral area of {al}. \n -> The total value of the area is {ab + al}cm \n", '~'*100)
    
    if formula == 'v':
        print('~'*10, "CYLINDER'S VOLUME", '~'*10)
        definition = input('Is the value of π defined (Y/N)? ').lower()
        if definition == 'y':
            ab = float(input('Area of the base: '))
            h = float(input('Value of the height: '))
            print(f'-> O volume desse sólido é de {ab * h}', '~'*100)
            
        if definition == 'n':
            ab = float(input('Area of the base: '))
            h = float(input('Value of the height: '))
            print(f'-> O volume desse sólido é de {ab * h}{sympy.pi}', '~'*100)

def sphere():
    print('~'*10, "SPHERE", '~'*10)
    formula =  input('Write A for area or V for volume: ').lower()
    
    if formula == 'a':
        print('~'*10, "SPHERE'S AREA", '~'*10)
        definition = input('Is the value of π defined (Y/N)? ').lower()
        if definition == 'y':
            pi = float(input('Value of π: '))
            r = float(input('Value of the radius: '))
            a = 4 * circle(pi, r)
                
        if definition == 'n':
            pi = sympy.pi
            r = float(input('Value of the radius: '))
            a = 4 * circle(pi, r)
        
        print(f"\n This sphere's area is {a}", '~'*100)       

    if formula == 'v':
        print('~'*10, "SPHERE'S VOLUME", '~'*10)
        definition = input('Is the value of π defined (Y/N)? ').lower()
        if definition == 'y':
            pi = float(input('Value of π: '))
            r = float(input('Value of the radius: '))
            print(f'The volume of this sphere is of {4 * pi * (r)**3 / 3}')
            
        if definition == 'n':
            pi = sympy.pi
            r = float(input('Value of the radius: '))
            print(f'The volume of this sphere is of {4 * pi * (r)**3 / 3}')
            
while True:
    match start():
        case 1: pyramid()
        case 2: cone()
        case 3: cylinder()
        case 4: sphere()
        case _: print("This command doesn't exist, try again.")
