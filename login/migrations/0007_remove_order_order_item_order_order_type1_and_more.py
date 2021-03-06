# Generated by Django 4.0.1 on 2022-02-22 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_remove_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_item',
        ),
        migrations.AddField(
            model_name='order',
            name='order_type1',
            field=models.CharField(choices=[('Sushi', 'Sushi'), ('Okonomiyaki', 'Okonomiyaki'), ('Gyoza', 'Gyoza'), ('Mochi', 'Mochi'), ('Kushiyaki', 'Kushiyaki'), ('None', 'None')], default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='order_type2',
            field=models.CharField(choices=[('Milo ice', 'Milo ice'), ('Chrysanthemum Tea', 'Chrysanthemum Tea'), ('Watermelon juice ', 'Watermelon juice '), ('Orange Juice', 'Orange Juice'), ('Lemon tea', 'Lemon tea'), ('None', 'None')], default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='order_type3',
            field=models.CharField(choices=[('Hainan Chicken Rice', 'Hainan Chicken Rice'), ('Nasi Lemak', 'Nasi Lemak'), ('Fried rice ', 'Fried rice '), ('indian Style rice', 'Indian Style rice'), ('Economy rice', 'Economy rice'), ('None', 'None')], default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='order_type4',
            field=models.CharField(choices=[('Walnut and Lentil Bolognese ', 'Walnut and Lentil Bolognese '), ('Vegan Roasted Sweet Potato Salad', 'Vegan Roasted Sweet Potato Salad'), ('Shaved Brussels Sprout Salad  ', 'Shaved Brussels Sprout Salad  '), ('Vegetarian Burrito Bowl with Avocado Crema', 'Vegetarian Burrito Bowl with Avocado Crema'), ('Green Curry Buddha Bowl', 'Green Curry Buddha Bowl'), ('None', 'None')], default='None', max_length=50),
        ),
    ]
