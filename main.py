from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import random


class MainApp(App):
    def build(self):
        layout = GridLayout(cols=10, rows=10)
        self.button_dict = {}
        self.bomb_list = random.sample(range(100), 20)
        for i in range(100):
            button = Button(
                on_release=lambda button_obj, num_button=i: self.click(num_button)
            )
            self.button_dict[f"{i}"] = [button, False]
            layout.add_widget(button)

        return layout

    def click(self, num_button):
        if num_button in self.bomb_list:
            self.button_dict[str(num_button)][0].text = "bomb"
        else:
            self.show(num_button)

    def show(self, num_button):
        self.button_dict[str(num_button)][1] = True
        count_bomb = 0
        adjacentes_esquerda = [
            num_button - 10,
            num_button - 9,
            num_button + 1,
            num_button + 10,
            num_button + 11,
        ]
        adjacentes_meio = [
            num_button - 1,
            num_button - 10,
            num_button - 11,
            num_button - 9,
            num_button + 1,
            num_button + 10,
            num_button + 11,
            num_button + 9,
        ]
        adjacentes_direita = [
            num_button - 1,
            num_button - 10,
            num_button - 11,
            num_button + 10,
            num_button + 9,
        ]
        if num_button % 10 == 0:
            for i in adjacentes_esquerda:
                if i in self.bomb_list and 0 <= i < 100:
                    count_bomb += 1
            self.button_dict[str(num_button)][0].text = f"{count_bomb}"
            if count_bomb == 0:
                for i in adjacentes_esquerda:
                    if 0 <= i < 100 and not self.button_dict[str(i)][1]:
                        self.show(i)

            count_bomb = 0
        elif num_button % 10 == 9:
            for i in adjacentes_direita:
                if i in self.bomb_list and 0 <= i < 100:
                    count_bomb += 1
            self.button_dict[str(num_button)][0].text = f"{count_bomb}"
            if count_bomb == 0:
                for i in adjacentes_direita:
                    if 0 <= i < 100 and not self.button_dict[str(i)][1]:
                        self.show(i)
            count_bomb = 0
        else:
            for i in adjacentes_meio:
                if i in self.bomb_list and 0 <= i < 100:
                    count_bomb += 1
            self.button_dict[str(num_button)][0].text = f"{count_bomb}"
            if count_bomb == 0:
                for i in adjacentes_meio:
                    if 0 <= i < 100 and not self.button_dict[str(i)][1]:
                        self.show(i)
            count_bomb = 0


if __name__ == "__main__":
    MainApp().run()
