from django.contrib import admin
from ledger.models.ledger_model import LedgerModel


@admin.register(LedgerModel)
class LedgerAdmin(admin.ModelAdmin):
    pass
