# Generated by Django 4.0.1 on 2022-02-15 06:38

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
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Brief description of the bug.', max_length=500)),
                ('is_resolved', models.BooleanField(default=False, verbose_name='Resolved')),
                ('priority', models.CharField(choices=[('Low', 'Low'), ('Urgent', 'Urgent'), ('Critical', 'Critical')], default='Low', max_length=8)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date ticket was created.')),
                ('last_updated', models.DateTimeField(auto_now=True, help_text='Date ticket was last modified.')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(help_text='The project this ticket is associated with.', on_delete=django.db.models.deletion.CASCADE, to='bugs.project')),
            ],
        ),
        migrations.CreateModel(
            name='TicketComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date ticket comment was created.')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bugs.ticket')),
            ],
        ),
    ]