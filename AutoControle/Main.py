from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
import os
import psutil
from datetime import datetime
from kivy.uix.image import Image
from kivy.uix.popup import Popup
import threading
import time

__Name__ = 'AutoControle'
__Author__ = "Rafael Moraes De Oliveira"
__Date__ = "Segunda-Feira (14\10\2024)"

dia = str(datetime.now().day)
mês = str(datetime.now().month)
ano = str(datetime.now().year)

horas = datetime.now().hour
minutos = datetime.now().minute
segundos = datetime.now().second

Gui = Builder.load_string("""
<Menu>:
    ScrollView:
        size_hint_y:None
        height:1390
        BoxLayout:
            orientation:'vertical'
            size_hint_y:None
            height:1985
            ActionBar:
                ActionView:
                    ActionPrevious:
                        title:'Sair'
                        on_press:root.sair()
            Label:
                text:''
                size_hint_y:None
                height:100
            Label:
                text:'Auto-Controle'
                size_hint_y:None
                height:100
                font_size:30
                color:0,1,0,1
            Label:
                text:''
                size_hint_y:None
                height:200
            Image:
                source:r'C:\\Users\\us\\Downloads\\atenção.png'
                size_hint_y:None
                height:100
            Label:
                text:''
                size_hint_y:None
                height:100
            Button:
                text:'Registro'
                size_hint_y:None
                height:80
                background_color:0,1,0,1
                on_press:root.manager.current = 'registro'


            Label:
                text:''
                size_hint_y:None
                height:100
            Button:
                text:'Bloquear: App'
                size_hint_y:None
                height:80
                on_press:root.manager.current = 'bloquearapp'
                background_color:0,1,0,1
            Label:
                text:''
                size_hint_y:None
                height:100
            Button:
                text:'Bloquear: Sites'
                size_hint_y:None
                height:80
                background_color:0,1,0,1
                on_press:root.manager.current = 'bloqueiodesite'
            Label:
                text:''
                size_hint_y:None
                height:200








<Registrar>:
    ScrollView:
        size_hint: 1, None  # Ajusta a largura para ocupar a tela toda e a altura pode ser controlada
        height: 630  # Isso pode ser alterado de acordo com a necessidade
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 900
            ActionBar:
                ActionView:
                    ActionPrevious:
                        title: 'Voltar'
                        on_press: root.manager.current = 'registro'
            Label:
                text: ''
                size_hint_y: None
                height: 100
            Label:
                text: 'Auto-Controle'
                size_hint_y: None
                height: 100
                font_size: 40
                color: 0, 1, 0, 1
            Label:
                text: ''
                size_hint_y: None
                height: 200
            Label:
                text: "Você superou este dia? "
                size_hint_y: None
                height: 100
            Label:
                text: ''
                size_hint_y: None
                height: 100
            BoxLayout:
                orientation: 'horizontal'
                size_hint_x: None
                width: 100
                Label:
                    text: ''
                    size_hint_x: None
                    width: 250
                Button:
                    text: 'Sim'
                    size_hint_y: None
                    height: 100
                    size_hint_x: None
                    width: 100
                    background_color: 0, 1, 0, 1
                    on_press: root.mudar()
                Label:
                    text: ''
                    size_hint_x: None
                    width: 300
                Button:
                    text: 'Não'
                    size_hint_y: None
                    height: 100
                    size_hint_x: None
                    width: 100
                    background_color: 3, 0, 1, 2
                    on_press: root.apagar()
            Label:
                text:''
                size_hint_y:None
                height:100

<Dia_Registrado>:
    ScrollView:
        size_hint_y:None
        height:1390
        BoxLayout:
            orientation:'vertical'
            size_hint_y:None
            height:1250
            ActionBar:
                ActionView:
                    ActionPrevious:
                        title:'Menu'
                        on_press:root.manager.current = 'registro'
            Label:
                text:''
                size_hint_y:None
                height:400
            Label:
                text:'Dia Registrado Com Sucesso'
                size_hint_y:None
                height:100
                font_size:40
                color:0,1,0,1



<Aviso>:
    ScrollView:
        size_hint_y:None
        height:1390
        BoxLayout:
            orientation:'vertical'
            size_hint_y:None
            height:1250
            ActionBar:
                ActionView:
                    ActionPrevious:
                        title:'Menu'
                        on_press:root.manager.current = 'registro'
            Label:
                text:''
                size_hint_y:None
                height:400
            Label:
                text:'Você ainda não superou nenhum dia!'
                size_hint_y:None
                height:100
                font_size:40
                color:0,1,0,1


<Dia_Eliminado>:
    ScrollView:
        size_hint_y:None
        height:1390
        BoxLayout:
            orientation:'vertical'
            size_hint_y:None
            height:1250
            ActionBar:
                ActionView:
                    ActionPrevious:
                        title:'Menu'
                        on_press:root.manager.current = 'registro'
            Label:
                text:''
                size_hint_y:None
                height:400
            Label:
                text:'Dia Eliminado Com Sucesso'
                size_hint_y:None
                height:100
                font_size:40
                color:0,1,0,1


<Alerta>:
    ScrollView:
        size_hint_y:None
        height:1390
        BoxLayout:
            orientation:'vertical'
            size_hint_y:None
            height:1250
            ActionBar:
                ActionView:
                    ActionPrevious:
                        title:'Menu'
                        on_press:root.manager.current = 'registro'
            Label:
                text:''
                size_hint_y:None
                height:400
            Label:
                text:'Você já registrou esse dia!'
                size_hint_y:None
                height:100
                font_size:40
                color:0,1,0,1


<Historico>:
    ScrollView:
        size_hint_y:None
        height:1390
        BoxLayout:
            orientation:'vertical'
            size_hint_y:None
            height:2750
            ActionBar:
                ActionView:
                    ActionPrevious:
                        title:'Menu'
                        on_press:root.manager.current = 'registro'
            Label:
                text:''
                size_hint_y:None
                height:200
            Label:
                text:'HISTORICO'
                size_hint_y:None
                height:100
                font_size:40
                color:0,1,0,1
            Label:
                text:''
                size_hint_y:None
                height:100
            Label:
                text:''
                size_hint_y:None
                height:400
            ScrollView:
                size_hint_y:None
                height:800
                Label:
                    id:diasregistrados
                    text:''
                    size_hint_y:None
                    height:1200
            Label:
                text:''
                size_hint_y:None
                height:200
            Label:
                id:total
                text:''
                size_hint_y:None
                height:100
            Label:
                text:''
                size_hint_y:None
                height:100


<Blocklist>:
    ScrollView:
        size_hint_y:None
        height:1390
        BoxLayout:
            id:box
            orientation:'vertical'
            size_hint_y:None
            height:2350
            ActionBar:
                ActionView:
                    ActionPrevious:
                        title:'Menu'
                        on_press:root.manager.current = 'bloquearapp'
            Label:
                text:''
                size_hint_y:None
                height:200
            Label:
                text:'Blocklist'
                size_hint_y:None
                height:100
                font_size:40
                color:0,1,0,1
            Label:
                text:''
                size_hint_y:None
                height:300
            ScrollView:
                size_hint_y:None
                height:1000
                BoxLayout:
                    orientation:'vertical'
                    size_hint_y:None
                    height:4000
                    Label:
                        id:programa
                        text:''
                        size_hint_y:None
                        height:4000
                        background_color:0,1,0,1

<Bloqueio>:
    ScrollView:
        size_hint_y:None
        height:1390
        BoxLayout:
            orientation:'vertical'
            size_hint_y:None
            height:1500
            ActionBar:
                ActionView:
                    ActionPrevious:
                        title:'Menu'
                        on_press:root.manager.current = 'bloquearapp'
            Label:
                text:''
                size_hint_y:None
                height:200
            Label:
                text:'Lista De Bloqueio'
                size_hint_y:None
                height:100
                font_size:40
                color:0,1,0,1
            Label:
                text:''
                size_hint_y:None
                height:100

            TextInput:
                id:texto
                text:'Digite o nome do aplicativo que você deseja bloquear'
                size_hint_y:None
                height:100
                multiline:False
                on_focus:root.apagar()
            Label:
                text:''
                size_hint_y:None
                height:100
            Button:
                text:'Adicionar'
                size_hint_y:None
                height:100
                on_press:root.adicionar()


<Alterar_Bloqueio>:
    ScrollView:
        size_hint_y:None
        height:1390
        BoxLayout:
            orientation:'vertical'
            size_hint_y:None
            height:1550
            ActionBar:
                ActionView:
                    ActionPrevious:
                        title:'Menu'
                        on_press:root.manager.current = 'bloquearapp'
            Label:
                text:''
                size_hint_y:None
                height:200
            Label:
                text:'Alterar Lista De Bloqueio'
                size_hint_y:None
                height:100
                font_size:40
                color:0,1,0,1
            Label:
                text:''
                size_hint_y:None
                height:100

            TextInput:
                id:texto
                text:'''Digite o nome do aplicativo que você deseja remover da lista de bloqueio'''
                size_hint_y:None
                height:100
                multiline:False
                on_focus:root.limpar()
            Label:
                text:''
                size_hint_y:None
                height:100
            Button:
                text:'Remover'
                size_hint_y:None
                height:100
                on_press:root.remover()


<Bloquear_Site>:
    ScrollView:
        size_hint_y:None
        height:1390
        BoxLayout:
            orientation:'vertical'
            size_hint_y:None
            height:850
            ActionBar:
                ActionView:
                    ActionPrevious:
                        title:'Menu'
                        on_press:root.manager.current = 'menu'
            Label:
                text:''
                size_hint_y:None
                height:200
            Label:
                text:'Lista De Bloqueio'
                size_hint_y:None
                height:100
                font_size:40
                color:0,1,0,1
            Label:
                text:''
                size_hint_y:None
                height:100

            TextInput:
                id:texto
                text:'Digite o nome do site que você deseja bloquear'
                size_hint_y:None
                height:100
                multiline:False

            Label:
                text:''
                size_hint_y:None
                height:100
            Button:
                text:'Adicionar'
                size_hint_y:None
                height:100


<Alterar_Bloqueio_Site>:
    ScrollView:
        size_hint_y:None
        height:1390
        BoxLayout:
            orientation:'vertical'
            size_hint_y:None
            height:850
            ActionBar:
                ActionView:
                    ActionPrevious:
                        title:'Menu'
                        on_press:root.manager.current = 'menu'
            Label:
                text:''
                size_hint_y:None
                height:200
            Label:
                text:'Alterar Lista De Bloqueio'
                size_hint_y:None
                height:100
                font_size:40
                color:0,1,0,1
            Label:
                text:''
                size_hint_y:None
                height:100

            TextInput:
                id:texto
                text:'''Digite o nome do site que você deseja remover da lista de bloqueio'''
                size_hint_y:None
                height:100
                multiline:False

            Label:
                text:''
                size_hint_y:None
                height:100
            Button:
                text:'Remover'
                size_hint_y:None
                height:100


<Registro>:
    ScrollView:
        size_hint_y:None
        height:1390
        BoxLayout:
            orientation:'vertical'
            size_hint_y:None
            height:1940
            ActionBar:
                ActionView:
                    ActionPrevious:
                        title:'Voltar'
                        on_press:root.manager.current = 'menu'
            Label:
                text:''
                size_hint_y:None
                height:100
            Label:
                text:'Registros'
                size_hint_y:None
                height:100
                font_size:30
                color:0,1,0,1
            Label:
                text:''
                size_hint_y:None
                height:200
            Image:
                source:r'C:\\Users\\us\\Downloads\\atenção.png'
                size_hint_y:None
                height:100
            Label:
                text:''
                size_hint_y:None
                height:150
            Button:
                text:'Registrar Dia'
                size_hint_y:None
                height:80
                background_color:0,1,0,1
                on_press:root.manager.current = 'registrar'
            Label:
                text:''
                size_hint_y:None
                height:100
            Button:
                text:'Historico'
                size_hint_y:None
                height:80
                background_color:0,1,0,1
                on_press:root.manager.current = 'historico'
            Label:
                text:''
                size_hint_y:None
                height:100
            Button:
                text:'Recorde'
                size_hint_y:None
                height:80
                background_color:0,1,0,1
            Label:
                text:''
                size_hint_y:None
                height:100

<Bloquear_App>:
    ScrollView:
        size_hint_y:None
        height:1390
        BoxLayout:
            orientation:'vertical'
            size_hint_y:None
            height:1880
            ActionBar:
                ActionView:
                    ActionPrevious:
                        title:'Voltar'
                        on_press:root.manager.current = 'menu'
            Label:
                text:''
                size_hint_y:None
                height:100
            Label:
                text:'Bloquear App'
                size_hint_y:None
                height:100
                font_size:30
                color:0,1,0,1
            Label:
                text:''
                size_hint_y:None
                height:200
            Image:
                source:r'C:\\Users\\us\\Downloads\\atenção.png'
                size_hint_y:None
                height:100
            Label:
                text:''
                size_hint_y:None
                height:100
            Button:
                text:'Lista De Bloqueio'
                size_hint_y:None
                height:80
                background_color:0,1,0,1
                on_press:root.manager.current = 'blocklist'
            Label:
                text:''
                size_hint_y:None
                height:100
            Button:
                text:'Bloquear Programas'
                size_hint_y:None
                height:80
                background_color:0,1,0,1
                on_press:root.manager.current = 'bloqueio'
            Label:
                text:''
                size_hint_y:None
                height:100
            Button:
                text:'Alterar Lista de bloqueio: Programas'
                size_hint_y:None
                height:80
                background_color:0,1,0,1
                on_press:root.manager.current = 'alterarbloqueio'
            Label:
                text:''
                size_hint_y:None
                height:100


<Bloqueio_De_Site>:
    ScrollView:
        size_hint_y:None
        height:1390
        BoxLayout:
            orientation:'vertical'
            size_hint_y:None
            height:1980
            ActionBar:
                ActionView:
                    ActionPrevious:
                        title:'Voltar'
                        on_press:root.manager.current = 'menu'
            Label:
                text:''
                size_hint_y:None
                height:100
            Label:
                text:'Bloqueio De Sites'
                size_hint_y:None
                height:100
                font_size:30
                color:0,1,0,1
            Label:
                text:''
                size_hint_y:None
                height:200
            Image:
                source:r'C:\\Users\\us\\Downloads\\atenção.png'
                size_hint_y:None
                height:100
            Label:
                text:''
                size_hint_y:None
                height:100
            Button:
                text:'Bloquear Sites'
                size_hint_y:None
                height:80
                background_color:0,1,0,1
            Label:
                text:''
                size_hint_y:None
                height:100
            Button:
                text:'Lista de Bloqueio'
                size_hint_y:None
                height:80
                background_color:0,1,0,1
            Label:
                text:''
                size_hint_y:None
                height:100
            Button:
                text:'Alterar Lista de Bloqueio: Sites'
                size_hint_y:None
                height:80
                background_color:0,1,0,1

            Label:
                text:''
                size_hint_y:None
                height:200


""")

