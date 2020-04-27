from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class State(models.Model):
    state_name = models.CharField(max_length=50)
    state_base_tax = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.state_name + " " + (round(self.state_base_tax * 100,2)).__str__() + "%"


class State_Category_Tax(models.Model):
    id_cat = models.ForeignKey(Category, related_name="Category+", on_delete=models.DO_NOTHING)
    id_state = models.ForeignKey(State, related_name="State+", on_delete=models.DO_NOTHING)
    tax_val = models.FloatField(default=State(id_state).state_base_tax)

    def __str__(self):
        return "NAZWA STANU= " + self.id_state.state_name + " KATEGORIA= " + self.id_cat.category_name + " WARTOSC= " + self.tax_val.__str__()


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    id_cat = models.ForeignKey(Category, related_name="Category+", on_delete=models.DO_NOTHING)
    product_price = models.FloatField(validators=[MinValueValidator(0)])

    #
    # class Meta():
    #     ordering = ('-product_name',)
    def __str__(self):
        return "PRODUCT NAME " + self.product_name + " CATEGORY " + self.id_cat.category_name + " PRICE " + self.product_price.__str__()


class FormInfoHandler(models.Model):
    id_state = models.ForeignKey(State, related_name="State+", on_delete=models.DO_NOTHING)
    id_product = models.ForeignKey(Product, related_name="Product+", on_delete=models.DO_NOTHING)
    selling_price = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return "Product " + self.id_product.product_name + " in state " + self.id_state.state_name + " expected selling price " + self.selling_price.__str__()
