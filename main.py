from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar


class ConverterApp(MDApp):
    def flip(self):
        # Hide labels until needed.
        self.converted.text = ""
        self.label.text = ""
        self.input.text = ""
        # A method for the "flip" icon
        # changes the state of the app.
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Decimal to Binary"
            self.input.hint_text = "Enter a decimal number"
        else:
            self.state = 0
            self.toolbar.title = "Binary to Decimal"
            self.input.hint_text = "Enter a binary number"

    def convert(self, x):
        # A method to find the decimal/binary equivalent.
        try:
            if "." not in self.input.text:
                # If the user-provided number is not a fraction.
                if self.state == 0:
                    # Binary to decimal
                    val = str(int(self.input.text, 2))
                    self.label.text = "in decimal is:"
                else:
                    # Decimal to binary.
                    val = bin(int(self.input.text))[2:]
                    self.label.text = "in binary is:"
                self.converted.text = val
            else:
                # If the user provided number is a fraction.
                whole, fraction = self.input.text.split(".")

                if self.state == 0:
                    # Convert binary to decimal.
                    whole = int(whole, 2)
                    floating = 0
                    for idx, digit in enumerate(fraction):
                        floating += int(digit) * 2 ** (- (idx + 1))
                    self.label.text = "in decimal is:"
                    self.converted.text = str(whole + floating)
                else:
                    # Convert decimal to binary.
                    decimal_places = 10
                    whole = bin(int(whole))[2:]
                    fraction = float("0." + fraction)
                    floating = []
                    for i in range(decimal_places):
                        if fraction * 2 < 1:
                            floating.append("0")
                            fraction *= 2
                        elif fraction * 2 > 1:
                            floating.append("1")
                            fraction = fraction * 2 - 1
                        elif fraction * 2 == 1.0:
                            floating.append("1")
                            break
                    self.label.text = "in binary is:"
                    self.converted.text = whole + "." + "".join(floating)
        except ValueError:
            # If the user-provided value is invalid.
            self.converted.text = ""
            if self.state == 0:
                # Binary to decimal.
                self.label.text = "Please enter a valid binary number"

            else:
                # Decimal to binary.
                self.label.text = "Please enter a valid decimal number"

    def build(self):
        self.state = 0  # Initial state.
        self.theme_cls.primary_palette = "Blue"
        screen = MDScreen()

        # Top toolbar.
        self.toolbar = MDToolbar(title="Binary to Decimal")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.toolbar)

        # Logo.
        screen.add_widget(Image(
            source="logo.png",
            pos_hint={"center_x": 0.5, "center_y": 0.7}
            ))

        # Collect user input.
        self.input = MDTextField(
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_text_validate=self.convert
        )
        self.input.hint_text = "Enter a binary number"
        screen.add_widget(self.input)

        # Secondary + Primary labels.
        self.label = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color="Secondary"
        )

        self.converted = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            theme_text_color="Primary",
            font_style="H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        # "CONVERT" button.
        screen.add_widget(MDFillRoundFlatButton(
            text="    CONVERT    ",
            font_size=25,
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            on_press=self.convert
        ))

        return screen


if __name__ == '__main__':
    ConverterApp().run()