conta = 0


class Menu(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)
        self.block_thread = None
        self.blocking_event = threading.Event()  # Controle de evento para a thread de bloqueio

    def block_app(self, app_name):
        # Função para bloquear o app
        while not self.blocking_event.is_set():  # A thread continua rodando enquanto o evento não for sinalizado
            for process in psutil.process_iter(attrs=['pid', 'name']):
                try:
                    if app_name.lower() in process.info['name'].lower():
                        # Fecha o processo
                        print(f'Bloqueando {process.info["name"]} com PID {process.info["pid"]}')
                        psutil.Process(process.info['pid']).terminate()
                except (psutil.NoSuchProcess, psutil.AccessDenied,
                        psutil.ZombieProcess):
                    pass
            time.sleep(1)  # Atraso para evitar uso excessivo da CPU, ajustável conforme necessidade

    def on_pre_enter(self):
        os.chdir(r'C:\Users\us\PycharmProjects\pythonProject\Autocontrole\Marcador')

        lista = os.listdir()

        for teste in range(0, len(lista)):
            os.chdir(lista[teste])
            file = open("data", "r")
            texto = file.read()
            file.close()

            if dia + '/' + mês + '/' + ano in texto:
                pass
                os.chdir('..')
            else:
                os.remove('data')
                os.chdir('..')
                os.rmdir(lista[teste])
                print('Eliminado')

                os.chdir('../Black List')
                lista2 = os.listdir()
                file = open('arquivo', 'r')
                texto = file.read()
                file.close()

                file = open('arquivo', 'w')
                file.write(texto.replace(lista[teste], ''))
                file.close()

                for contador in range(1, len(lista2)):
                    file = open(lista2[contador], 'r')
                    leitor = file.read()
                    file.close()

                    if lista[teste] in leitor:
                        os.remove(lista2[contador])
                    else:
                        pass

                os.chdir('../Marcador')
        Menu.start_blocking_thread(self)

    def start_blocking_thread(self):
        # Cria e inicia a thread para bloquear apps
        os.chdir(r'C:\Users\us\PycharmProjects\pythonProject\Autocontrole\Black list')
        lista = len(os.listdir())

        for contador in range(1, lista + 1):
            try:
                file = open(str(contador), 'r')
            except:
                pass
            else:
                texto = file.read()
                file.close()

                # Cria a thread de bloqueio para cada app da lista de bloqueio
                blocking_thread = threading.Thread(target=self.block_app, args=(texto,))
                blocking_thread.daemon = True  # A thread será terminada automaticamente quando o programa principal terminar
                blocking_thread.start()

        # Marca que o evento de bloqueio está ativo
        self.blocking_event.clear()

    def registrar(self):
        dia = str(datetime.now().day)
        mês = str(datetime.now().month)
        ano = str(datetime.now().year)

        file = open(r'C:\Users\us\PycharmProjects\pythonProject\Autocontrole\Registro\dia.py', 'w')
        file.write('''{} {} {}'''.format(dia, mês, ano))
        file.close()

    def sair(self):
        pop1 = BoxLayout(orientation='horizontal')
        sim = Button(text='Sim', size_hint_y=None, height=100)
        sim.bind(on_press=self.encerrar)
        espaço = Label(text='', size_hint_x=None, width=40)
        não = Button(text='Não', size_hint_y=None, height=100)
        não.bind(on_press=self.desaparecer)

        pop1.add_widget(sim)
        pop1.add_widget(espaço)
        pop1.add_widget(não)

        self.pop = Popup(title='Você realmente quer Sair?',
                         content=pop1, size_hint_y=None, height=300)
        self.pop.open()

    def encerrar(self, instance):
        self.blocking_event.set()  # Sinaliza o término da thread de bloqueio
        exit()

    def desaparecer(self, instance):
        self.pop.dismiss()


