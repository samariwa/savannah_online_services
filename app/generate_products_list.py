import pandas as pd
from flask import send_file
from app.controllers.read import fetch_active_products
from app.general_functions import create_timestamp

def generate_products_excel():
    # create products dictionary
    all_products = fetch_active_products()
    sheet_index = 0
    now = create_timestamp()
    products = {
        'PLU No': {},
        'PLU Type': {},
        'Itemcode': {},
        'Name1': {},
        'Unit Price': {},
        'Update Date': {}
    }
    for product in all_products:
        products['PLU No'][sheet_index] = all_products[product]['product_id']
        if all_products[product]['measurement_mode'] == 'weight':
            products['PLU Type'][sheet_index] = 1
        else:
            products['PLU Type'][sheet_index] = 2
        products['Itemcode'][sheet_index] = all_products[product]['product_id']
        products['Name1'][sheet_index] = all_products[product]['product_name']
        products['Unit Price'][sheet_index] = all_products[product]['selling_price']
        products['Update Date'][sheet_index] = now
        sheet_index = sheet_index + 1
    
    # forming dataframe
    data = pd.DataFrame(products)
    # storing into the excel file
    data.to_excel("app/static/Stock_Sheets/stock_sheet_"+now+".xlsx", index=False)
    
    return send_file("static/Stock_Sheets/stock_sheet_"+now+".xlsx", as_attachment=True)