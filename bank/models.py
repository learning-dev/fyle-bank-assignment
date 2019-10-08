from django.db import models


class Bank(models.Model):
	ifsc_code = models.CharField(max_length=11, primary_key=True)
	bank_id = models.IntegerField()
	bank_name = models.CharField(max_length=50)
	branch = models.CharField(max_length=80)
	addres = models.CharField(max_length=200)
	city = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	state = models.CharField(max_length=50) 

	def __str__(self):
		return self.ifsc_code + '-' + self.bank_name 


	@staticmethod
	def get_bank_by_ifsc(bank_ifsc):
		try:
			bank_list = Bank.objects.get(ifsc_code=bank_ifsc)
		except Exception as e:
			raise e
			bank_list = None
		
		return bank_list

	@staticmethod
	def get_branch_in_city(bank_name, city):
		try:
			branch_list = Bank.objects.filter(bank_name=bank_name, city=city)
		except Exception as e:
			branch_list = []

		return branch_list
