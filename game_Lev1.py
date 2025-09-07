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



class Name(MDApp,Screen):
    def build(self):
   
        sane=Middle()
        sane.milld()
    
        self.manager = ScreenManager()
        self.manager.add_widget(Screen(name="main"))
        self.manager.add_widget(Middle(name="middle"))
        
        
        self.curent_player="X"
        leayout=GridLayout(cols=3)
       
        
        layoutjok=GridLayout(cols=1,size_hint=(0.5,0.2),spacing=44,pos_hint={'x': 0.05})
        
        layout2=BoxLayout(orientation='vertical')
        button2=MDIconButton(icon = "restore",md_bg_color="red",on_press=self.rest_game)
    
        
       

   
        
        layoutjok.add_widget(button2)
    

        
        layout2.add_widget(layoutjok)

        
       
        self.buttons= [[None] *3 for _ in range(3)]
        
        
        for row in range(3):
            for col in range(3):
                button=MDRectangleFlatButton(font_size=60, size_hint=(100, 100))
                button.bind(on_press=self.on_press_button)
                self.buttons[col][row] = button
                leayout.add_widget(button)
             
        layout2.add_widget(leayout)   
        layout3=BoxLayout(size_hint=(0.2, 0.2))  
        layout2.add_widget(layout3)  
         
        return layout2
    
    
    
    def on_press_button(self, button):
        if button.text == "":
            button.text = self.curent_player
            
            if self.change_winer():
                self.show_popup(f"player {self.curent_player} deowr!")
                return
            elif all(button.text != "" for row in self.buttons for button in row):
                self.show_popup("It s a Deowr!")
            self.curent_player = "O" if self.curent_player == "X" else "X"
            if self.curent_player == "O":
                button.text_color=(1,0,0,1)
            else:
                button.text_color=(0,0,1,1)
            
            
    def change_winer(self):
        for row in self.buttons:
            if row[0].text == row[1].text == row[2].text !="":
                return True
        for col in range(3):
            if self.buttons[0][col].text == self.buttons[1][col].text == self.buttons[2][col].text !="":
                return True
        if self.buttons[0][0].text == self.buttons[1][1].text == self.buttons[2][2].text !="":
            return True

        if self.buttons[0][2].text==self.buttons[1][1].text == self.buttons[2][0].text !="":
            return True
        return False
    def show_popup(self, masage):
        popup=Popup(title="Game Over",background_color=(1,0,0,1),
                    content=Label(text=masage),
                    size_hint=(0.9 , 0.3))
        popup.open()
        popup.bind(on_dismiss=self.rest_game)
                    
    def rest_game(self, args):
        self.curent_player = "X"
        for row  in self.buttons:
            for button in row:
                button.text = ""     
 

class Middle(Screen):   
    
        
    def milld(self):
      
       
        print("sane")   
        self.curent_play="X"
            
        layout=GridLayout(cols=4)
        self.buttons=[[None] * 4 for _ in range(4)]
        for row in range(4):
            for col in range(4):
                buttonlv2=MDRectangleFlatButton(font_size=40,on_press=self.on_button)
                
                self.buttons[col][row] = buttonlv2
                layout.add_widget(buttonlv2)
        return layout
    def on_button(self,buttonlv2):
        if buttonlv2.text =="":
            buttonlv2.text = self.curent_play
            if self.cha_wine_mid(self):
                self.show_popup_mud(f"player {self.curent_play} diner!")
            elif all(buttonlv2.text != "" for row in self.buttons for buttonlv2 in row):
                self.show_popup_mud("It s Dirw!")
            self.curent_play = "O" if self.curent_play == "X" else "X"
                
                
        
        
  

    
Name().run()
              