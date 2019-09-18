# Generated by Django 2.2.5 on 2019-09-14 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20190912_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='state',
            field=models.CharField(choices=[('PB', 'Published'), ('DR', 'Draft')], default='DR', max_length=2, verbose_name='Article state'),
        ),
    ]
