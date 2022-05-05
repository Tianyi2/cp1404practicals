from kivy.app import App
from kivy.lang import Builder


class ConvertMilesKmDemo(App):
    def build(self):
        self.title = "Convert Miles Km Demo"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesKmDemo().run()
