# Generated by Django 5.0.7 on 2024-07-29 16:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgchart', '0007_alter_sysuser_department_alter_sysuser_division_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commondepartment',
            options={'verbose_name': 'Common Department', 'verbose_name_plural': 'Common Departments'},
        ),
        migrations.RemoveField(
            model_name='commondepartment',
            name='department_name',
        ),
        migrations.AddField(
            model_name='commondepartment',
            name='department',
            field=models.CharField(blank=True, choices=[('営業本部', '営業本部 Sales Division'), ('システム事業部', 'システム事業部 System Division'), ('ITサポート事業部', 'Itサポート事業部 It Support Division'), ('管理部', '管理部 Management Department'), ('N/A', 'N A')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='commondepartment',
            name='division',
            field=models.CharField(blank=True, choices=[('ソリューション営業部', 'ソリューション営業部 Solution Sales Department'), ('研究開発課', '研究開発課 Research And Development Section'), ('システム課', 'システム課 System Section'), ('SW開発課', 'Sw開発課 Software Development Section'), ('購買調達部', '購買調達部 Purchasing And Procurement Department'), ('N/A', 'N A')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='commondepartment',
            name='group',
            field=models.CharField(blank=True, choices=[('1G', 'G1'), ('2G', 'G2'), ('3G', 'G3'), ('4G', 'G4'), ('N/A', 'N A')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='commondepartment',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Department Name'),
        ),
        migrations.AddField(
            model_name='commondepartment',
            name='section',
            field=models.CharField(blank=True, choices=[('1課', '課 1'), ('2課', '課 2'), ('N/A', 'N A')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='commondepartment',
            name='department_head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_head', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='commondepartment',
            name='primary_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_contact', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sysuser',
            name='division',
            field=models.CharField(blank=True, choices=[('ソリューション営業部', 'ソリューション営業部 Solution Sales Department'), ('研究開発課', '研究開発課 Research And Development Section'), ('システム課', 'システム課 System Section'), ('SW開発課', 'Sw開発課 Software Development Section'), ('購買調達部', '購買調達部 Purchasing And Procurement Department'), ('N/A', 'N A')], max_length=255, null=True),
        ),
    ]
