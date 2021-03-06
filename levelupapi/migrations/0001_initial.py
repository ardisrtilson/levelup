# Generated by Django 3.1.2 on 2020-11-30 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('maker', models.CharField(max_length=50)),
                ('number_of_players', models.CharField(max_length=50)),
                ('skill_level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='gameType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=50)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.game')),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=50)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('imgURL', models.CharField(max_length=50)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.game')),
                ('sumbitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer'),
        ),
        migrations.AddField(
            model_name='game',
            name='gametype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gametype'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.game')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer')),
            ],
        ),
    ]
