forma = -1

while forma != 0:
    print('~'*30)
    forma = int(input('''
    [ 0 ] TO EXIT
    [ 1 ] PIRÂMIDE
    [ 2 ] CONE
    [ 3 ] CILINDRO
    [ 4 ] PRISMA
    [ 5 ] ESFERA
    Qual é sua escolha? 
    '''))
    print('~'*30)

    ### PYRAMID ###
    while forma == 1:
        formula = input('Digite A para área e V para volume [0 pra voltar]: ').lower()
        if formula == 'a':
            print('~'*10, 'Área Lateral', '~'*10)
            pb = float(input('Digite o valor do lado base: '))
            ph = float(input('Digite o valor da altura: '))
            print('~'*30)
            al = pb * ph / 2

            print('~'*30)
            base = int(input('''
            Escolha a base:
            [ 1 ] QUADRADO
            [ 2 ] RETÂNGULO
            [ 3 ] HEXAGONO
            '''))
            print('~'*30)

            while base == 1:
                ab = float(input('Digite o valor da aresta: '))
                ab = ab ** 2
                al * 4
                break

            while base == 2:
                b = float(input('Digite o valor da base: '))
                h = float(input('Digite o valor da altura: '))
                ab = b * h
                al * 4
                break

            while base == 3:
                b = float(input('Digite o valor da base: '))
                l = float(input('Digite o valor do lado: '))
                ra = float(input('Digite o valor da raiz de 3: '))
                ab = b * (l)**2 * ra / 4
                al * 6
                break
            
            print(''' Esse sólido tem a area da base de valor {} e a area lateral de valor {}.
            O valor da área total é de {}cm'''.format(ab, al, ab + al))

        if formula == 'v':
            ab = float(input('Digite a area da base: '))
            h = float(input('Digite a altura: '))
            print('O volume desse sólido é {}cm'.format(ab * h / 3))
            print('~'*30)
            break
        if formula == '0':
            break
        
    ### CONES ###
    while forma == 2:
        formula = input('Digite A para área e V para volume [0 pra voltar]: ').lower()
        if formula == 'a':
            pi = float(input('Digite o valor de pi: '))
            r = float(input('Digite o valor do raio: '))
            g = float(input('Digite o valor da geratriz: '))
            print('''Esse sólido tem a area da base de valor {} e a area lateral de valor {}
            A area total do sólido é de {}'''.format(pi * (r)**2 + pi * r * g ))

        if formula == 'v':
            ab = float(input('Digite o valor da area da base: '))
            h = float(input('Digite o valor da altura: '))
            print('O volume desse sólido é de {}'.format(ab * h / 3))
            break
        
        if formula == '0':
            break
        
    ### CYLINDERS ###
    while forma == 3:
        formula = input('Digite A para área e V para volume [0 pra voltar]: ').lower()
        if formula == 'a':
            pi = float(input('Digite o valor de pi: '))
            r = float(input('Digite o valor do raio: '))
            h = float(input('Digite o valor da altura: '))
            ab = 2 * pi * (r)**2
            al = 2 * pi * r

            print('''Esse sólido tem a area da base de valor {} e a area lateral de valor {}
            A area total do sólido é de {}'''.format(ab, al, ab + al))

        if formula == 'v':
            ab = float(input('Digite o valor da area da base: '))
            h = float(input('Digite o valor da altura: '))
            print('O volume desse sólido é de {}'.format(ab * h))
            break
    
        if formula == '0':
            break
    
    ### POLYGONS ###
    while forma == 4:
        formula = input('Digite A para área e V para volume [0 pra voltar]: ').lower()
        if formula == 'a':
            print('~'*30)
            base = int(input('''
            Escolha a base (calcule de uma base por vez):
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
                b = float(input('Digite o valor da base: '))
                l = float(input('Digite o valor do lado: '))
                ra = float(input('Digite o valor da raiz de 3 (3 ou o valor apresentado na questão): '))
                ab = ab * l** 2 * ra / 4
                break
        
            print('~'*30)
            lateral = int(input('''
            Escolha a area lateral (calcule de uma lateral por vez):
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
                b = float(input('Digite o valor da base: '))
                l = float(input('Digite o valor do lado: '))
                ra = float(input('Digite o valor da raiz de 3 (3 ou o valor apresentado na questão): '))
                al = al * l** 2 * ra / 4
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
            ab = float(input('Digite a area da base: '))
            h = float(input('Digite o valor da altura do solido: '))
            print('O volume desse sólido com a area de base {} e altura de {}, é de {}'.format(ab, h, ab * h))
            break

        if formula == '0':
            break
        
    ### SPHERE ###
    while forma == 5: 
        formula = input('Digite A para área e V para volume [0 pra voltar]: ').lower()
        print('~'*30)

        if formula == 'a':
            pi = float(input('Digite o valor de pi: '))
            r = float(input('Digite o valor do raio: '))
            print('A area total da esfera é de {}'.format(4 * pi * (r)**2))
        
        print('~'*30)

        if formula == 'v':
            pi = float(input('Digite o valor de pi: '))
            r = float(input('Digite o valor do raio: '))
            print('O volume total da esfera é de {}'.format(4 * pi * (r)**3 / 3))
            break
        
        if formula == '0':
            break

