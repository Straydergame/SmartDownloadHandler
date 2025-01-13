from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

# Set the window size to 1080x1920 (portrait mode)
Window.size = (1080, 1920)

class SmartDownloadHandler(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Presplash image as background
        self.presplash_image = Image(source='data/presplash.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.presplash_image)

        # Input field
        self.input_field = TextInput(
            hint_text="Enter file name to search",
            size_hint=(.8, None),
            height=40,
            pos_hint={"center_x": .5, "center_y": .5},
            multiline=False
        )
        self.add_widget(self.input_field)

        # Search button
        self.search_button = Button(
            text="Search",
            size_hint=(.3, None),
            height=40,
            pos_hint={"center_x": .5, "center_y": .4}
        )
        self.search_button.bind(on_press=self.on_search_button_press)
        self.add_widget(self.search_button)

        # Alert label for messages
        self.alert_label = Label(
            text="",
            markup=True,
            size_hint=(None, None),
            size=(600, 50),
            pos_hint={"center_x": .5, "center_y": .45},
            font_size='24sp',
            bold=True
        )
        self.add_widget(self.alert_label)

    def on_search_button_press(self, instance):
        file_name = self.input_field.text.strip()
        if not file_name:
            self.alert_label.text = "[color=ff0000]Enter file name to search![/color]"
        else:
            # Example logic to check if file exists (to be replaced with actual logic)
            if file_name == "example.txt":
                self.alert_label.text = "[color=00ff00]File found![/color]"
                self.show_file_options_popup()
            else:
                self.alert_label.text = "[color=ff0000]File doesn't exist![/color]"

    def show_file_options_popup(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Open File button
        open_file_button = Button(text="Open File", size_hint=(1, None), height=40)
        open_file_button.bind(on_press=self.open_file)
        layout.add_widget(open_file_button)

        # Open File Location button
        open_location_button = Button(text="Open File Location", size_hint=(1, None), height=40)
        open_location_button.bind(on_press=self.open_file_location)
        layout.add_widget(open_location_button)

        # Cancel button
        cancel_button = Button(text="Cancel", size_hint=(1, None), height=40)
        cancel_button.bind(on_press=self.dismiss_popup)
        layout.add_widget(cancel_button)

        self.popup = Popup(title="File Options", content=layout, size_hint=(None, None), size=(400, 300))
        self.popup.open()

    def open_file(self, instance):
        self.alert_label.text = "[color=00ff00]Opening file...[/color]"
        self.popup.dismiss()

    def open_file_location(self, instance):
        self.alert_label.text = "[color=00ff00]Opening file location...[/color]"
        self.popup.dismiss()

    def dismiss_popup(self, instance):
        self.popup.dismiss()

class SmartDownloadHandlerApp(App):
    def build(self):
        return SmartDownloadHandler()

if __name__ == "__main__":
    SmartDownloadHandlerApp().run()
