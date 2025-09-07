from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton , MDIconButton , MDRaisedButton
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder


Window.size=(410 , 600)

class Namelev2(MDApp):
    def build(self):

        self.curent_player="X"
        layoutjok=GridLayout(cols=3,size_hint=(0.5,0.2),spacing=44,pos_hint={'x': 0.05 , "y": 0.5})
        
        layout2=BoxLayout(orientation='vertical')
        button2=MDIconButton(icon = "restore",md_bg_color="red",on_press=self.rest_game)

        

        layoutjok.add_widget(button2)

   
        
        layout2.add_widget(layoutjok)
        
        
        
        layout=GridLayout(cols=4,size_hint=(0.99, 0.7),pos_hint={'x': 0.0, 'y': 0.1})
        self.buttons=[[None] * 4 for _ in range(4)]
        
      
        
        for row in range(4):
            for col in range(4):
                button=MDRectangleFlatButton(font_size=50, size_hint=(220, 200),on_press=self.press_button)
                button.bind()
                self.buttons[col][row] = button
                layout.add_widget(button)
       
        
        layout2.add_widget(layout) 
        layout3=BoxLayout(size_hint=(0.0, 0.5))
        layout2.add_widget(layout3) 
        return layout2
    
    
    def press_button(self, button):
        if button.text == "":
            button.text = self.curent_player
            
            if self.change_winner():
                self.show_popup(f"player {self.curent_player} Winer!")
            elif all(button.text !="" for row in self.buttons  for button in row):
                self.show_popup("It s a Dirwer!")
            
            self.curent_player = "O" if self.curent_player == "X" else "X"
            if self.curent_player == "O":
                button.text_color=(1,0,0,1)
            else:
                button.text_color=(0,0,1,1)
    
    def change_winner(self):
        for row in self.buttons:
            if row[0].text == row[1].text == row[2].text == row[3].text!="":
                return True
            
        for col in range(4):
            if self.buttons[0][col].text == self.buttons[1][col].text == self.buttons[2][col].text == self.buttons[3][col].text!="":
                return True
            
        if self.buttons[0][0].text == self.buttons[1][1].text == self.buttons[2][2].text == self.buttons[3][3].text !="":
            return True
        
        if self.buttons[3][0].text == self.buttons[2][1].text == self.buttons[1][2].text == self.buttons[0][3].text !="":
            return True
        return False
            
            
    def show_popup(self,masage):
        popup=Popup(title="Game_over!",
                    size_hint=(0.7,0.3),
                    content=Label(text=masage))
        popup.open()
        popup.bind(on_dismiss=self.rest_game)
        
    def rest_game(self, *args):
        self.curent_player = "X"
        for row in self.buttons:
            for button in row:
                button.text = ""
    
        
        
Namelev2().run()
