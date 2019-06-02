# Generated by Django 2.2.1 on 2019-05-03 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20190503_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='controlled_ip',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='controlling_ip',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='iptables',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mark',
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controlling_ip', models.GenericIPAddressField(null=True, verbose_name='控制设备ip')),
                ('controlled_ip', models.GenericIPAddressField(null=True, verbose_name='被控制设备ip')),
                ('mark', models.IntegerField(null=True, verbose_name='mark标记值')),
                ('iptables', models.TextField(max_length=2048, null=True, verbose_name='iptables字符串')),
                ('status', models.BooleanField(default=False, verbose_name='默认为未shaping')),
                ('profile_pk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Profile', verbose_name='profile规则编号')),
            ],
        ),
    ]