class User(object):
	def __init__(self, id, first_name, last_name, p_number, s_number, email, f_name, f_location, area, is_producer, is_admin, is_other, member_since, f_type, rating, m_street, m_city, m_province, m_country, m_postal_code, b_street, b_city, b_province, b_country, b_postal_code, comments):
		self.id = id
		self.first_name = first_name
		self.last_name = last_name
		self.p_number = p_number
		self.s_number = s_number
		self.email = email
		self.f_name = f_name
		self.f_location = f_location
		self.area=area
		self.is_producer = is_producer
		self.is_admin = is_admin
		self.is_other = is_other
		self.member_since = member_since
		self.f_type = f_type
		self.rating = rating
		self.m_street = m_street
		self.m_city = m_city
		self.m_province = m_province
		self.m_country = m_country
		self.m_postal_code = m_postal_code
		self.b_street = b_street
		self.b_city = b_city
		self.b_province = b_province
		self.b_country = b_country
		self.b_postal_code = b_postal_code
		self.comments = comments

	def __str__(self):
		return f'User-id: {self.id}, first name: {self.first_name}, last name: {self.last_name}, primary number: {self.p_number}, secondary number: {self.s_number}, email: {self.email}, farm name: {self.f_name}, farm location: {self.f_location}, area: {self.area}, is producer: {self.is_producer}, is admin: {self.is_admin}, is other: {self.is_other}, member since: {self.member_since}, farm type: {self.f_type}, rating: {self.rating}, mailing street: {self.m_street}, mailing city: {self.m_city}, mailing province: {self.m_province}, mailing country: {self.m_country}, mailing postal code: {self.m_postal_code}, billing street: {self.b_street}, billing city: {self.b_city}, billing province: {self.b_province}, billing country: {self.b_country}, billing postal code: {self.b_postal_code}, comments: {self.comments}'

	def __repr__(self):
		return self.__str__()
