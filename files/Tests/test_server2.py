import pytest
import server2
import tempfile
import json


@pytest.fixture(scope='function')
def client():
    server2.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    server2.app.config['TESTING'] = True
    client = server2.app.test_client()

    with server2.app.app_context():
        server2.db.create_all()

    yield client


# class TestGetUsers(object):
#     @pytest.mark.users
#     def test_get_users_empty(self, client):
#         response = client.get('/admin/users/')
#         response_data = json.loads(response.data)

#         assert len(response_data['users']) == 0

#     @pytest.mark.users
#     def test_get_users_one(self, client):
#         with server2.app.app_context():
#             test_user = server2.Users(first_name='Bill')

#             server2.db.session.add(test_user)
#             server2.db.session.commit()

#         response = client.get('/admin/users/')
#         response_data = json.loads(response.data)

#         assert response_data['users'][0]['firstName'] == 'Bill'


class TestAddUsers(object):
    def test_add_one_user(self, client):
        response = client.post('/admin/', json={
            'firstName': 'Byron',
            'lastName': 'Daniels'
        })

        with server2.app.app_context():
            name = server2.db.session.query(server2.Users).one().first_name

            assert name == 'Byron'
