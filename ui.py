import flet as ft

def ui(page: ft.Page):
    page.title = 'Backup & Restore Database'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.theme_mode = 'dark'
    page.window_height = 600
    page.window_width = 600

    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else 'canceled'
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    database_type_dropdown = ft.Dropdown(label='Database Type', width=400, options=[
        ft.dropdown.Option('mysql'),
        ft.dropdown.Option('postgres'),
        ft.dropdown.Option('mongodb'),
    ], autofocus=True, hint_text='Database Type')
    host_text = ft.TextField(label='Host address', value='localhost', text_align=ft.TextAlign.LEFT, width=400)
    host_port = ft.TextField(label='Host port', text_align=ft.TextAlign.LEFT, width=400)
    username_text = ft.TextField(label='Username', value='root', text_align=ft.TextAlign.LEFT, width=400)
    password_text = ft.TextField(label='Password', text_align=ft.TextAlign.LEFT, width=400, password=True)

    mode_dropdown = ft.Dropdown(label='Backup/Restore',width=400, options=[
        ft.dropdown.Option('Backup'),
        ft.dropdown.Option('Restore'),
    ])
    
    page.add(database_type_dropdown, host_text, host_port, username_text, password_text,
    ft.ElevatedButton("Pick files", icon=ft.icons.UPLOAD_FILE, on_click=lambda _: pick_files_dialog.pick_files()), selected_files)

ft.app(target=ui)