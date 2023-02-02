from django.db.models.signals import post_save
from django.dispatch import receiver

from ledger.models.ledger_model import LedgerModel, LedgerType
from ledger.models.account_model import AccountModel


@receiver(post_save, sender=LedgerModel)
def ledger_model_post_save(sender, instance: LedgerModel, created, **kwargs):
    if created:
        if instance.ledger_type == LedgerType.IN.value:
            instance.client_id.amount += instance.amount
        if instance.ledger_type == LedgerType.OUT.value:
            instance.client_id.amount -= instance.amount
        instance.client_id.save()
