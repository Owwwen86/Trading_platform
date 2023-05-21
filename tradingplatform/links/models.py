from django.db import models


class Contact(models.Model):
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    Email = models.EmailField()
    Country = models.CharField(verbose_name="Страна", max_length=30)
    City = models.CharField(verbose_name="Город", max_length=30)
    Street = models.CharField(verbose_name="Улица", max_length=30)
    HouseNumber = models.PositiveSmallIntegerField(verbose_name="Номер дома")

    def __str__(self):
        return f'{self.Email}, {self.Country}, {self.City}'


class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField(verbose_name="Название", max_length=30)
    model = models.CharField(verbose_name="Модель", max_length=30)
    DateOfAppearance = models.DateTimeField(verbose_name="Дата выхода на рынок", auto_now_add=False)

    def __str__(self):
        return f'{self.name}, {self.model}, {self.DateOfAppearance} '


class Link(models.Model):
    class Meta:
        verbose_name = "Звено"
        verbose_name_plural = "Звенья"

    class Level(models.IntegerChoices):
        Factory = 0, "Завод"
        RetailNetwork = 1, "Розничная сеть"
        Entrepreneur = 2, "Индивидуальный предприниматель"

    level = models.PositiveSmallIntegerField(
        verbose_name="Уровень", choices=Level.choices, default=Level.Factory
    )
    contacts = models.ForeignKey(Contact, verbose_name='Контакты', on_delete=models.PROTECT)
    name = models.CharField(verbose_name="Название", max_length=30)
    products = models.ManyToManyField(Product, verbose_name='Продукты')
    provider = models.ForeignKey('self', verbose_name='Поставщик', on_delete=models.PROTECT, blank=True, null=True,
                                 related_name='provider_level', )
    debt = models.DecimalField(verbose_name='Задолженность перед поставщиком', max_digits=19, decimal_places=2)
    TimeCreate = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)

    @property
    def is_level(self):
        if self.provider is None:
            self.level = 0
            self.save()
            return self.level
        if self.provider.level == 0:
            self.level = 1
            self.save()
            return self.level
        if self.provider.level == 1:
            self.level = 2
            self.save()
            return self.level
        if self.provider.level == 2:
            self.level = 2
            self.save()
            return self.level

    def __str__(self):
        return f'{self.name}, {self.is_level}'
