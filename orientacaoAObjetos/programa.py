from registro import Registro

class Programa:
    registro = Registro()

    def registrar(self):
        print('\n[1]- registrar pessoa')
        print('[2]- registrar estudante')
        print('[3]- registrar professor')
        print('[4]- registrar monitor')
        op = input('escolha a opção desejada: ')

        if op == '1':
            self.registro.registrar_pessoa()
        
        elif op == '2':
            self.registro.registrar_estudante()
        
        elif op == '3':
            self.registro.registrar_professor()
        
        elif op == '4':
            self.registro.registrar_monitor()

    def listar(self):
        print('\n[1]- listar pessoas')
        print('[2]- listar estudantes')
        print('[3]- listrar professores')
        print('[4]- listrar monitores')
        op = input('escolha a opção desejada: ')

        if op == '1':
            self.registro.listar_pessoa()
        
        elif op == '2':
            self.registro.listar_estudante()
        
        elif op == '3':
            self.registro.listar_professor()
        
        elif op == '4':
            self.registro.listar_monitor()

    def executar(self):
        while True:
            print('\n[1]- registrar')
            print('[2]- listar')
            op = input('escolha a opção desejada: ')

            if op == '1':
                self.registrar()
            
            elif op == '2':
                self.listar()