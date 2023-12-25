# Generated by Django 4.2.7 on 2023-12-22 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_animal_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('picture', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('animal_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='app.item')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
