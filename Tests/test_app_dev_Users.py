import pytest
import app_dev
import tempfile
import json


@pytest.fixture(scope='function')
def client():
    app_dev.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app_dev.app.config['TESTING'] = True
    client = app_dev.app.test_client()

    with app_dev.app.app_context():
        app_dev.db.create_all()

    yield client


class TestGetUsers(object):
    @pytest.mark.users
    def test_get_users_empty(self, client):
        response = client.get('/admin/users/')
        response_data = json.loads(response.data)

        assert len(response_data['users']) == 0

    @pytest.mark.users
    def test_get_users_one(self, client):
        with app_dev.app.app_context():
            test_user = app_dev.Users(first_name='Bill', last_name='Dee',
                                      primary_phone=333, email='bill@hotmail.com', farm_name='bfarm')
            app_dev.db.session.add(test_user)
            app_dev.db.session.commit()

        response = client.get('/admin/users/')
        response_data = json.loads(response.data)

        assert response_data['users'][0]['firstName'] == 'Bill'
        with app_dev.app.app_context():
            app_dev.db.session.query(app_dev.Users).delete()
            app_dev.db.session.commit()


class TestAddUsers(object):
    def test_add_one_user(self, client):
        response = client.post('/admin/', json={
            'firstName': 'Byron',
            'lastName': 'Daniels',
            'primaryNumber': 666,
            'email': 'byron@hotmail.com',
            'farmName': 'happy farm'
        })

        with app_dev.app.app_context():
            name1 = app_dev.db.session.query(app_dev.Users).one().first_name
            name2 = app_dev.db.session.query(app_dev.Users).one().last_name
            num1 = app_dev.db.session.query(app_dev.Users).one().primary_phone
            email_1 = app_dev.db.session.query(app_dev.Users).one().email
            fname = app_dev.db.session.query(app_dev.Users).one().farm_name
            ID = app_dev.db.session.query(app_dev.Users).one().id

            assert name1 == 'Byron'
            assert name2 == 'Daniels'
            assert num1 == '666'
            assert email_1 == 'byron@hotmail.com'
            assert fname == 'happy farm'
            assert ID == 1

        with app_dev.app.app_context():
            app_dev.db.session.query(app_dev.Users).delete()
            app_dev.db.session.commit()


class TestDeleteUsers(object):
    def test_delete_one_user(self, client):

        with app_dev.app.app_context():
            test_user = app_dev.Users(first_name='Bill', last_name='Dee',
                                      primary_phone=333, email='bill@hotmail.com', farm_name='bfarm')
            app_dev.db.session.add(test_user)
            app_dev.db.session.commit()

        response = client.post('/admin/users/delete/', json={
            'id': '1',
        })
        with app_dev.app.app_context():
            response = client.get('/admin/users/')
            response_data = json.loads(response.data)
            assert len(response_data['users']) == 0
            app_dev.db.session.query(app_dev.Users).delete()
            app_dev.db.session.commit()


# class TestModifyUsers(object):
#     def test_modify_one_user(self, client):

#         with app_dev.app.app_context():
#             test_user = app_dev.Users(first_name='Bill', last_name='Dee',
#                                       primary_phone=333, email='bill@hotmail.com', farm_name='bfarm')
#             app_dev.db.session.add(test_user)
#             app_dev.db.session.commit()

#         response = client.post('/admin/updateUsers/', json={
#             'id': 1,
#             'firstName': 'Joe',
#             'lastName': 'Carrot',
#             'primaryNumber': 555,
#             'email': 'jcarrot@hotmail.com',
#             'farmName': 'carrot farm',
#             "billingAddressStreet": 'lenton',
#             "secondaryNumber": '123',
#             "billingAddressCity": 'edmonton',
#             "billingAddressProvince": 'ab',
#             "billingAddressCountry": 'canada',
#             "billingAddressPostalCode": 't3e5e7',
#             "farmLocation": 'enderby',
#             "mailingAddressStreet": 'laxton',
#             "farmType": 'big',
#             "area": 'NW',
#             "mailingAddressCity": 'calgary',
#             "mailingAddressProvince": "Alberta",
#             "rating": 4,
#             "mailingAddressCountry": 'canada',
#             "mailingAddressPostalCode": 't3e5e7',
#             "comments": 'testcomment',
#             "isAdmin": True
#         })

        # with app_dev.app.app_context():
        #     name1 = app_dev.db.session.query(app_dev.Users).one().first_name
        #     assert name1 == 'Byron'
