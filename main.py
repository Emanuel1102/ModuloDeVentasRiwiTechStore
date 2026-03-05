client_name=input('Nombre del cliente (sin espacios, ni numeros ni caracteres especiales) => ')

if client_name.isalpha():
    try:
        products_quantity=int(input('¿Cuantos productos va a comprar el cliente? => '))

        products=[]

        for current_product in range(products_quantity):
            product_name=input(f'Ingresa el producto #{current_product+1} (nombre del producto) => ')
            unitary_price=int(input('Precio unitario del producto => $'))
            product_quantity=int(input('Cantidad => '))
            total_product=unitary_price*product_quantity


            if product_name.isalpha():
                if unitary_price and product_quantity:
                    new_product={
                        'product_name':product_name,
                        'unitary_price': unitary_price,
                        'product_quantity':product_quantity,
                        'product_total': total_product
                    }
                    products.append(new_product)
                else:
                    print('No se pudo realizar el proceso, dejaste un campo sin llenar')
            else:
                print('El nombre no debe contener espacios, numeros o caracteres especiales')

            print('-'*15)
                


        subtotal=0

        for product in products:
            subtotal+=product['product_total']

        total=subtotal

    # Interfaz de los datos de la venta
        print(f'Cliente: {client_name}')
        print('-'*60)
        print(f'''| Product... | cant... |  Precio unit... |     total    |''')
        print('-'*60)
        for product in products:
            print(f'| {product['product_name']}     |    {product['product_quantity']}    |    ${product['unitary_price']}        |    ${product['product_total']}    |')
            print('-'*60)

        print(f'''
            subtotal: ${subtotal} 
            ----------------------    
            total general: ${total} 
              ''')

    except ValueError:
        print('Los campos de cantidades deben ser valores numéricos')
else:
    print('Al parecer ingresaste el nombre mal, verifica que no contenga espacios, numeros o caracteres especiales.')




