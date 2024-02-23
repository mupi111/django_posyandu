# Generated by Django 4.1.3 on 2022-11-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Siposyandu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(max_length=17, verbose_name='NIK')),
                ('nama', models.CharField(max_length=50, verbose_name='Nama Anak')),
                ('tmpt_lahir', models.CharField(max_length=30, verbose_name='Tempat Lahir')),
                ('jk', models.CharField(choices=[('l', 'Laki-laki'), ('p', 'Perempuan')], max_length=2, verbose_name='Jenis Kelamin')),
                ('bb', models.CharField(max_length=3, verbose_name='Berat Badan')),
                ('tb', models.CharField(max_length=3, verbose_name='Tinggi Badan')),
                ('nama_ayah', models.CharField(max_length=50, verbose_name='Nama Ayah')),
                ('nama_ibu', models.CharField(max_length=50, verbose_name='Nama Ibu')),
                ('agama', models.CharField(choices=[('is', 'Islam'), ('kk', 'Kristen Katolik'), ('kp', 'Kristen Protestan'), ('hi', 'Hindu'), ('bu', 'Budha')], max_length=50, verbose_name='Agama')),
            ],
        ),
    ]