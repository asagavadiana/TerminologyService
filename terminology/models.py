from django.db import models

class Refbook(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'

    def __str__(self):
        return self.name

class RefbookVersion(models.Model):
    refbook = models.ForeignKey(Refbook, related_name='versions', on_delete=models.CASCADE)
    version = models.CharField(max_length=50)
    start_date = models.DateField()

    class Meta:
        unique_together = ('refbook', 'version')
        verbose_name = 'Версия справочника'
        verbose_name_plural = 'Версии справочников'

    def __str__(self):
        return f'{self.refbook.name} - {self.version}'

class RefbookElement(models.Model):
    refbook_version = models.ForeignKey(RefbookVersion, related_name='elements', on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    value = models.CharField(max_length=300)

    class Meta:
        unique_together = ('refbook_version', 'code')
        verbose_name = 'Элемент справочника'
        verbose_name_plural = 'Элементы справочников'

    def __str__(self):
        return self.value
