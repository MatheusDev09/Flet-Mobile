import flet as ft

def main(page: ft.Page):
    # Early Configurations
    page.title="Light Mode/Dark Mode"
    page.theme_mode=ft.ThemeMode.LIGHT # Starts with the light mode.
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER # Aligns every component on the horizontal center of the application.

    def build():
        # Refresh the window before restarting the app.
        page.controls.clear()

        # Assign a variable "dark" with the value of dark theme.
        dark = page.theme_mode == ft.ThemeMode.DARK

        # Defines the icon's colors and text along with the active theme.
        icon = ft.Icon(
            ft.Icons.LIGHT_MODE if dark else ft.Icons.DARK_MODE,
            size=60,
            color=ft.Colors.AMBER if dark else ft.Colors.BLUE_200,
        )
        text = ft.Text(
            "Dark Mode activated." if dark else "Light Mode activated.",
            size=20,
            weight=ft.FontWeight.BOLD,
        )
        button = ft.Button( # ft.ElevatedButton is outdated on Flet's current version.
            "Activate Light Mode" if dark else "Activate Dark Mode",
            on_click=change_theme,
        )
        

        # Background settings.
        page.bg_color= ft.Colors.BLACK if dark else ft.Colors.WHITE

        # Load the elements created on the center.
        page.add(
            ft.Column( # Build a column with, so, the main axis becomes the vertical axis.
                [ft.Container(height=60), icon, text, button], # Incrementing the objects we created inside the container along with its height.
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )

        page.update()

    def change_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        build() # Calls the function to update the theme everytime the change_theme is used.


    build() # Different from this one. This is the first calling to build the interface, before any action is taken.

# Initialize the application
ft.run(main)