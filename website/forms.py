from django import forms
from .models import DvsInfoDbCsv
from .models import DvsInfoDbAkbCsv
from .models import DvsInfoDbRaaIekrtaCsv
from .models import DvsInfoDbRtuIekrtaCsv

class ObjectForm(forms.ModelForm):
    class Meta:
        model = DvsInfoDbCsv
        fields = ['reģions','nodaļa','iezīme','objekts', 'objekta_nosaukums', 'adrese', 'atbidības_teritorija', 'tehn_id', 'gps_n', 'gps_e', 'ģis_x', 'ģis_y', 'pieslēguma_veids', 'darbs_ar_2_centriem', 'garantētā_barošana', 'rtu_ražotājs', 'rtu_2_ražotājs', 'status', 'rtu_ip_adrese', 'nfe_tabula', 'protokols_ar_scada', 'protokols_ar_ast', 'dpp_1_saite_ar_slēgiekārtu', 'dpp_2_saite_ar_slēgiekārtu', 'js', 'io', 'ts', 'tv', 'tm', 'rekonstrukcijas_gads', 'vec_komp_gads', 'piezīme']