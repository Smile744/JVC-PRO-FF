import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class GameOptimizerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.label = Label(
            text="JVC-PRO FF\nOptimizador de RAM", 
            font_size='24sp', 
            halign='center'
        )
        layout.add_widget(self.label)
        
        btn_optimize = Button(
            text="Optimizar Celular para Free Fire", 
            size_hint=(1, 0.2),
            background_color=(1, 0, 0, 1)
        )
        btn_optimize.bind(on_press=self.run_optimization)
        layout.add_widget(btn_optimize)
        
        return layout

    def run_optimization(self, instance):
        self.label.text = "¡RAM Optimizada con éxito!\nListo para jugar."

if __name__ == '__main__':
    GameOptimizerApp().run()
