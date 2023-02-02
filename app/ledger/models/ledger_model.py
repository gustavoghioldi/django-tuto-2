import uuid
from django.db import models
from ledger.models.account_model import AccountModel


class LedgerType(models.Choices):
    IN = "IN"
    OUT = "OUT"


class LedgerModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    client_id = models.ForeignKey(AccountModel, on_delete=models.DO_NOTHING)
    ledger_type = models.CharField(max_length=12, choices=LedgerType.choices)
    amount = models.FloatField(default=0.0)
    description = models.TextField(default="No description", blank=True)
