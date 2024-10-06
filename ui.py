import flet as ft
import backup as b

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

    database_type_dropdown = ft.Dropdown(label='Database Type', width=300, options=[
        ft.dropdown.Option('mysql'),
        ft.dropdown.Option('postgres'),
        ft.dropdown.Option('mongodb'),
    ], autofocus=True, hint_text='Database Type')
    host_text = ft.TextField(label='Host address', value='localhost', text_align=ft.TextAlign.LEFT, width=300)
    port_text = ft.TextField(label='Host port', text_align=ft.TextAlign.LEFT, width=300)
    username_text = ft.TextField(label='Username', value='root', text_align=ft.TextAlign.LEFT, width=300)
    password_text = ft.TextField(label='Password', text_align=ft.TextAlign.LEFT, width=300, password=True)
    database_text = ft.TextField(label='Database', text_align=ft.TextAlign.LEFT, width=300)

    def backup(e: ft.ControlEvent):
        print(f"type is {database_type_dropdown.value}")
        print(f"host is {host_text.value}")
        print(f"port is {port_text.value}")
        print(f"username is {username_text.value}")
        print(f"password is {password_text.value}")
        print(f"database is {database_text.value}")
        backup_result = b.backup_db(database_type_dropdown.value, database_text.value, host_text.value, port_text.value, username_text.value, password_text.value)

    backup_button = ft.ElevatedButton(text='Backup')
    backup_button.on_click = backup
    # page.add(database_type_dropdown, host_text, host_port, username_text, password_text,
    # ft.ElevatedButton("Pick files", icon=ft.icons.UPLOAD_FILE, on_click=lambda _: pick_files_dialog.pick_files()), selected_files)

    backup_tab = ft.Tab(
        text="Backup",
        icon=ft.icons.BACKUP_TABLE,
        content=ft.Column(
            [
                database_type_dropdown,
                host_text,
                port_text,
                username_text,
                password_text,
                database_text,
                backup_button
            ],
        )
    )

    tabs = ft.Tabs(selected_index=0, animation_duration=300, tabs=[backup_tab])
    page.add(tabs)


ft.app(target=ui)