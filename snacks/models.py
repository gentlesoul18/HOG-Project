from django.db import models

class Snack(models.Model):
    PEANUT = 'P'
    CHINCHIN = 'C'
    JAM_DOUGHNUT = 'J'
    RING_DOUGHNUT = 'R'
    PUFF_PUFF = 'PU'
    BUNS = 'B'
    FISH_PIE = 'FP'
    FISH_ROLL = 'FR'
    EGG_ROLL = 'ER'
    SMALL_CHOPS = 'S'


    SNACK_CHOICES =[
        (PEANUT, 'P'),
        (CHINCHIN, 'C'),
        (JAM_DOUGHNUT, 'J'),
        (RING_DOUGHNUT, 'R'),
        (PUFF_PUFF, 'PU'),
        (BUNS, 'B'),
        (FISH_PIE, 'FP'),
        (FISH_ROLL, 'FR'),
        (EGG_ROLL, 'ER'),
        (SMALL_CHOPS, 'S')
    ]
    name = models.CharField(max_length=2, verbose_name="Snack Type", choices=SNACK_CHOICES, help_text="The snack you want to order")
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()


class Customer(models.Model):
    first_name = models.CharField(max_length=100, help_text="Your first name(i.e; your name that people call you)")
    last_name = models.CharField(max_length=100, verbose_name= 'Surname')
    mail = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)


class Order(models.Model):
    PAYMENT_CHOICE=[
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('F', 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICE, default='P')
    ordered_product = models.ForeignKey(Snack, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