class Registrar(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)

    def mudar(self):
        os.chdir(r'C:\Users\us\PycharmProjects\pythonProject\Autocontrole\Dias')
        caminho = os.getcwd()
        lista = os.listdir()

        file = open('registros', 'r')
        texto = file.read()
        file.close()

        if str(dia) + '/' + str(mês) + '/' + str(ano) in texto:
            self.manager.current = 'alerta'
        else:
            file = open('registros', 'w')
            texto = file.write("""
{} 

{:^60}

{}/{}/{}

{:^60}

{}:{}:{}



""".format(texto, 'Data', str(dia), str(mês), str(ano), 'Horário', str(horas), str(minutos), str(segundos)))
            self.manager.current = 'diaregistrado'

    def apagar(self):
        os.chdir(r'C:\Users\us\PycharmProjects\pythonProject\Autocontrole\Dias')
        caminho = os.getcwd()
        lista = os.listdir()

        file = open('registros', 'r')
        texto = file.read()
        file.close()

        if len(texto) == 0:
            self.manager.current = 'aviso'
        else:
            file = open('registros', 'w')
            file.write('')
            file.close()

            self.manager.current = 'diaeliminado'


class Dia_Registrado(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)


class Aviso(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)


class Alerta(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)


class Dia_Eliminado(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)


