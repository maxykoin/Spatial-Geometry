import sympy
forma = -1

while forma != 0:
    print('~'*30)
    forma = int(input('''Choose which solid do you want to calculate:
        [ 1 ] PYRAMID
        [ 2 ] CONE
        [ 3 ] CYLINDER
        [ 4 ] POLYGON
        [ 5 ] SPHERE
        [ 0 ] TO EXIT
    Enter here: '''))
    print('~'*30)
    
#### PYRAMIDS ###############################################################################################
    while forma == 1:
        formula = input('Write A for area or V for volume [0 to exit]: ').lower()
        if formula == 'a':
            print('~'*10, '''Triangle's Area''', '~'*10)
            b = float(input('Digite o valor do lado base: '))
            h = float(input('Digite o valor da altura: '))
            print('~'*30)

            base = int(input('''Choose the base:
                [ 1 ] SQUARE
                [ 2 ] RETANGLE
                [ 3 ] HEXAGON
            Enter here: '''))
            print('~'*30)

            while base == 1:
                l = float(input('Digite o valor da aresta: '))
                ab = l**2
                al = b * h / 2 * 4
                break

            while base == 2:
                b = float(input('Digite o valor da base: '))
                h = float(input('Digite o valor da altura: '))
                ab = b * h 
                al = b * h / 2 * 4
                break
            
            while base == 3:
                definition = input('Is the value of √3 defined (Y/N)? ').lower()
                if definition == 'y':
                    b = float(input('Digite o valor da base: '))
                    l = float(input('Digite o valor do lado: '))
                    ra = float(input('Digite o valor da raiz de 3: '))
                    ab = b * (l)**2 * ra / 4
                    al = b * h / 2 * 6
                    break
                
                if definition == 'n':
                    b = float(input('Digite o valor da base: '))
                    l = float(input('Digite o valor do lado: '))
                    ab = b * (l)**2 * sympy.sqrt(3) / 4
                    al = b * h / 2 * 6
                    break
                
            print('''Esse sólido tem a area da base de valor {} e a area lateral de valor {}.
            O valor da área total é de {}cm'''.format(ab, al, ab + al))

        if formula == 'v':
            definition = input('Is there any undefined square roots (Y/N)? ').lower()
            if definition == 'y':
                sqrt = int(input('Write down the number (without the square root): '))
                ab = float(input('Digite a area da base (w/o sqrt): '))
                h = float(input('Digite a altura (w/o sqrt): '))
                print('O volume desse sólido é {} {} cm'.format(ab * h / 3, sympy.sqrt(sqrt)))
                print('~'*30)
                break
    
            if definition == 'n':
                ab = float(input('Digite a area da base: '))
                h = float(input('Digite a altura: '))
                print('O volume desse sólido é {}cm'.format(ab * h / 3))
                print('~'*30)
                break
            
        if formula == '0':
            break
#### CONES #####################################################################################################    
    while forma == 2:
        formula = input('Write A for area or V for volume [0 to exit]: ').lower()
        if formula == 'a':
            definition = input('Is the value of π defined (Y/N)? ').lower()
            if definition == 'n':
                r = float(input('Digite o valor do raio: '))
                g = float(input('Digite o valor da geratriz: '))
                
                print('''Esse sólido tem a area da base de valor {} e a area lateral de valor {}
                A area total do sólido é de {}'''.format(sympy.pi * (r)**2, sympy.pi * r * g, sympy.pi * (r)**2 + sympy.pi * r * g))
                break 
            
            if definition == 'y':
                pi = float(input('Digite o valor de pi: '))
                r = float(input('Digite o valor do raio: '))
                g = float(input('Digite o valor da geratriz: '))
                print('''Esse sólido tem a area da base de valor {} e a area lateral de valor {}
                A area total do sólido é de {}'''.format(pi * (r)**2, pi * r * g, pi * (r)**2 + pi * r * g))
                break 
            
        if formula == 'v':
            definition = input('Is the value of pi undefined (Y/N)? ').lower()
            if definition == 'n':
                ab = float(input('Digite a area da base: '))
                h = float(input('Digite a altura: '))
                print('O volume desse sólido é de {} {}'.format(ab * h / 3, sympy.pi))
                break
            
            if definition == 'y':
                ab = float(input('Digite o valor da area da base: '))
                h = float(input('Digite o valor da altura: '))
                print('O volume desse sólido é de {}'.format(ab * h / 3))
                break
            
        if formula == '0':
            break 
#### CYLINDERS ###################################################################################################
    while forma == 3:
        formula = input('Write A for area or V for volume [0 to exit]: ').lower()
        if formula == 'a':
            definition = input('Is the value of π defined (Y/N)? ').lower()
            if definition == 'y':
                pi = float(input('Digite o valor de pi: '))
                r = float(input('Digite o valor do raio: '))
                h = float(input('Digite o valor da altura: '))
                ab = 2 * pi * (r)**2
                al = 2 * pi * r

                print('''Esse sólido tem a area da base de valor {} e a area lateral de valor {}
                A area total do sólido é de {}'''.format(ab, al, ab + al))
                break 
            
            if definition == 'n':
                r = float(input('Digite o valor do raio: '))
                h = float(input('Digite o valor da altura: '))
                ab = 2 * sympy.pi * (r)**2
                al = 2 * sympy.pi * r

                print('''Esse sólido tem a area da base de valor {} e a area lateral de valor {}
                A area total do sólido é de {}'''.format(ab, al, ab + al))
                break
            
        if formula == 'v':
            definition = input('Is the value of pi undefined (Y/N)? ').lower()
            if definition == 'n':
                ab = float(input('Digite a area da base: '))
                h = float(input('Digite a altura: '))
                print('O volume desse sólido é de {} {}'.format(ab * h, sympy.pi))
                break
            
            if definition == 'y':
                ab = float(input('Digite o valor da area da base: '))
                h = float(input('Digite o valor da altura: '))
                print('O volume desse sólido é de {}'.format(ab * h))
                break
            
        if formula == '0':
            break 
