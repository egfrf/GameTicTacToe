from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton , MDIconButton , MDRaisedButton
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder

Window.size=(400 , 600)

class Name(MDApp):
    def build(self):
        
        
        layout2=BoxLayout(orientation='vertical')
        button2=MDIconButton(icon="restore",on_press=self.rest_game)
      
        
    
        
        
        layout3=GridLayout(cols=1,size_hint=(0.2,0.2),spacing=30,pos_hint={'x': 0.02 , "y": 0.5})
        layout2.add_widget(layout3)
        
        
        layout3.add_widget(button2)
        
        
        
        
        
        self.curent_player="O"
        layout=GridLayout(cols=6,size_hint=(0.3,0.7),pos_hint={'x': 0.02 , "y": 0.2})
        self.buttons=[[None] *6 for _ in range(6)]
        
        for row in range(6):
            for col in range(6):
                button=MDRectangleFlatButton(font_size=40,size_hint=(200,380),on_press=self.press_but)
                button.bind()
                self.buttons[row][col]= button
                
                layout.add_widget(button)
                
      
      
        layout3.add_widget(layout) 
        
        layout55=BoxLayout(size_hint=(0.0, 0.05))
        layout2.add_widget(layout55) 
        
        
        return layout2
    
    def press_but(self, button):
        if button.text == "":
            button.text = self.curent_player
            if self.change_winner():
                self.show_popup(f"player ({self.curent_player}) Winner! ")
            elif all(button.text !="" for row in self.buttons for button in row):
                self.show_popup("The game ended in a draw!..")   
            self.curent_player ="X" if self.curent_player == "O" else "O"   
            
            if self.curent_player == "X":
                button.text_color=(1,0,0,1)
               
            else:
                button.text_color=(0,0,1,1)
             
            
    def change_winner(self):
        for row in self.buttons:
            if row[0].text == row[1].text== row[2].text == row[2].text == row[3].text == row[4].text==row[5].text !="":
                return True
        for col in range(6):
            if self.buttons[0][col].text == self.buttons[1][col].text == self.buttons[2][col].text == self.buttons[3][col].text == self.buttons[4][col].text == self.buttons[5][col].text !="":
                return True
        if self.buttons[0][0].text ==self.buttons[1][1].text == self.buttons[2][2].text == self.buttons[3][3].text == self.buttons[4][4].text == self.buttons[5][5].text !="":
            return True
        
        if self.buttons[5][0].text ==self.buttons[4][1].text == self.buttons[3][2].text == self.buttons[2][3].text == self.buttons[1][4].text == self.buttons[0][5].text !="":
            return True
        return False
    def show_popup(self,masage):
        popup=Popup(title="Over Game",
                    content=Label(text=masage),size_hint=(0.7, 0.3))
        popup.open()
        popup.bind(on_dismiss=self.rest_game)
        
    def rest_game(self, *args):
        self.curent_player ="O"
        for row in self.buttons:
            for button in row:
                button.text = ""
                
    
Name().run()