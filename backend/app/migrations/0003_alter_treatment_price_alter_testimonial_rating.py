import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_testimonial_rating_alter_monthlyoffer_active_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="treatment",
            name="price",
            field=models.CharField(max_length=20, null=True, verbose_name="Preise"),
        ),
        migrations.AlterField(
            model_name="testimonial",
            name="rating",
            field=models.IntegerField(
                default=5,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
                verbose_name="Bewertung",
            ),
        ),
    ]