#### POLYGONS ###################################################################################################
    while forma == 4:
        formula = input('Write A for area or V for volume [0 to exit]: ').lower()
        if formula == 'a':
            print('~'*30)
            base = int(input('''
            Escolha a base (para bases diferentes, calcule uma por vez):
            [ 1 ] QUADRADO
            [ 2 ] RETÂNGULO
            [ 3 ] HEXAGONO
            '''))
            print('~'*30)

            while base == 1:
                a = float(input('Digite o valor da aresta: '))
                ab = a ** 2
                break

            while base == 2:
                b = float(input('Digite o valor da base: '))
                h = float(input('Digite o valor da altura: '))
                ab = b * h
                break

            while base == 3:
                definition = input('Is the value of √3 defined (Y/N)? ').lower()
                if definition == 'y':
                    b = float(input('Digite o valor da base: '))
                    l = float(input('Digite o valor do lado: '))
                    ra = float(input('Digite o valor da raiz de 3: '))
                    ab = b * (l)**2 * ra / 4
                    break
                if definition == 'n':
                    b = float(input('Digite o valor da base: '))
                    l = float(input('Digite o valor do lado: '))
                    ab = b * (l)**2 * sympy.sqrt(3) / 4
                    break
        
            print('~'*30)
            lateral = int(input('''
            Escolha a area lateral (para laterais diferentes, calcule uma por vez):
            [ 1 ] QUADRADO
            [ 2 ] RETÂNGULO
            [ 3 ] HEXAGONO
            [ 4 ] TRIÂNGULO
            '''))
            print('~'*30)

            while lateral == 1:
                a = float(input('Digite o valor da aresta: '))
                al = a ** 2
                break

            while lateral == 2:
                b = float(input('Digite o valor da base: '))
                h = float(input('Digite o valor da altura: '))
                al = al * h
                break

            while lateral == 3:
                definition = input('Is the value of √3 defined (Y/N)? ').lower()
                if definition == 'y':
                    b = float(input('Digite o valor da base: '))
                    l = float(input('Digite o valor do lado: '))
                    ra = float(input('Digite o valor da raiz de 3: '))
                    ab = b * (l)**2 * ra / 4
                    break
                
                if definition == 'n':
                    b = float(input('Digite o valor da base: '))
                    l = float(input('Digite o valor do lado: '))
                    ab = b * (l)**2 * sympy.sqrt(3) / 4
                    break

            while lateral == 4:
                b = float(input('Digite o valor da base: '))
                h = float(input('Digite o valor da altura: '))
                al = b * h / 2
                break

            print(''' Esse sólido tem a area da base de valor {} e a area lateral de valor {}.
            O valor da área total é de {}cm'''.format(ab, al, ab + al))
            break

        if formula == 'v': 
            definition = input('Is there any undefined square roots (Y/N)? ').lower()
            if definition == 'y':
                sqrt = int(input('Write down the number (without the square root): '))
                ab = float(input('Digite a area da base (w/o sqrt): '))
                h = float(input('Digite a altura (w/o sqrt): '))
                print('O volume desse sólido é {} {} cm'.format(ab * h, sympy.sqrt(sqrt)))
                print('~'*30)
                break
    
            if definition == 'n':
                ab = float(input('Digite a area da base: '))
                h = float(input('Digite a altura: '))
                print('O volume desse sólido é {}cm'.format(ab * h))
                print('~'*30)
                break
            
        if formula == '0':
            break
#### SPHERES ###################################################################################################
    while forma == 5: 
        formula = input('Write A for area or V for volume [0 to exit]: ').lower()
        
        if formula == 'a':
            definition = input('Is the value of π defined (Y/N)? ').lower()
            if definition == 'y':
                pi = float(input('Digite o valor de pi: '))
                r = float(input('Digite o valor do raio: '))
                print('A area total da esfera é de {}'.format(4 * pi * (r)**2)) 
                break
            
            if definition == 'n':
                r = float(input('Digite o valor do raio: '))
                print('A area total da esfera é de {}'.format(4 * sympy.pi * (r)**2))
                break
            
        print('~'*30)

        if formula == 'v':
            definition = input('Is the value of π defined (Y/N)? ').lower()
            if definition == 'y':
                pi = float(input('Digite o valor de pi: '))
                r = float(input('Digite o valor do raio: '))
                print('A area total da esfera é de {}'.format(4 * pi * (r)**3 / 3))
                break
            
            if definition == 'n':
                r = float(input('Digite o valor do raio: '))
                print('A area total da esfera é de {}'.format(4 * sympy.pi * (r)**3 / 3))
                break
            
        if formula == '0':
            break

