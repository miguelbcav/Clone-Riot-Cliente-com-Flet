import flet as ft

def main(page:ft.Page):
    page.theme_mode = 'dark'
    page.padding = 0
    page.window.frameless = True
    page.adaptive = True

    main_stack = ft.Stack(
        expand=True,
        controls=[
            ft.Row(
                spacing=0,
                expand=True,
                controls=[
                    ft.Container(
                        padding=0,
                        width=330,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=["#09121D","#162437","#152943","#193457"]
                        ),
                        content=ft.Column(
                            horizontal_alignment='center',
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(top=30),
                                    alignment=ft.alignment.top_center,
                                    content=ft.Container(
                                        image=ft.DecorationImage(
                                            src="imagem_2024-11-09_232331470-removebg-preview.png",
                                        ),
                                        width=130,
                                        height=130
                                    ),
                                ),
                                ft.Container(
                                    width=250,
                                    height=40,
                                    bgcolor='#152943',
                                    border_radius=12,
                                    border=ft.border.all(width=0.1,color=ft.colors.with_opacity(opacity=.2,color='white')),
                                    padding=ft.padding.only(left=5,right=5),
                                    content=ft.Row(
                                        spacing=0,
                                        #alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[
                                            ft.ElevatedButton(
                                                text="Fazer login",
                                                bgcolor="#152943",
                                                elevation=0,
                                                icon=ft.icons.KEYBOARD,
                                                style=ft.ButtonStyle(
                                                    text_style=ft.TextStyle(
                                                        size=10
                                                    ),
                                                    icon_size=24
                                                )
                                            ),
                                            ft.ElevatedButton(
                                                text="Código QR",
                                                bgcolor="#152943",
                                                elevation=0,
                                                icon=ft.icons.QR_CODE,
                                                style=ft.ButtonStyle(
                                                    text_style=ft.TextStyle(
                                                        size=10
                                                    ),
                                                    icon_size=24
                                                )
                                            )
                                        ]
                                    )
                                ),
                                ft.Divider(
                                    height=5,
                                    color='transparent'
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.TextField(
                                                width=250,
                                                height=40,
                                                label="NOME DE USUÁRIO",
                                                label_style=ft.TextStyle(
                                                    color="#a0cafd",
                                                    size=10
                                                ),
                                                bgcolor='#152943',
                                                border_radius=5,
                                                border_color='transparent',
                                                content_padding=10,
                                                color='white'
                                            )
                                        ]
                                    )
                                ),
                                ft.Divider(
                                    height=0.5,
                                    color='transparent'
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.TextField(
                                                width=250,
                                                height=40,
                                                label="SENHA",
                                                label_style=ft.TextStyle(
                                                    color="#a0cafd",
                                                    size=10
                                                ),
                                                bgcolor='#152943',
                                                border_radius=5,
                                                border_color='transparent',
                                                content_padding=10,
                                                color='white',
                                                password=True,
                                                can_reveal_password=True
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    padding=ft.padding.only(left=36),
                                    alignment=ft.alignment.center_left,
                                    content=ft.Checkbox(
                                        splash_radius=10,
                                        label="Manter login",
                                        label_style=ft.TextStyle(
                                            color="#a0cafd",
                                            size=12
                                        ),
                                        active_color="#a0cafd",
                                        border_side=ft.BorderSide(color="#a0cafd",width=1)
                                    )
                                ),
                                ft.Container(
                                    padding=ft.padding.only(top=50),
                                    content=ft.FloatingActionButton(
                                        bgcolor="#213a5b",
                                        content=ft.Icon(ft.icons.ARROW_FORWARD,color='#a0cafd'),
                                        
                                    )
                                ),
                            ]
                        )
                    ),
                    ft.Container(
                        image_src="https://images4.alphacoders.com/119/1194463.jpg",
                        expand=True,
                        image_fit=ft.ImageFit.COVER
                    )
                ]
            ),
            ft.Row(
                controls=[
                    ft.WindowDragArea(width=page.window.width - 35,height=30,content=ft.Container(bgcolor='transparent')),
                    ft.Container(
                        content=ft.Icon(
                            name=ft.icons.CLOSE,
                            color="grey",
                            scale=0.7
                        ),
                        ink=True,
                        ink_color="red",
                        on_click = lambda e: page.window.close()
                    ),
                ]
            ),
        ]
    )


    page.add(
        main_stack
    )

ft.app(target=main)