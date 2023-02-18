import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


# @pytest.mark.database
# def test_check_all_users():

#     db = Database()
#     users = db.get_all_users()


#     print(users)


@pytest.mark.database
def test_check_user_stepan():
    db = Database()
    user = db.get_users_address_by_name('Stepan')

    assert user[0][0] == 'Stepana Bandery str, 2'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '2055'
    assert user[0][3] == 'Ukraine'

# @pytest.mark.database
# def test_check_all_products():
#     db = Database()
#     products = db.get_all_products()

#     print(products)

# @pytest.mark.database
# def test_product_qnt_update():
#     db = Database()
#     db.update_products(30, 1)
#     water_qnt = db.get_products_quantity_by_id(1)

#     assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_add():
    db = Database()
    db.insert_product(5, 'coffee', 'Arabica', 5)
    # db.insert_product(4, 'печиво', 'пісочне', 25)
    product_qnt = db.get_products_quantity_by_id(5)

    assert product_qnt[0][0] == 5


@pytest.mark.database
def test_product_deleted():
    db = Database()
    db.insert_product(100, 'test_product', 'test_data', 10000)
    db.delete_product_by_id(100)
    qnt = db.get_products_quantity_by_id(100)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    # print("Orders: ", orders)
    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'
