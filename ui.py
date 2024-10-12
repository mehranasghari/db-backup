import flet as ft 
''' import flet for creating UI '''
import backup as b
import restore as r

def ui(page: ft.Page, height, width): 
    ''' setup the page '''
    page.title = 'Backup & Restore Database'
    page.window.height = height
    page.window.width = width


    database_type_dropdown = ft.Dropdown(label='Database Type', width=300, options=[
        ft.dropdown.Option('mysql'),
        ft.dropdown.Option('postgres'),
        ft.dropdown.Option('mongodb'),
    ], autofocus=True, hint_text='Database Type')
    host_text = ft.TextField(
        label='Host address', value='127.0.0.1', 
        text_align=ft.TextAlign.LEFT, width=300
        )
    port_text = ft.TextField(label='Host port', text_align=ft.TextAlign.LEFT, width=300)
    username_text = ft.TextField(
        label='Username', value='root', 
        text_align=ft.TextAlign.LEFT, width=300)
    password_text = ft.TextField(
        label='Password', text_align=ft.TextAlign.LEFT, width=300, password=True)
    database_text = ft.TextField(label='Database', text_align=ft.TextAlign.LEFT, width=300)


    backup_result_message = ft.Text(value='', color='green')

    selected_files = ft.Text()
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else 'canceled'
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)

    page.overlay.append(pick_files_dialog)
    restore_result_message = ft.Text(value='', color='green')


    def backup():
        print(f"type is {database_type_dropdown.value}")
        print(f"host is {host_text.value}")
        print(f"port is {port_text.value}")
        print(f"username is {username_text.value}")
        print(f"database is {database_text.value}")
        backup_result = b.backup_db(database_type_dropdown.value,
            database_text.value,
            host_text.value, port_text.value,
            username_text.value, password_text.value)

        if backup_result:
            backup_result_message.value = f'Backup was successful! File name: {backup_result}'
            backup_result_message.color = 'green'
        else:
            backup_result_message.value = 'Backup failed!'
            backup_result_message.color = 'red'
        backup_result_message.update()

    def restore():
        print(f"type is {database_type_dropdown.value}")
        print(f"database restore file path is {selected_files.value}")
        print(f"host is {host_text.value}")
        print(f"port is {port_text.value}")
        print(f"username is {username_text.value}")
        print(f"database is {database_text.value}")
        restore_result = r.restore_db(
            database_type_dropdown.value,
            selected_files.value,
            database_text.value,
            host_text.value, port_text.value,
            username_text.value, password_text.value)

        if restore_result:
            restore_result_message.value = f'Restore file {selected_files.value} \
                to database {database_text.value} was successful!'
            restore_result_message.color = 'green'
        else:
            restore_result_message.value = f'Restore file {selected_files.value} \
                to database {database_text.value} failed!'
            restore_result_message.color = 'red'
        restore_result_message.update()


    pick_files_button = ft.ElevatedButton(
        "Select files", icon=ft.icons.UPLOAD_FILE,
        on_click=lambda _: pick_files_dialog.pick_files()
        )
    restore_button = ft.ElevatedButton("Restore", on_click=restore)

    backup_button = ft.ElevatedButton(text='Backup', on_click=backup)

    backup_tab = ft.Tab(
        text="Backup",
        icon=ft.icons.BACKUP_TABLE,
        content=ft.Column([
                database_type_dropdown,
                host_text,
                port_text,
                username_text,
                password_text,
                database_text,
                backup_button,
                selected_files,
                backup_result_message
            ],
        )
    )

    restore_tab = ft.Tab(
        text="Restore",
        icon=ft.icons.RESTORE_PAGE_OUTLINED,
        content=ft.Column([
            database_type_dropdown,
            host_text,
            port_text,
            username_text,
            password_text,
            database_text,
            pick_files_button,
            restore_button,
            restore_result_message,
        ])
    )

    tabs = ft.Tabs(selected_index=0, animation_duration=300, tabs=[backup_tab, restore_tab])
    page.add(tabs)


ft.app(target=ui(height=600, width=600))
