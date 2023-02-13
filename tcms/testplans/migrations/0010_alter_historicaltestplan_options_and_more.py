# Generated by Django 4.1.3 on 2022-11-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("testplans", "0009_tree"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicaltestplan",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical test plan",
                "verbose_name_plural": "historical test plans",
            },
        ),
        migrations.AlterField(
            model_name="historicaltestplan",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
    ]
