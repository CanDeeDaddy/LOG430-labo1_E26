"""
Main view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, Dave Charles 2026
"""
from models.user import User
from models.product import Product
from controllers.user_controller import UserController
from controllers.product_controller import ProductController

class MainView:
    @staticmethod
    def show_options():
        """ Show main menu with all options """
        user_controller = UserController()
        product_controller = ProductController()

        while True:
            print("\n1. Montrer la liste d'utilisateurs")
            print("2. Ajouter un utilisateur")
            print("3. Montrer la liste d'articles")
            print("4. Ajouter un article")
            print("5. Quitter l'appli")
            choice = input("Choisissez une option: ")

            if choice == '1':
                users = user_controller.list_users()
                MainView.show_users(users)
            elif choice == '2':
                name = input("Nom d'utilisateur : ").strip()
                email = input("Adresse courriel : ").strip()
                user_controller.create_user(User(None, name, email))
            elif choice == '3':
                products = product_controller.list_products()
                MainView.show_products(products)
            elif choice == '4':
                name = input("Nom du produit : ").strip()
                brand = input("Marque : ").strip()
                price = float(input("Prix : ").strip())
                product_controller.create_product(Product(None, name, brand, price))
            elif choice == '5':
                user_controller.shutdown()
                product_controller.shutdown()
                break
            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def show_users(users):
        print("\n".join(f"{u.id}: {u.name} ({u.email})" for u in users))

    @staticmethod
    def show_products(products):
        print("\n".join(f"{p.id}: {p.name} ({p.brand}) - ${p.price}" for p in products))