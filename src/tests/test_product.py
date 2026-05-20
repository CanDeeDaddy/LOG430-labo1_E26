from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
    product_list = dao.select_all()
    assert len(product_list) >= 3

def test_product_insert():
    product = Product(None, 'Moniteur', 'Samsung', 299.99)
    dao.insert(product)
    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name in names

def test_product_update():
    product = Product(None, 'Vieux Clavier', 'HP', 19.99)
    assigned_id = dao.insert(product)

    product.id = assigned_id
    product.price = 24.99
    dao.update(product)

    product_list = dao.select_all()
    prices = [p.price for p in product_list]
    assert float(24.99) in [float(p) for p in prices]
    
    # cleanup
    dao.delete(assigned_id)

def test_product_delete():
    product = Product(None, 'Temp Product', 'TestBrand', 9.99)
    assigned_id = dao.insert(product)
    dao.delete(assigned_id)
    
    new_dao = ProductDAO()
    product_list = new_dao.select_all()
    names = [p.name for p in product_list]
    assert product.name not in names