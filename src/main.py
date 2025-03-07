import flet as ft

def main(page: ft.Page):
    
    def table_cell(cell_content):
        return ft.DataCell(ft.Text(cell_content))
    
    contItens_pedido = 0
    #item = [table_cell(contItens_pedido), table_cell("teste"),table_cell("teste"), table_cell("teste"), table_cell("teste")]
    itens_pedido = ft.DataRow(cells=[table_cell(contItens_pedido), table_cell("teste"),table_cell("teste"), table_cell("teste"), table_cell("teste")])
    
    def updateItem_table(cont):
        return 
        page.add(ft.DataRow(
            ft.DataCell(ft.Text(cont)),
            ft.DataCell(ft.Text("teste")),
            ft.DataCell(ft.Text("teste")),
            ft.DataCell(ft.Text("teste")),
            ft.DataCell(ft.Text("teste"))
        ))
    
    def addItem_clicked(e):
        rowTable = []
        contItens_pedido += 1
        item = [table_cell(contItens_pedido), table_cell("teste"),table_cell("teste"), table_cell("teste"), table_cell("teste")]
        itens_pedido.append(ft.DataRow(cells=item))
    
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
            rows=itens_pedido)
    )
        
    page.add(ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=addItem_clicked))
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    
ft.app(main)