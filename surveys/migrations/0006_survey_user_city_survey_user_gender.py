# Generated by Django 4.1.4 on 2022-12-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0005_survey_best_brand_survey_buy_before_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='user_city',
            field=models.CharField(blank=True, default='city', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='user_gender',
            field=models.CharField(blank=True, default='Male', max_length=150, null=True),
        ),
    ]