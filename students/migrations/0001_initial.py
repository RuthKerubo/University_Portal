# Generated by Django 2.2.7 on 2019-11-26 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=13, unique=True)),
                ('level_of_study', models.CharField(choices=[('Cert', 'Certificate'), ('Dip', 'Diploma'), ('Deg', 'Degree'), ('Mst', 'Master')], max_length=15)),
                ('sponsor', models.CharField(choices=[('Govt', 'Government'), ('Self', 'Self'), ('Other', 'Other')], max_length=15)),
                ('year_joined', models.IntegerField(default=2019)),
                ('semester_joined', models.CharField(choices=[('Jan-Apr', 'Jan - Apr'), ('May-Aug', 'May - Aug'), ('Sept-Dec', 'Sept - Dec')], max_length=15)),
                ('national_id', models.IntegerField(unique=True)),
                ('date_of_birth', models.DateField()),
                ('nhif_owner', models.CharField(choices=[('Self', 'Self'), ('Guardian', 'Guardian')], max_length=15)),
                ('nhif_membership_no', models.IntegerField(unique=True)),
                ('nhif_is_card_valid', models.BooleanField(default=False)),
                ('nhif_valid_until', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
    ]
