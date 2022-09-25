# Generated by Django 4.1.1 on 2022-09-19 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='PROJECT_FOR_THE_LESSON/image', verbose_name='PhotoN')),
                ('title', models.CharField(max_length=40)),
                ('preview_info', models.TextField()),
                ('information', models.TextField()),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.category')),
            ],
        ),
    ]