class Blocklist(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)

        self.conta = 0

    def on_pre_enter(self):
        self.conta += 1

        os.chdir(r'C:\Users\us\PycharmProjects\pythonProject\Autocontrole\Black list')

        lista = len(os.listdir())

        file = open('arquivo', 'r')
        texto = file.read()
        file.close()

        self.ids.programa.text = texto


class Recorde(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)


class Bloqueio(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)

    def apagar(self):
        if self.ids.texto.focus:
            self.ids.texto.text = ''

    def adicionar(self):
        os.chdir(r'C:\Users\us\PycharmProjects\pythonProject\Autocontrole\Black list')

        lista = len(os.listdir())

        if self.ids.texto.text == '':
            self.ids.texto.text = 'Digite o nome'
            pass
        else:
            file = open('arquivo', 'r')
            texto = file.read()
            file.close()

            if self.ids.texto.text in texto:
                self.ids.texto.text = 'Esse App já está bloqueado'
            else:
                file = open(str(int(lista + 1)), 'w')
                file.write(self.ids.texto.text)
                file.close()

                file = open('arquivo', 'r')
                texto = file.read()
                file.close()

                file = open('arquivo', 'w')
                file.write("""

{}

{}

            """.format(texto.strip(), self.ids.texto.text.strip()))
                file.close()
                self.ids.texto.text = 'App adicionado a lista'


