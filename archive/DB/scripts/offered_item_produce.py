class Offered_item_produce(object):
	def __init__(self,
                Id,
                Users_id,
                Product_name,
                Package_type,
                Date_planted,
                Seed_type,
                Modified_seed,
                Heirloom,
                Fertilizer_type_used,
                Pesticide_type_used,
                Estimated_qty_planted,
                GMO,
                Estimated_finished_qty,
                Est_price_to_be_paid,
                Qty_accepted_for_listing,
                Qty_accepted_at_delivery,
                Chargebacks,
                Price_paid,
                Delivered_date,
                Delivered_to,
                Comments,
                Status):
                self.id = Id
                self.Users_id = Users_id
                self.Product_name = Product_name
                self.Package_type = Package_type
                self.Date_planted = Date_planted
                self.Seed_type = Seed_type
                self.Modified_seed = Modified_seed
                self.Heirloom = Heirloom
                self.Fertilizer_type_used = Fertilizer_type_used
                self.Pesticide_type_used = Pesticide_type_used
                self.Estimated_qty_planted = Estimated_qty_planted
                self.GMO = GMO
                self.Estimated_finished_qty = Estimated_finished_qty
                self.Est_price_to_be_paid = Est_price_to_be_paid
                self.Qty_accepted_for_listing = Qty_accepted_for_listing
                self.Qty_accepted_at_delivery = Qty_accepted_at_delivery
                self.Chargebacks = Chargebacks
                self.Price_paid = Price_paid
                self.Delivered_date = Delivered_date
                self.Delivered_to = Delivered_to
                self.Comments = Comments
                self.Status = Status
	def __str__(self):
		return f'Offered Item=id: {self.id}, UserId: {self.Users_id}, Product Name: {self.Product_name}, Package Type: {self.Package_type}, Date Planted: {self.Date_planted}, Seed Type: {self.Seed_type}, Modified Seed: {self.Modified_seed}, Heirloom: {self.Heirloom}, Fertilizer Type: {self.Fertilizer_type_used}, Pesticide Type: {self.Pesticide_type_used}, Est. Qty. Planted: {self.Estimated_qty_planted}, GMO: {self.GMO}, Est. Finished Qty: {self.Estimated_finished_qty}, Est. Price: {self.Est_price_to_be_paid}, Qty Accepted For Listing: {self.Qty_accepted_for_listing}, Qty Accepted At Delivery: {self.Qty_accepted_at_delivery}, Chargebacks: {self.Chargebacks}, Final Price: {self.Price_paid}, Delivered Date: {self.Delivered_date}, Delivered To: {self.Delivered_to}, Comments: {self.Comments}, Status: {self.Status}'

	def __repr__(self):
		return self.__str__()