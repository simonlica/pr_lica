from restaurante import InterfaceUsuario

def main():
    app = InterfaceUsuario()

    app.gerenciador.adicionar_restaurante("La Trattoria del Nonno", "Culinaria Itáliana")
    app.gerenciador.adicionar_restaurante("La Pizzeria Romana", "Pizzaria")
    app.gerenciador.adicionar_restaurante("La Dolce Vita", "Padaria")

    app.main()

if __name__ == '__main__':
    main()