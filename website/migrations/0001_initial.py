# Generated by Django 3.2 on 2021-04-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DvsInfoDbAkbCsv',
            fields=[
                ('id_akb', models.IntegerField(db_column='id_AKB', primary_key=True, serialize=False)),
                ('reģions', models.CharField(blank=True, db_column='Reģions', max_length=2, null=True)),
                ('nodaļa', models.CharField(blank=True, db_column='Nodaļa', max_length=10, null=True)),
                ('iezīme', models.CharField(blank=True, db_column='Iezīme', max_length=10, null=True)),
                ('objekts', models.CharField(blank=True, db_column='Objekts', max_length=18, null=True)),
                ('akb_ražotājs_un_nomināli', models.CharField(blank=True, db_column='AKB_Ražotājs_un_nomināli', max_length=36, null=True)),
                ('akb_skaits', models.IntegerField(blank=True, db_column='AKB_skaits', null=True)),
                ('akb_izmērītais_ah', models.CharField(blank=True, db_column='AKB_izmērītais_Ah', max_length=25, null=True)),
                ('akb_iekšējā_pretestība_mom', models.IntegerField(blank=True, db_column='AKB_iekšējā_pretestība_mOm', null=True)),
                ('uzstādīšanas_vieta', models.CharField(blank=True, db_column='Uzstādīšanas_vieta', max_length=20, null=True)),
                ('uzstādīšanas_gads', models.CharField(blank=True, db_column='Uzstādīšanas_gads', max_length=20, null=True)),
                ('akb_izgatavošanas_partija_vai_datums', models.CharField(blank=True, db_column='AKB_izgatavošanas_partija_vai_datums', max_length=23, null=True)),
                ('pārbaudes_datums', models.CharField(blank=True, db_column='Pārbaudes_datums', max_length=13, null=True)),
                ('nākošā_pārbaude', models.CharField(blank=True, db_column='Nākošā_pārbaude', max_length=10, null=True)),
                ('piezīme', models.CharField(blank=True, db_column='Piezīme', max_length=59, null=True)),
            ],
            options={
                'db_table': 'DVS_info_DB_AKB_csv',
            },
        ),
        migrations.CreateModel(
            name='DvsInfoDbCsv',
            fields=[
                ('reģions', models.CharField(blank=True, db_column='Reģions', max_length=2, null=True)),
                ('nodaļa', models.CharField(blank=True, db_column='Nodaļa', max_length=10, null=True)),
                ('iezīme', models.CharField(blank=True, db_column='Iezīme', max_length=10, null=True)),
                ('objekts', models.CharField(db_column='Objekts', max_length=26, primary_key=True, serialize=False)),
                ('objekta_nosaukums', models.CharField(blank=True, db_column='Objekta_nosaukums', max_length=27, null=True)),
                ('adrese', models.CharField(blank=True, db_column='Adrese', max_length=87, null=True)),
                ('atbidības_teritorija', models.CharField(blank=True, db_column='Atbidības_teritorija', max_length=46, null=True)),
                ('tehn_id', models.CharField(blank=True, db_column='Tehn_ID', max_length=22, null=True)),
                ('gps_n', models.CharField(blank=True, db_column='GPS_N', max_length=14, null=True)),
                ('gps_e', models.CharField(blank=True, db_column='GPS_E', max_length=13, null=True)),
                ('ģis_x', models.FloatField(blank=True, db_column='ĢIS_X', null=True)),
                ('ģis_y', models.FloatField(blank=True, db_column='ĢIS_Y', null=True)),
                ('pieslēguma_veids', models.CharField(blank=True, db_column='Pieslēguma_veids', max_length=24, null=True)),
                ('darbs_ar_2_centriem', models.CharField(blank=True, db_column='Darbs_ar_2_centriem', max_length=18, null=True)),
                ('garantētā_barošana', models.CharField(blank=True, db_column='Garantētā_barošana', max_length=24, null=True)),
                ('rtu_ražotājs', models.CharField(blank=True, db_column='RTU_ražotājs', max_length=21, null=True)),
                ('rtu_2_ražotājs', models.CharField(blank=True, db_column='RTU_2_ražotājs', max_length=22, null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=13, null=True)),
                ('rtu_ip_adrese', models.CharField(blank=True, db_column='RTU_IP_adrese', max_length=81, null=True)),
                ('nfe_tabula', models.CharField(blank=True, db_column='NFE_tabula', max_length=49, null=True)),
                ('protokols_ar_scada', models.CharField(blank=True, db_column='Protokols_ar_SCADA', max_length=16, null=True)),
                ('protokols_ar_ast', models.CharField(blank=True, db_column='Protokols_ar_AST', max_length=17, null=True)),
                ('dpp_1_saite_ar_slēgiekārtu', models.CharField(blank=True, db_column='DPP_1_saite_ar_slēgiekārtu', max_length=15, null=True)),
                ('dpp_2_saite_ar_slēgiekārtu', models.CharField(blank=True, db_column='DPP_2_saite_ar_slēgiekārtu', max_length=15, null=True)),
                ('js', models.CharField(blank=True, db_column='JS', max_length=15, null=True)),
                ('io', models.CharField(blank=True, db_column='IO', max_length=15, null=True)),
                ('ts', models.CharField(blank=True, db_column='TS', max_length=15, null=True)),
                ('tv', models.CharField(blank=True, db_column='TV', max_length=9, null=True)),
                ('tm', models.IntegerField(blank=True, db_column='TM', null=True)),
                ('rekonstrukcijas_gads', models.IntegerField(blank=True, db_column='Rekonstrukcijas_gads', null=True)),
                ('vec_komp_gads', models.IntegerField(blank=True, db_column='Vec_komp_gads', null=True)),
                ('piezīme', models.CharField(blank=True, db_column='Piezīme', max_length=255, null=True)),
            ],
            options={
                'db_table': 'DVS_info_DB_csv',
            },
        ),
        migrations.CreateModel(
            name='DvsInfoDbRaaIekrtaCsv',
            fields=[
                ('id_raa', models.IntegerField(db_column='id_RAA', primary_key=True, serialize=False)),
                ('reģions', models.CharField(blank=True, db_column='Reģions', max_length=2, null=True)),
                ('nodaļa', models.CharField(blank=True, db_column='Nodaļa', max_length=10, null=True)),
                ('iezīme', models.CharField(blank=True, db_column='Iezīme', max_length=5, null=True)),
                ('objekts', models.CharField(blank=True, db_column='Objekts', max_length=14, null=True)),
                ('raa_ražotājs', models.CharField(blank=True, db_column='RAA_Ražotājs', max_length=16, null=True)),
                ('raa_modelis', models.CharField(blank=True, db_column='RAA_Modelis', max_length=17, null=True)),
                ('raa_daudzums', models.IntegerField(blank=True, db_column='RAA_daudzums', null=True)),
                ('raa_protokols', models.CharField(blank=True, db_column='RAA_Protokols', max_length=15, null=True)),
                ('raa_interface', models.CharField(blank=True, db_column='RAA_Interface', max_length=15, null=True)),
                ('raa_pieslegums', models.CharField(blank=True, db_column='RAA_pieslegums', max_length=13, null=True)),
                ('piezime', models.CharField(blank=True, db_column='Piezime', max_length=42, null=True)),
            ],
            options={
                'db_table': 'DVS_info_DB_RAA_iekārta_csv',
            },
        ),
        migrations.CreateModel(
            name='DvsInfoDbRtuIekrtaCsv',
            fields=[
                ('id_rtu', models.IntegerField(db_column='id_RTU', primary_key=True, serialize=False)),
                ('reģions', models.CharField(blank=True, db_column='Reģions', max_length=2, null=True)),
                ('nodaļa', models.CharField(blank=True, db_column='Nodaļa', max_length=10, null=True)),
                ('iezīme', models.CharField(blank=True, db_column='Iezīme', max_length=5, null=True)),
                ('objekts', models.CharField(blank=True, db_column='Objekts', max_length=17, null=True)),
                ('tips', models.CharField(blank=True, db_column='Tips', max_length=23, null=True)),
                ('iekārtas_ražotājs', models.CharField(blank=True, db_column='Iekārtas_Ražotājs', max_length=17, null=True)),
                ('modelis', models.CharField(blank=True, db_column='Modelis', max_length=22, null=True)),
                ('daudzums', models.IntegerField(blank=True, db_column='Daudzums', null=True)),
                ('uzstadīšanas_vieta', models.CharField(blank=True, db_column='Uzstadīšanas_vieta', max_length=21, null=True)),
                ('programmaturas_versija', models.CharField(blank=True, db_column='Programmaturas_versija', max_length=34, null=True)),
                ('piezime', models.CharField(blank=True, db_column='Piezime', max_length=66, null=True)),
                ('column13', models.CharField(blank=True, db_column='Column13', max_length=18, null=True)),
                ('column14', models.CharField(blank=True, db_column='Column14', max_length=18, null=True)),
                ('column15', models.CharField(blank=True, db_column='Column15', max_length=1, null=True)),
            ],
            options={
                'db_table': 'DVS_info_DB_RTU_iekārta_csv',
            },
        ),
    ]
