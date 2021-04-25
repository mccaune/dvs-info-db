# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RTUrazotajs(models.Model):
    rtu_ražotājs = models.CharField(db_column='RTU_ražotājs', max_length=50, primary_key=True)  # Field name made lowercase.
    rtu_count = models.IntegerField(db_column='RTU_count', blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return self.rtu_ražotājs + '... count:  ' + str(self.rtu_count) 

    class Meta:
        #managed = False
        db_table = 'RTU_razotaji'
        
class RTUvecums(models.Model):
    rtu_gads = models.IntegerField(db_column='Vec_komp_gads', primary_key=True)  # Field name made lowercase.
    rtu_skaits = models.IntegerField(db_column='rtu_skaits', blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return str(self.rtu_gads) + '... RTU skaits:  ' + str(self.rtu_skaits) 

    class Meta:
        #managed = False
        db_table = 'RTU_vecums'

        
class ObjektuSadalijums(models.Model):
    reģions = models.CharField(db_column='Reģions', max_length=50, primary_key=True)  # Field name made lowercase.
    objektu_skaits = models.IntegerField(db_column='RTU_count', blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return self.reģions + '... count:  ' + str(self.objektu_skaits) 

    class Meta:
        #managed = False
        db_table = 'Objektu_skaits_reģionos'


class DvsInfoDbAkbCsv(models.Model):
    id_akb = models.AutoField(db_column='id_AKB', primary_key=True)  # Field name made lowercase.
    reģions = models.CharField(db_column='Reģions', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nodaļa = models.CharField(db_column='Nodaļa', max_length=10, blank=True, null=True)  # Field name made lowercase.
    iezīme = models.CharField(db_column='Iezīme', max_length=10, blank=True, null=True)  # Field name made lowercase.
    objekts = models.CharField(db_column='Objekts', max_length=18, blank=True, null=True)  # Field name made lowercase.
    akb_ražotājs_un_nomināli = models.CharField(db_column='AKB_Ražotājs_un_nomināli', max_length=36, blank=True, null=True)  # Field name made lowercase.
    akb_skaits = models.IntegerField(db_column='AKB_skaits', blank=True, null=True)  # Field name made lowercase.
    akb_izmērītais_ah = models.CharField(db_column='AKB_izmērītais_Ah', max_length=25, blank=True, null=True)  # Field name made lowercase.
    akb_iekšējā_pretestība_mom = models.IntegerField(db_column='AKB_iekšējā_pretestība_mOm', blank=True, null=True)  # Field name made lowercase.
    uzstādīšanas_vieta = models.CharField(db_column='Uzstādīšanas_vieta', max_length=20, blank=True, null=True)  # Field name made lowercase.
    uzstādīšanas_gads = models.CharField(db_column='Uzstādīšanas_gads', max_length=20, blank=True, null=True)  # Field name made lowercase.
    akb_izgatavošanas_partija_vai_datums = models.CharField(db_column='AKB_izgatavošanas_partija_vai_datums', max_length=23, blank=True, null=True)  # Field name made lowercase.
    pārbaudes_datums = models.CharField(db_column='Pārbaudes_datums', max_length=13, blank=True, null=True)  # Field name made lowercase.
    nākošā_pārbaude = models.CharField(db_column='Nākošā_pārbaude', max_length=10, blank=True, null=True)  # Field name made lowercase.
    piezīme = models.CharField(db_column='Piezīme', max_length=59, blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return self.reģions + ' ' + self.nodaļa + ' ' + self.objekts

    class Meta:
        #managed = False
        db_table = 'DVS_info_DB_AKB_csv'


class DvsInfoDbRaaIekrtaCsv(models.Model):
    id_raa = models.AutoField(db_column='id_RAA', primary_key=True)  # Field name made lowercase.
    reģions = models.CharField(db_column='Reģions', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nodaļa = models.CharField(db_column='Nodaļa', max_length=10, blank=True, null=True)  # Field name made lowercase.
    iezīme = models.CharField(db_column='Iezīme', max_length=5, blank=True, null=True)  # Field name made lowercase.
    objekts = models.CharField(db_column='Objekts', max_length=14, blank=True, null=True)  # Field name made lowercase.
    raa_ražotājs = models.CharField(db_column='RAA_Ražotājs', max_length=16, blank=True, null=True)  # Field name made lowercase.
    raa_modelis = models.CharField(db_column='RAA_Modelis', max_length=17, blank=True, null=True)  # Field name made lowercase.
    raa_daudzums = models.IntegerField(db_column='RAA_daudzums', blank=True, null=True)  # Field name made lowercase.
    raa_protokols = models.CharField(db_column='RAA_Protokols', max_length=15, blank=True, null=True)  # Field name made lowercase.
    raa_interface = models.CharField(db_column='RAA_Interface', max_length=15, blank=True, null=True)  # Field name made lowercase.
    raa_pieslegums = models.CharField(db_column='RAA_pieslegums', max_length=13, blank=True, null=True)  # Field name made lowercase.
    piezime = models.CharField(db_column='Piezime', max_length=42, blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return self.reģions + ' ' + self.nodaļa + ' ' + self.objekts + ' ' + self.raa_ražotājs + ' ' + self.raa_modelis

    class Meta:
        #managed = False
        db_table = 'DVS_info_DB_RAA_iekārta_csv'


class DvsInfoDbRtuIekrtaCsv(models.Model):
    id_rtu = models.AutoField(db_column='id_RTU', primary_key=True)  # Field name made lowercase.
    reģions = models.CharField(db_column='Reģions', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nodaļa = models.CharField(db_column='Nodaļa', max_length=10, blank=True, null=True)  # Field name made lowercase.
    iezīme = models.CharField(db_column='Iezīme', max_length=5, blank=True, null=True)  # Field name made lowercase.
    objekts = models.CharField(db_column='Objekts', max_length=17, blank=True, null=True)  # Field name made lowercase.
    tips = models.CharField(db_column='Tips', max_length=23, blank=True, null=True)  # Field name made lowercase.
    iekārtas_ražotājs = models.CharField(db_column='Iekārtas_Ražotājs', max_length=17, blank=True, null=True)  # Field name made lowercase.
    modelis = models.CharField(db_column='Modelis', max_length=22, blank=True, null=True)  # Field name made lowercase.
    daudzums = models.IntegerField(db_column='Daudzums', blank=True, null=True)  # Field name made lowercase.
    uzstadīšanas_vieta = models.CharField(db_column='Uzstadīšanas_vieta', max_length=21, blank=True, null=True)  # Field name made lowercase.
    programmaturas_versija = models.CharField(db_column='Programmaturas_versija', max_length=34, blank=True, null=True)  # Field name made lowercase.
    piezime = models.CharField(db_column='Piezime', max_length=66, blank=True, null=True)  # Field name made lowercase.
    column13 = models.CharField(db_column='Column13', max_length=18, blank=True, null=True)  # Field name made lowercase.
    column14 = models.CharField(db_column='Column14', max_length=18, blank=True, null=True)  # Field name made lowercase.
    column15 = models.CharField(db_column='Column15', max_length=1, blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return self.reģions + ' ' + self.nodaļa + ' ' + self.objekts + ' ' + self.iekārtas_ražotājs + ' ' + self.modelis

    class Meta:
        #managed = False
        db_table = 'DVS_info_DB_RTU_iekārta_csv'


class DvsInfoDbCsv(models.Model):
    id_dvs = models.AutoField(db_column='id_DVS', primary_key=True)  # Field name made lowercase.
    reģions = models.CharField(db_column='Reģions', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nodaļa = models.CharField(db_column='Nodaļa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iezīme = models.CharField(db_column='Iezīme', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekts = models.CharField(db_column='Objekts', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekta_nosaukums = models.CharField(db_column='Objekta_nosaukums', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adrese = models.CharField(db_column='Adrese', max_length=100, blank=True, null=True)  # Field name made lowercase.
    atbidības_teritorija = models.CharField(db_column='Atbidības_teritorija', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tehn_id = models.CharField(db_column='Tehn_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps_n = models.CharField(db_column='GPS_N', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps_e = models.CharField(db_column='GPS_E', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ģis_x = models.FloatField(db_column='ĢIS_X', blank=True, null=True)  # Field name made lowercase.
    ģis_y = models.FloatField(db_column='ĢIS_Y', blank=True, null=True)  # Field name made lowercase.
    pieslēguma_veids = models.CharField(db_column='Pieslēguma_veids', max_length=50, blank=True, null=True)  # Field name made lowercase.
    darbs_ar_2_centriem = models.CharField(db_column='Darbs_ar_2_centriem', max_length=50, blank=True, null=True)  # Field name made lowercase.
    garantētā_barošana = models.CharField(db_column='Garantētā_barošana', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rtu_ražotājs = models.CharField(db_column='RTU_ražotājs', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rtu_2_ražotājs = models.CharField(db_column='RTU_2_ražotājs', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rtu_ip_adrese = models.CharField(db_column='RTU_IP_adrese', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nfe_tabula = models.CharField(db_column='NFE_tabula', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protokols_ar_scada = models.CharField(db_column='Protokols_ar_SCADA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protokols_ar_ast = models.CharField(db_column='Protokols_ar_AST', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dpp_1_saite_ar_slēgiekārtu = models.CharField(db_column='DPP_1_saite_ar_slēgiekārtu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dpp_2_saite_ar_slēgiekārtu = models.CharField(db_column='DPP_2_saite_ar_slēgiekārtu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    js = models.IntegerField(db_column='JS', blank=True, null=True)  # Field name made lowercase.
    io = models.IntegerField(db_column='IO', blank=True, null=True)  # Field name made lowercase.
    ts = models.IntegerField(db_column='TS', blank=True, null=True)  # Field name made lowercase.
    tv = models.IntegerField(db_column='TV', blank=True, null=True)  # Field name made lowercase.
    tm = models.IntegerField(db_column='TM', blank=True, null=True)  # Field name made lowercase.
    rekonstrukcijas_gads = models.IntegerField(db_column='Rekonstrukcijas_gads', blank=True, null=True)  # Field name made lowercase.
    vec_komp_gads = models.IntegerField(db_column='Vec_komp_gads', blank=True, null=True)  # Field name made lowercase.
    piezīme = models.CharField(db_column='Piezīme', max_length=255, blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return self.reģions + ' ' + self.nodaļa + ' ' + self.objekts

    class Meta:
        #managed = False
        db_table = 'DVS_info_DB_csv'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'