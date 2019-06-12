class Offered_item_livestock(object):
	def __init__(self,
                Id,
                Users_id,
                Product_name,
                Breed,
                Single_brand,
                Est_birthdate,
                Registration_number,
                RFID_tag,
                Starting_weight,
                Hanging_weight,
                Chargebacks,
                Starting_date_of_feed,
                Feed_method,
                Type_of_pasture,
                Type_of_feed,
                Est_completion_date,
                Est_finished_weight,
                Est_price_to_be_paid,
                Quantity,
                Comments,
                Price_paid,
                Delivered_date,
                Delivered_to,
                Status):
                self.id = Id
                self.Users_id = Users_id
                self.Product_name = Product_name
                self.Breed = Breed
                self.Single_brand = Single_brand
                self.Est_birthdate = Est_birthdate
                self.Registration_number = Registration_number
                self.RFID_tag = RFID_tag
                self.Starting_weight = Starting_weight
                self.Hanging_weight = Hanging_weight
                self.Chargebacks = Chargebacks
                self.Starting_date_of_feed = Starting_date_of_feed
                self.Feed_method = Feed_method
                self.Type_of_pasture = Type_of_pasture
                self.Type_of_feed = Type_of_feed
                self.Est_completion_date = Est_completion_date
                self.Est_finished_weight = Est_finished_weight
                self.Est_price_to_be_paid = Est_price_to_be_paid
                self.Quantity = Quantity
                self.Comments = Comments
                self.Price_paid = Price_paid
                self.Delivered_date = Delivered_date
                self.Delivered_to = Delivered_to
                self.Status = Status
                
	def __str__(self):
		return f'Offered Item=id: {self.id}, UserId: {self.Users_id}, Product Name: {self.Product_name}, Breed: {self.Breed}, Single Brand: {self.Single_brand}, Est. Birthday: {self.Est_birthdate}, Registration Number: {self.Registration_number},RFID Tag: {self.RFID_tag}, Starting Weight: {self.Starting_weight}, Hanging Weight: {self.Hanging_weight}, Charge Backs: {self.Chargebacks}, Start Date Of Feed: {self.Starting_date_of_feed}, Feed Method: {self.Feed_method}, Type of Pasture: {self.Type_of_pasture}, Type of Feed: {self.Type_of_feed}, Est. Completion Date: {self.Est_completion_date}, Est. Finished Weight: {self.Est_finished_weight}, Est. Price: {self.Est_price_to_be_paid}, Qty: {self.Quantity}, Comments: {self.Comments}, Price Paid: {self.Price_paid}, Delivered Date: {self.Delivered_date}, Delivered To: {self.Delivered_to}, Status: {self.Status}'

	def __repr__(self):
		return self.__str__()