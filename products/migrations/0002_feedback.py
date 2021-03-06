# Generated by Django 3.0.6 on 2020-05-28 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(verbose_name='Отправить ответ на e-mail')),
                ('email_adress', models.CharField(blank=True, max_length=500, verbose_name='e-mail адрес для ответа')),
                ('email_reply_capt', models.CharField(blank=True, max_length=500, verbose_name='Заголовок ответа на e-mail')),
                ('email_reply_text', models.TextField(blank=True, null=True, verbose_name='Текст ответа на e-mail')),
            ],
        ),
    ]