class Historico(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)

    def on_pre_enter(self):
        os.chdir(r'C:\Users\us\PycharmProjects\pythonProject\AutoControle\Dias')
        caminho = os.getcwd()
        lista = os.listdir()

        file = open('registros', 'r')
        texto = file.read()
        file.close()

        contador = texto.count('Data')

        self.ids.diasregistrados.text = texto

        self.ids.total.text = """


{:^60}

{}

""".format('Dias Superados', str(contador))


class Alterar_Bloqueio(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)

    def limpar(self):
        if self.ids.texto.focus:
            self.ids.texto.text = ""

    def remover(self):
        os.chdir(r'C:\Users\us\PycharmProjects\pythonProject\Autocontrole\Marcador')

        try:
            os.mkdir(self.ids.texto.text)
        except:
            self.ids.texto.text = 'Já está na lista de exclusão'
        else:
            os.chdir(self.ids.texto.text)

            dia2 = int(dia) + 1
            mês2 = int(mês) + 1
            ano2 = int(ano) + 1

            file = open('data', 'w')
            file.write("""

{}/{}/{}

{}:{}:{}

""".format(dia, mês, ano, horas, minutos, segundos))
            file.close()


class Bloquear_Site(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)


class Alterar_Bloqueio_Sites(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)


class Registro(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)


class Bloquear_App(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)


class Bloqueio_De_Site(Screen):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name="menu"))
        sm.add_widget(Registrar(name='registrar'))
        sm.add_widget(Dia_Registrado(name='diaregistrado'))
        sm.add_widget(Aviso(name='aviso'))
        sm.add_widget(Dia_Eliminado(name='diaeliminado'))
        sm.add_widget(Alerta(name='alerta'))
        sm.add_widget(Historico(name='historico'))
        sm.add_widget(Blocklist(name='blocklist'))
        sm.add_widget(Bloqueio(name='bloqueio'))
        sm.add_widget(Alterar_Bloqueio(name='alterarbloqueio'))
        sm.add_widget(Bloquear_Site(name='bloquearsites'))
        sm.add_widget(Alterar_Bloqueio_Sites(name='alterarbloqueiosites'))
        sm.add_widget(Recorde(name='recorde'))
        sm.add_widget(Registro(name='registro'))
        sm.add_widget(Bloquear_App(name='bloquearapp'))
        sm.add_widget(Bloqueio_De_Site(name='bloqueiodesite'))
        return sm


MyApp().run()