import kivy
kivy.require('1.5.2')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from random import choice, randint

signs = ("O", "X")
conditions = ((1,2,3),(4,5,6),(7,8,9),
              (3,5,7),(1,5,9),
              (1,4,7),(2,5,8),(3,6,9))

class ShowPopup(Popup): 
    def __init__(self, baslik, mesaj, **kwargs):
        self.size_hint_x = self.size_hint_y = .5
        self.title = baslik
        super(ShowPopup, self).__init__(**kwargs)
        self.add_widget(Button(text=mesaj, on_press=lambda x:self.dismiss()))
        self.open()

class TicTacToe(GridLayout):
    def __init__(self, **kwargs):
        self.cols = 3
        self.rows = 3
        super(TicTacToe, self).__init__(**kwargs)
        for _ in range(9):
            self.add_widget(Button(font_size=100, on_press=self.button_pressed))

    def show_draw_popup(self):
        ShowPopup('Игра окончена', 'Ничья!')
    
    def reset(self):
        for child in self.children:
            child.text = ''
            child.background_color = (1, 1, 1, 1)
            
    def recolorize(self):
        colors = {signs[0]: (255,0,0,255),
                  signs[1]: (0,0,255,255),
                  ''      : (1,1,1,1)}
        for child in self.children:
            child.background_color = colors[child.text]
            
    def after_move(self):
        # 0 = Continue
        # 1 = Win
        # 2 = Draw 
        status_code = 0
        table = list(map(lambda x : x.text, self.children))
        for s in signs:
            for cond in conditions:             
                if all(list(map(lambda x : table[x-1] == s, cond))):
                    status_code = 1

        if '' not in table and status_code != 1:
            status_code = 2
        self.recolorize()
        return status_code
    
    def opponent_move(self):
        def get_signs(*cond):
            return [self.children[i-1].text for i in cond]
        def make_a_move():
            for i in range(2):
                for s in signs:
                    for cond in conditions:
                        cond_signs = get_signs(*cond)
                        if cond_signs.count(s) == 2 and '' in cond_signs and i == 0:
                            return cond[cond_signs.index('')]
                        elif cond_signs.count(s) == 1 and cond_signs.count('') == 2 and i == 1:
                            return cond[choice([j for j in range(3) if j != cond_signs.index(s)])]
            while True:
                r = randint(0,8)
                if self.children[r].text == '':
                    return r+1
        move = make_a_move()
        self.children[move-1].text = signs[0]
        status_code = self.after_move()
        if status_code == 1:
            ShowPopup('Игра окончена!', 'Ты проиграл!')
        elif status_code == 2:
            self.show_draw_popup()
        if status_code in (1,2):
            self.reset()
            return
    
    def button_pressed(self, w):
        if w.text:
            ShowPopup('Ошибка!', "Здесь уже есть знак!")
            return
        w.text = signs[1]
        status_code = self.after_move()
        if status_code == 1:
            ShowPopup('Игра окончена!', 'Поздравляем! Вы выиграли!')
        elif status_code == 2:
            self.show_draw_popup()
        if status_code in (1,2):
            self.reset()
            return
        self.opponent_move()
        
class TheGame(App):
    def build(self):
        self.title = 'Tic-Tac-Toe'
        return TicTacToe()

if __name__ == '__main__':
    TheGame().run()