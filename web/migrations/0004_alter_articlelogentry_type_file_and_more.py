# Generated by Django 4.0.4 on 2022-07-01 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0003_alter_article_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlelogentry',
            name='type',
            field=models.TextField(choices=[('source', 'Source'), ('title', 'Title'), ('name', 'Name'), ('tags', 'Tags'), ('new', 'New'), ('parent', 'Parent'), ('file_added', 'Fileadded'), ('file_deleted', 'Filedeleted'), ('file_renamed', 'Filerenamed')], verbose_name='Тип'),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название файла')),
                ('media_name', models.TextField(verbose_name='Название файла в ФС-хранилище')),
                ('mime_type', models.TextField(verbose_name='MIME-тип')),
                ('size', models.PositiveBigIntegerField(verbose_name='Размер файла')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('deleted_at', models.DateTimeField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.article', verbose_name='Статья')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_files', to=settings.AUTH_USER_MODEL, verbose_name='Автор файла')),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_files', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, удаливший файл')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.site', verbose_name='Сайт')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.AddIndex(
            model_name='file',
            index=models.Index(fields=['article', 'name'], name='web_file_article_c1ccbd_idx'),
        ),
        migrations.AddConstraint(
            model_name='file',
            constraint=models.UniqueConstraint(fields=('site', 'article', 'name', 'deleted_at'), name='web_file_unique'),
        ),
    ]