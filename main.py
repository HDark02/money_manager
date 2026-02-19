from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.keyboard_anim_args ={'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"
add_money="""
MDScreen:
    name: "ajouter"
    money:money
    expende:expende
    urgent:urgent
    investment:investment
    fun:fun
    MDFloatLayout:
        md_bg_color: "black"
        MDLabel:
            text: "How to use my money"
            theme_text_color: "Custom"
            text_color: "white"
            pos_hint: {"center_x": .5, "center_y": .95}
            halign: "center"
            font_size: "25sp"
        MDFloatLayout:
            md_bg_color: 1, 1, 1, 0.1
            size_hint: .9, .2
            radius: [20, ]
            pos_hint: {"center_x": .5, "center_y": .8}
            MDLabel:
                text: "My money"
                theme_text_color: "Custom"
                text_color: "white"
                pos_hint: {"center_x": .5, "center_y": .85}
                halign: "center"
                font_size: "18sp"
            MDLabel:
                id: money_in
                text: money.text
                theme_text_color: "Custom"
                text_color: "white"
                bold: True
                pos_hint: {"center_x": .5, "center_y": .5}
                halign: "center"
                font_size: "35sp"
            
        MDFloatLayout:
            md_bg_color: "black"
            pos_hint: {"center_x": .5, "top": .7}
            size_hint: 1, .8
            radius: [20, ]
            MDFlatButton:
                text: "Use it like this"
                theme_text_color: "Custom"
                text_color: "white"
                bold: True
                # md_bg_color: 1, 1, 1, 0.2
                size_hint: .8, .08
                pos_hint: {"center_x": .5, "center_y": .8}
                halign: "center"
                font_size: "20sp"
                on_release:
                    app.use_my_money(money.text)
            MDTextField:
                id: money
                hint_text: "Entrez le montant"
                pos_hint: {"center_x": .5, "center_y": .9}
                font_size: "20sp"
                size_hint: .8, .1
                theme_text_color: "Custom"
                mode: "rectangle"
                multiline: True
                hint_text_color_normal: "white"
                hint_text_color_focus: "white"
                # fill_color_focus: 1, 1, 1, 0
                # fill_color_normal: 1, 1, 1, 0
                # text: "good mord"
                text_color_focus: "white"
                text_color_normal: 1, 1, 1, 0.8
                line_color_focus: 1, 1, 1, 1
                line_color_normal: 1, 1, 1, 0.1
            MDLabel:
                text: "XOF"
                theme_text_color: "Custom"
                pos_hint: {"center_x": .8, "center_y": .9}
                text_color: "white"
                halign: "center"
                font_size: "20sp"
        MDGridLayout:
            cols: 2
            rows: 2
            pos_hint: {"center_x": .5, "top": .5}
            # md_bg_color: ("red")
            size_hint: 1, .4
            spacing: 10
            Table_:
                id: expende
                role: "Expende"
                stat: "50%"
                color_in: "red"
            Table_:
                id: urgent
                role: "Urgent"
                stat: "15%"
                color_in: "yellow"
            Table_:
                id: investment
                role: "Investment"
                stat: "25%"
                color_in: "green"
            Table_:
                id: fun
                role: "Fun"
                stat: "10%"
                color_in: "white"

<Table_@MDFloatLayout>:
    role:"role"
    stat:"stat"
    color_in: "red"
    md_bg_color: 1, 1, 1, 0.1
    size_hint: .9, .2
    radius: [20, ]
    pos_hint: {"center_x": .5, "center_y": .8}
    MDLabel:
        text: root.role
        theme_text_color: "Custom"
        text_color: "white"
        pos_hint: {"center_x": .5, "center_y": .85}
        halign: "center"
        font_size: "18sp"
    MDLabel:
        text: root.stat
        theme_text_color: "Custom"
        text_color: root.color_in
        bold: True
        pos_hint: {"center_x": .5, "center_y": .5}
        halign: "center"
        font_size: "35sp"
"""
class Gestion_money(MDApp):
    def build(self):
        global screen
        screen=Builder.load_string(add_money)
        return screen
    def use_my_money(self, money):
        try:
            money= float(money)
            expense=money*(50/100)
            urgent=money*(15/100)
            investment=money*(25/100)
            fun=money*(10/100)
            screen.ids.expende.stat=str(expense)
            screen.ids.urgent.stat=str(urgent)
            screen.ids.investment.stat=str(investment)
            screen.ids.fun.stat=str(fun)
        except:
            pass
    
if __name__=="__main__":
    Gestion_money().run()