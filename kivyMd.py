# from kivymd.app import MDApp
# from kivymd.uix.floatlayout import FloatLayout
# from  kivymd.uix.button import MDRaisedButton

# class MeuApplicativo(MDApp):
#     def build(self):
#         fl = FloatLayout()
#         fl.add_widget(MDRaisedButton(text='clica aqui!'))
#         return fl

# MeuApplicativo().run()


from kivymd.app import MDApp
from kivymd.uix.floatlayout import FloatLayout
from kivy.lang import Builder

KV = '''
MDScreen:
    MDIconButton:
        icon: 'steam'
        pos_hint: {'center_x':.5, 'center_y':.8}
        icon_size: '75sp'

    MDTextField:
        mode: 'round'
        size_hint_x: .6
        pos_hint: {'center_x':.5, 'center_y':.6}
        hint_text: 'email'
        mode: 'fill'
    MDTextField:
        size_hint_x: .6
        mode: 'round'
        pos_hint: {'center_x':.5, 'center_y':.5}
        hint_text: 'password'
        password: 'True'
        mode: 'fill'
        min_text_length: 8
        helper_text: 'minimo 8 caracteres'
 
    MDRaisedButton:
        size_hint_x: .6
        pos_hint:{'center_x':.5, 'center_y':.38}
        md_bg_color: 'blue'
        text: 'login'


'''


class MeuApplicativo(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

MeuApplicativo().run()



#pip install kivymd || kivy