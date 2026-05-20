"""
Product view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Dave Charles 2026
"""
from models.product import Product
from controllers.product_controller import ProductController

class ProductView:
    @staticmethod
    def show_options():
        """ Show menu with operation options """
        controller = ProductController()
        while True:
            print("\n1. Montrer la liste d'items\n2. Ajouter un item\n3. Supprimer un item\n4. Quitter l'appli")
            choice = input("Choisissez une option: ")
            if choice == '1':
                products = controller.list_products()
                ProductView.show_products(products)
            elif choice == '2':
                name, brand, price = ProductView.get_inputs()
                product = Product(None, name, brand, price)
                controller.create_product(product)
            elif choice == '3':
                product_id = int(input("ID du produit à supprimer : ").strip())
                controller.delete_product(product_id)
                print("Produit supprimé.")
            elif choice == '4':
                controller.shutdown()
                break
            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def show_products(products):
        """ List products """
        print("\n".join(f"{p.id}: {p.name} ({p.brand}) - ${p.price}" for p in products))

    @staticmethod
    def get_inputs():
        """ Prompt user for inputs to add a new product """
        name = input("Nom du produit : ").strip()
        brand = input("Marque : ").strip()
        price = float(input("Prix : ").strip())
        return name, brand, price