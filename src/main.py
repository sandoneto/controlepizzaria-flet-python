import flet as ft


def main(page: ft.Page):
    
    def handle_close(e):
        page.close(addItemDialog)
    
    addItemDialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Adicionar Novo Item Ao Pedido"),
        actions=[
            ft.FilledButton(text="Cancelar", on_click=handle_close),
            ft.FilledButton(text="Adicionar Item", on_click=handle_close)
        ],
        on_dismiss=lambda e: page.add()
    )
    
    def table_cell(cell_content):
        return ft.DataCell(ft.Text(cell_content))
    
    contItens_pedido = 0
    #item = [table_cell(contItens_pedido), table_cell("teste"),table_cell("teste"), table_cell("teste"), table_cell("teste")]
    itens_pedido = ft.DataRow(cells=[table_cell(contItens_pedido), table_cell("teste"),table_cell("teste"), table_cell("teste"), table_cell("teste")])
    
    def updateItem_table(cont):
        pass
        
    
    def addItem_clicked(e):
        
        pass
    
    page.add(
        
        ft.Row(controls=[
            ft.Text(value="Informações do Cliente")
        ]),
        
        ft.Row(controls=[
            ft.TextField(hint_text="Cliente", expand=True)
        ]),
        
        ft.Row(controls=[
            ft.TextField(hint_text="Local de Entrega",
                         multiline=True,
                         min_lines=3,
                         max_lines=3,
                         expand=True)
        ]),
        ft.Row(controls=[
            ft.Text(value="Itens do pedido:")
        ]),
        ft.DataTable(columns=[
            ft.DataColumn(ft.Text("Seq.")),
            ft.DataColumn(ft.Text("Descrição")),
            ft.DataColumn(ft.Text("Quatidade")),
            ft.DataColumn(ft.Text("Valor")),
            ft.DataColumn(ft.Text("Ações"))
        ],
        rows=[
            ft.DataRow([
                ft.DataCell(ft.Text("1")),
                ft.DataCell(ft.Text("Pizza Calabresa")),
                ft.DataCell(ft.Text("1")),
                ft.DataCell(ft.Text("35.50")),
                ft.DataCell(ft.Text("Exemplo"))
            ])
        ],
        ),
    )
        
    page.add(ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=lambda e: page.open(addItemDialog)))
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    
ft.app(main)