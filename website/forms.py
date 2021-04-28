from django import forms
from .models import DvsInfoDbCsv
from .models import DvsInfoDbAkbCsv
from .models import DvsInfoDbRaaIekrtaCsv
from .models import DvsInfoDbRtuIekrtaCsv

class ObjectForm(forms.ModelForm):
    class Meta:
        model = DvsInfoDbCsv
        fields = ['reģions','nodaļa','iezīme','objekts', 'objekta_nosaukums', 'adrese', 'atbidības_teritorija', 'tehn_id', 'gps_n', 'gps_e', 'ģis_x', 'ģis_y', 'pieslēguma_veids', 'darbs_ar_2_centriem', 'garantētā_barošana', 'rtu_ražotājs', 'rtu_2_ražotājs', 'status', 'rtu_ip_adrese', 'nfe_tabula', 'protokols_ar_scada', 'protokols_ar_ast', 'dpp_1_saite_ar_slēgiekārtu', 'dpp_2_saite_ar_slēgiekārtu', 'js', 'io', 'ts', 'tv', 'tm', 'rekonstrukcijas_gads', 'vec_komp_gads', 'piezīme']
        
class AkumForm(forms.ModelForm):
    class Meta:
        model = DvsInfoDbAkbCsv
        fields = ['reģions','nodaļa','iezīme','objekts', 'akb_ražotājs_un_nomināli', 'akb_skaits', 'akb_izmērītais_ah', 'akb_iekšējā_pretestība_mom', 'uzstādīšanas_vieta', 'uzstādīšanas_gads', 'akb_izgatavošanas_partija_vai_datums', 'pārbaudes_datums', 'nākošā_pārbaude', 'piezīme']
        
class RtuForm(forms.ModelForm):
    class Meta:
        model = DvsInfoDbRtuIekrtaCsv
        fields = ['reģions','nodaļa','iezīme','objekts', 'tips', 'iekārtas_ražotājs', 'modelis', 'daudzums', 'uzstadīšanas_vieta', 'programmaturas_versija', 'piezime']
        
class RaaForm(forms.ModelForm):
    class Meta:
        model = DvsInfoDbRaaIekrtaCsv
        fields = ['reģions','nodaļa','iezīme','objekts', 'raa_ražotājs', 'raa_modelis', 'raa_daudzums', 'raa_protokols', 'raa_interface', 'raa_pieslegums', 'piezime']