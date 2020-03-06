# Generated by Django 2.2.6 on 2019-12-15 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_userinfo_user_type_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.UserGroup'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(error_messages={'required': '请输入密码:'}, help_text='pwd', max_length=64),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(blank=True, max_length=32, verbose_name='用户名'),
        ),
    ]
