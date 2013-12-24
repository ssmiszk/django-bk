from django.db import models

class AccountType(models.Model):
	name = models.CharField(max_length=100, unique=True)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.__unicode__()

class Account(models.Model):
	type = models.ForeignKey(AccountType)
	name = models.CharField(max_length=100, unique=True)
	start = models.DateField(default='1970-01-01', blank=True)
	start_amount = models.DecimalField(max_digits=10, decimal_places=0, default=0, blank=True)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.__unicode__()

class Transaction(models.Model):
	date = models.DateField()
	from_account = models.ForeignKey(Account, related_name='+')
	to_account = models.ForeignKey(Account, related_name='+')
	amount = models.DecimalField(max_digits=10, decimal_places=0)
	description = models.CharField(max_length=200, null=True, blank=True)
	def __unicode__(self):
		return u"%s:%s->%s %d (%s)" % (self.date, self.from_account, self.to_account, self.amount, self.description)
	def __str__(self):
		return self.__unicode__()
