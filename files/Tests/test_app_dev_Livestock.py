import pytest
import app_dev
import tempfile
import json
from datetime import datetime


@pytest.fixture(scope='function')
def client():
    app_dev.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app_dev.app.config['TESTING'] = True
    client = app_dev.app.test_client()

    with app_dev.app.app_context():
        app_dev.db.create_all()

    yield client


class TestGetLivestock(object):
    def test_get_livestock_empty(self, client):
        response = client.get('/livestock/all/')
        response_data = json.loads(response.data)

        assert len(response_data['livestock']) == 0

    def test_get_livestock_one(self, client):
        with app_dev.app.app_context():
            test_livestock = app_dev.Livestock(product_name='Beef', breed='Angus',
                                               user_id=3, rfid_tag=41, starting_weight=6969)
            app_dev.db.session.add(test_livestock)
            app_dev.db.session.commit()

        response = client.get('/livestock/all/')
        response_data = json.loads(response.data)

        assert response_data['livestock'][0]['type'] == 'Beef'
        with app_dev.app.app_context():
            app_dev.db.session.query(app_dev.Livestock).delete()
            app_dev.db.session.commit()


class TestAddLivestock(object):
    def test_add_one_livestock(self, client):
        response = client.post('/livestock/', json={
            'userId': 6,
            'type': 'Pork',
            'breed': 'Berkshire',
            'singleBrand': True,
            'regNumber': 69
        })

        with app_dev.app.app_context():
            id = app_dev.db.session.query(app_dev.Livestock).one().user_id
            l_type = app_dev.db.session.query(
                app_dev.Livestock).one().product_name
            l_breed = app_dev.db.session.query(
                app_dev.Livestock).one().breed
            l_brand = app_dev.db.session.query(
                app_dev.Livestock).one().single_brand
            l_reg = app_dev.db.session.query(
                app_dev.Livestock).one().registration_number

            assert id == 6
            assert l_type == 'Pork'
            assert l_breed == 'Berkshire'
            assert l_brand == '1'
            assert l_reg == 69

        with app_dev.app.app_context():
            app_dev.db.session.query(app_dev.Livestock).delete()
            app_dev.db.session.commit()


class TestIncrementLivestockStatus(object):
    def test_increment_livestock_status(self, client):
        test_livestock = app_dev.Livestock(product_name='Beef', breed='Angus',
                                           user_id=6, id=6, status='accepted', starting_weight=6969)
        app_dev.db.session.add(test_livestock)
        app_dev.db.session.commit()

        response = client.post('/livestock/incrementStatus/', json={
            'id': '6',
            'nextStatus': 'sold',
        })
        with app_dev.app.app_context():
            l_status = app_dev.db.session.query(app_dev.Livestock).one().status
            assert l_status == 'sold'


class TestGetLivestockById(object):
    def test_get_livestock_by_id(self, client):
        test_livestock_1 = app_dev.Livestock(product_name='Beef', breed='Angus',
                                             user_id=6, id=16, status='accepted', starting_weight=6969)
        test_livestock_2 = app_dev.Livestock(product_name='Pork', breed='Berkshire',
                                             user_id=8, id=44, status='sold', starting_weight=69, est_birthdate=datetime.today())
        app_dev.db.session.add(test_livestock_1)
        app_dev.db.session.add(test_livestock_2)
        app_dev.db.session.commit()
        response = client.get('/livestock/8/')
        response_data = json.loads(response.data)

        assert response_data['livestock'][0]['type'] == 'Pork'
        assert response_data['livestock'][0]['birthdate'] == 'Sat, 20 Apr 2019 00:00:00 GMT'
        with app_dev.app.app_context():
            app_dev.db.session.query(app_dev.Livestock).delete()
            app_dev.db.session.commit()


# class TestModifyLivestock(object):
#     def test_modify_livestock_one(self, client):
#         test_livestock_1 = app_dev.Livestock(product_name='Beef', breed='Angus',
#                                              user_id=6, id=18, status='accepted', starting_weight=6969)
#         app_dev.db.session.add(test_livestock_1)
#         app_dev.db.session.commit()

#         response = client.post('/livestock/modify/', json={
#             'id': 18,
#             'estStartingWeight': 69,
#             'type': 'beef',
#             'breed': 'angus',
#             'singleBrand': True,
#             'birthdate': datetime.today(),
#             'regNumber': 77,
#             'rfid': 99,
#             'estStartingWeight': 44,
#             'hangingWeight': 54,
#             'chargebacks': 12,
#             'dateOnFeed': datetime.today(),
#             'feedMethod': 'free',
#             'typeOfPasture': 'red',
#             'typeOfFeed': 'grass',
#             'estCompletionDate': datetime.today(),
#             'estFinishedWeight': 66,
#             'estFinalPrice': 12,
#             'quantity': 31,
#             'comments': 'pie',
#             'finalPrice': 77,
#             'deliveredDate': datetime.today(),
#             'deliveredTo': 'byron',
#         })
#         with app_dev.app.app_context():
#             l_weight = app_dev.db.session.query(
#                 app_dev.Livestock).one().starting_weight
#             assert l_weight == 6
