from django.contrib import admin
from app.models import *

class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'start', 'start_amount']

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['date', 'from_account', 'to_account', 'amount', 'description']
    list_filter = ['from_account', 'to_account', 'description']

# Register your models here.
admin.site.register(AccountType)
admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
