from kelistoapp import Cesta

def main():
    carrito=Cesta(True,True)
    #añadir productos con carrito.scan('ID')
    carrito.scan('GR1')
    carrito.scan('SR1')
    carrito.scan('GR1')
    carrito.scan('GR1')
    carrito.scan('CF1')
    #------------------
    carrito.total() 

if __name__ == '__main__':
    main()
