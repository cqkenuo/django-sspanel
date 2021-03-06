# Generated by Django 3.0.6 on 2020-06-21 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sspanel", "0049_auto_20200619_0820"),
    ]

    operations = [
        migrations.AddField(
            model_name="relaynode",
            name="ehco_listen_host",
            field=models.CharField(
                blank=True, max_length=64, null=True, verbose_name="隧道监听地址"
            ),
        ),
        migrations.AddField(
            model_name="relaynode",
            name="ehco_listen_port",
            field=models.CharField(
                blank=True, max_length=64, null=True, verbose_name="隧道监听端口"
            ),
        ),
        migrations.AddField(
            model_name="relaynode",
            name="ehco_listen_type",
            field=models.CharField(
                choices=[("raw", "raw"), ("wss", "wss"), ("mwss", "mwss")],
                default="raw",
                max_length=64,
                verbose_name="隧道监听类型",
            ),
        ),
        migrations.AddField(
            model_name="relaynode",
            name="ehco_transport_type",
            field=models.CharField(
                choices=[("raw", "raw"), ("wss", "wss"), ("mwss", "mwss")],
                default="raw",
                max_length=64,
                verbose_name="隧道传输类型",
            ),
        ),
        migrations.AddField(
            model_name="ssnode",
            name="ehco_listen_host",
            field=models.CharField(
                blank=True, max_length=64, null=True, verbose_name="隧道监听地址"
            ),
        ),
        migrations.AddField(
            model_name="ssnode",
            name="ehco_listen_port",
            field=models.CharField(
                blank=True, max_length=64, null=True, verbose_name="隧道监听端口"
            ),
        ),
        migrations.AddField(
            model_name="ssnode",
            name="ehco_listen_type",
            field=models.CharField(
                choices=[("raw", "raw"), ("wss", "wss"), ("mwss", "mwss")],
                default="raw",
                max_length=64,
                verbose_name="隧道监听类型",
            ),
        ),
        migrations.AddField(
            model_name="ssnode",
            name="ehco_transport_type",
            field=models.CharField(
                choices=[("raw", "raw"), ("wss", "wss"), ("mwss", "mwss")],
                default="raw",
                max_length=64,
                verbose_name="隧道传输类型",
            ),
        ),
        migrations.AddField(
            model_name="ssrelayrule",
            name="listen_type",
            field=models.CharField(
                choices=[("raw", "raw"), ("wss", "wss"), ("mwss", "mwss")],
                default="raw",
                max_length=64,
                verbose_name="监听类型",
            ),
        ),
        migrations.AddField(
            model_name="ssrelayrule",
            name="transport_type",
            field=models.CharField(
                choices=[("raw", "raw"), ("wss", "wss"), ("mwss", "mwss")],
                default="raw",
                max_length=64,
                verbose_name="传输类型",
            ),
        ),
        migrations.AddField(
            model_name="vmessnode",
            name="ehco_listen_host",
            field=models.CharField(
                blank=True, max_length=64, null=True, verbose_name="隧道监听地址"
            ),
        ),
        migrations.AddField(
            model_name="vmessnode",
            name="ehco_listen_port",
            field=models.CharField(
                blank=True, max_length=64, null=True, verbose_name="隧道监听端口"
            ),
        ),
        migrations.AddField(
            model_name="vmessnode",
            name="ehco_listen_type",
            field=models.CharField(
                choices=[("raw", "raw"), ("wss", "wss"), ("mwss", "mwss")],
                default="raw",
                max_length=64,
                verbose_name="隧道监听类型",
            ),
        ),
        migrations.AddField(
            model_name="vmessnode",
            name="ehco_transport_type",
            field=models.CharField(
                choices=[("raw", "raw"), ("wss", "wss"), ("mwss", "mwss")],
                default="raw",
                max_length=64,
                verbose_name="隧道传输类型",
            ),
        ),
        migrations.AddField(
            model_name="vmessrelayrule",
            name="listen_type",
            field=models.CharField(
                choices=[("raw", "raw"), ("wss", "wss"), ("mwss", "mwss")],
                default="raw",
                max_length=64,
                verbose_name="监听类型",
            ),
        ),
        migrations.AddField(
            model_name="vmessrelayrule",
            name="transport_type",
            field=models.CharField(
                choices=[("raw", "raw"), ("wss", "wss"), ("mwss", "mwss")],
                default="raw",
                max_length=64,
                verbose_name="传输类型",
            ),
        ),
        migrations.AlterField(
            model_name="ssrelayrule",
            name="relay_node",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="ss_relay_rules",
                to="sspanel.RelayNode",
                verbose_name="中转节点",
            ),
        ),
        migrations.AlterField(
            model_name="vmessrelayrule",
            name="relay_node",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="vmess_relay_rules",
                to="sspanel.RelayNode",
                verbose_name="中转节点",
            ),
        ),
    ]
