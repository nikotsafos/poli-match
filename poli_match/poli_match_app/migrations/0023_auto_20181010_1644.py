# Generated by Django 2.1.1 on 2018-10-10 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poli_match_app', '0022_auto_20181010_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='missed_votes_pct',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='politician',
            name='state_rank',
            field=models.CharField(default=True, max_length=101, null=True),
        ),
        migrations.AlterField(
            model_name='politician',
            name='url',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='politician',
            name='votes_with_party_pct',
            field=models.FloatField(default=0),
        ),
    ]
