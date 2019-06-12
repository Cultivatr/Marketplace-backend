import unittest
import sql
import os


class TestSql(unittest.TestCase):

    def test_hello(self):
        self.assertEqual('hello world from SQL', sql.hello())

    def test_get_connect_string(self):
        self.assertEqual(sql.default_connect, sql.get_connect_string())
        os.environ[sql.db_env] = "1"
        self.assertEqual(os.environ[sql.db_env], sql.get_connect_string())
        del os.environ[sql.db_env]

    def test_users(self):
        sql.create_table_users()
        sql.add_user("Joe", "Bob", "123-456-7890", "890-123-4567", "test@gmail.com", "jeff's farm", "calgary", "southern alberta", "TRUE", "TRUE", "TRUE", "2018-09-01", "livestock", "5", "none", "none", "none", "none", "none", "none", "none", "none", "none", "none", "hellllooooo")
        sql.add_user("Jim", "Greg", "123-456-7890", "890-123-4567", "test2@gmail.com", "jeff's farm", "calgary", "southern alberta", "TRUE", "TRUE", "TRUE", "2018-09-01", "livestock", "5", "none", "none", "none", "none", "none", "none", "none", "none", "none", "none", "hellllooooo")
        users=sql.get_users()
        self.assertEqual(2, len(users))
        self.assertEqual("Joe", users[0].first_name)
        self.assertEqual("test2@gmail.com", users[1].email)
        user=sql.get_user(1)
        # print(user)
        self.assertEqual("Joe", user.first_name)
        user=sql.get_user(2)
        self.assertEqual("Greg", user.last_name)
        user=sql.get_user(10)
        self.assertIsNone(None)
        sql.update_user("Jeff", "Kwok", "123-456-7890", "890-123-4567", "jeff@test.com", "jeff's farm", "calgary", "southern alberta", "TRUE", "TRUE", "TRUE", "2018-09-01", "livestock", "5", "none", "none", "none", "none", "none", "none", "none", "none", "none", "none", "hellllooooo", "1")
        user=sql.get_user(1)
        # print(user)
        self.assertEqual("jeff@test.com", user.email)
        self.assertEqual("jeff's farm", user.f_name)
        # print(user.p_number)
        sql.delete_table_users()

    def test_offered_items_produce(self):
        sql.create_table_users()
        sql.add_user("Ana", "Elias", "123-456-7890", "890-123-4567", "test2@gmail.com", "jeff's farm", "calgary", "southern alberta", "TRUE", "TRUE", "TRUE", "2018-09-01", "livestock", "5", "none", "none", "none", "none", "none", "none", "none", "none", "none", "none", "hellllooooo")
        sql.create_table_offered_items_produce()
        sql.add_produce_item_by_user_id("1","Carrots", "Bag","2019-01-01", "Seed","True", "True","Fertilzier","pestocide","90","True","90","100","80","75","0","500","2019-03-01","Calgary","Helllllooooo", "Pending Approval")
        sql.add_produce_item_by_user_id("1","Cabbage", "Head","2019-01-01", "Seed","True", "True","Fertilzier","pestocide","90","True","90","100","80","75","0","500","2019-03-01","Calgary","Helllllooooo", "Pending Approval")
        sql.add_user("Larry", "Lemi", "123-456-7890", "890-123-4567", "test2@gmail.com", "jeff's farm", "calgary", "southern alberta", "TRUE", "TRUE", "TRUE", "2018-09-01", "livestock", "5", "none", "none", "none", "none", "none", "none", "none", "none", "none", "none", "hellllooooo")
        sql.add_produce_item_by_user_id("2","Wheat", "Bunch","2019-01-01", "Seed","True", "True","Fertilzier","pestocide","90","True","90","100","80","75","0","500","2019-03-01","Calgary","Helllllooooo", "Sold")
        offered_items=sql.get_offered_items_produce_by_id(2)
        # print(offered_items)
        self.assertEqual("Sold", offered_items[0].Status)
        self.assertEqual("Wheat", offered_items[0].Product_name)
        offered_items_detail=sql.get_offered_items_produce_details_by_id(2)
        # print(offered_items_detail)
        self.assertEqual("Cabbage", offered_items_detail.Product_name)
        all_offered_items=sql.get_all_offered_items_produce()
        # print(all_offered_items)
        self.assertEqual(3, len(all_offered_items))
        sql.update_offered_items_produce_detail("2","Beat", "Head","2019-01-01", "Seed","True", "True","Fertilzier","pestocide","90","True","90","100","80","75","0","500","2019-03-01","Calgary","Helllllooooo", "Pending Approval", "1")
        offered_items_detail=sql.get_offered_items_produce_details_by_id(1)
        # print(offered_items_detail)
        self.assertEqual("Beat", offered_items_detail.Product_name)
        sql.delete_table_offered_items_produce()
        sql.delete_table_users()

    def test_offered_items_livestock(self):
        sql.create_table_users()
        sql.add_user("Ana", "Elias", "123-456-7890", "890-123-4567", "test2@gmail.com", "jeff's farm", "calgary", "southern alberta", "TRUE", "TRUE", "TRUE", "2018-09-01", "livestock", "5", "none", "none", "none", "none", "none", "none", "none", "none", "none", "none", "hellllooooo")
        sql.create_table_offered_items_livestock()
        sql.add_livestock_item_by_user_id("1","Beef", "Angus","True","2019-03-01","12345", "678", "500","600","1","2019-02-01","Grass", "Alfa", "Barley", "2019-03-05","600","800","1","Hellllooooo","1000","2019-04-05","Calgary","Pending Approval")
        sql.add_livestock_item_by_user_id("1","Beef", "Birkshire","True","2019-03-02","12345", "678", "500","600","1","2019-02-01","Grass", "Alfa", "Barley", "2019-03-05","600","800","1","Hellllooooo","1000","2019-04-05","Calgary","Pending Approval")
        sql.add_user("Larry", "Lemi", "123-456-7890", "890-123-4567", "test2@gmail.com", "jeff's farm", "calgary", "southern alberta", "TRUE", "TRUE", "TRUE", "2018-09-01", "livestock", "5", "none", "none", "none", "none", "none", "none", "none", "none", "none", "none", "hellllooooo")
        sql.add_livestock_item_by_user_id("2","Chicken", "Birkshire","True","2019-03-02","12345", "678", "500","600","1","2019-02-01","Grass", "Alfa", "Barley", "2019-03-05","600","800","1","Hellllooooo","1000","2019-04-05","Calgary","Sold")
        offered_items=sql.get_offered_items_livestock_by_id(2)
        # print(offered_items)
        self.assertEqual("Sold", offered_items[0].Status)
        self.assertEqual("Chicken", offered_items[0].Product_name)
        offered_items_detail=sql.get_offered_items_livestock_details_by_id(2)
        # print(offered_items_detail)
        self.assertEqual("Birkshire", offered_items_detail.Breed)
        all_offered_items=sql.get_all_offered_items_livestock()
        print(all_offered_items)
        self.assertEqual(3, len(all_offered_items))
        sql.update_offered_items_livestock_detail("1","Beef", "Birkshire","True","2019-03-02","12345", "678", "500","600","1","2019-02-01","Grass", "Alfa", "Barley", "2019-03-05","600","800","1","Hellllooooo","1000","2019-04-05","Calgary","Pending Approval", "1")
        offered_items_detail=sql.get_offered_items_livestock_details_by_id(1)
        # print(offered_items_detail)
        self.assertEqual("Beef", offered_items_detail.Product_name)
        sql.delete_table_offered_items_livestock()
        sql.delete_table_users()
