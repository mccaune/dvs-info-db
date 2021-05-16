from django.shortcuts import render, redirect
from .models import DvsInfoDbCsv, DvsInfoDbAkbCsv, DvsInfoDbRaaIekrtaCsv, DvsInfoDbRtuIekrtaCsv, RTUrazotajs, ObjektuSadalijums, RTUvecums, AKB, RTU, RAA
from .forms import ObjectForm, AkumForm, RtuForm, RaaForm, RegisterForm
from django.contrib import messages
from django.views import generic
from django.contrib.auth.models import Permission, User, Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
#from website import forms
#from website import models


def test(request):
    main_dvs = DvsInfoDbCsv.objects.all
    return render(request, 'test.html', {'main_dvs': main_dvs})

def index(request):
    return render(request, 'index.html', {})

@login_required(login_url='login')
def home(request):
    main_dvs = DvsInfoDbCsv.objects.all
    return render(request, 'home.html', {'main_dvs': main_dvs})

@login_required(login_url='login')
def statistics(request):
    rtu_razotajs_stat = RTUrazotajs.objects.all
    objektu_sadalijums_stat = ObjektuSadalijums.objects.all
    rtu_vecums_stat = RTUvecums.objects.all
    
    labels = []
    data = []
    percent = []
    kopejais_skaits = 0
    
    times_to_iterate = RTUrazotajs.objects.order_by('-rtu_count')
    for item in times_to_iterate:
        labels.append(item.rtu_ražotājs)
        data.append(item.rtu_count)
        kopejais_skaits += item.rtu_count
    
    for x in data:
        percent.append((x/kopejais_skaits) * 100)
        
        
    labels_sadalijums = []
    data_sadalijums = []
    
    times_to_iterate_sadalijums = ObjektuSadalijums.objects.order_by('reģions')
    for item in times_to_iterate_sadalijums:
        labels_sadalijums.append(item.reģions)
        data_sadalijums.append(item.objektu_skaits)
        
    labels_vecums = []
    data_vecums = []
    
    times_to_iterate_vecums = RTUvecums.objects.order_by('rtu_gads')
    for item in times_to_iterate_vecums:
        labels_vecums.append(item.rtu_gads)
        data_vecums.append(item.rtu_skaits)
    
    labels_vecums[0] = 0
    return render(request, 'statistics.html', { 'rtu_razotajs_stat': rtu_razotajs_stat, 'labels': labels, 'data': data, 'kopejais_skaits': kopejais_skaits, 'percent': percent, 'labels_sadalijums': labels_sadalijums, 'data_sadalijums': data_sadalijums, 'objektu_sadalijums_stat': objektu_sadalijums_stat, 'labels_vecums': labels_vecums, 'data_vecums': data_vecums, 'rtu_vecums_stat': rtu_vecums_stat  })

@login_required(login_url='login')
def single_object(request, object_id):
    single_object = DvsInfoDbCsv.objects.get(pk = object_id)
    single_object_akb = DvsInfoDbAkbCsv.objects.all
    single_object_rtu = DvsInfoDbRtuIekrtaCsv.objects.all
    single_object_raa = DvsInfoDbRaaIekrtaCsv.objects.all
    return render(request, 'single_object.html', {'single_object': single_object, 'single_object_akb': single_object_akb, 'single_object_rtu': single_object_rtu, 'single_object_raa': single_object_raa})

@login_required(login_url='login')
def search_objects (request):
    if request.method == 'POST':
        meklesana = request.POST.get('meklesana')
        mekletais_objekts = DvsInfoDbCsv.objects.filter(objekts__contains = meklesana)
        return render(request, 'search_objects.html', {'meklesana': meklesana, 'mekletais_objekts': mekletais_objekts})
    else:
        return render(request, 'search_objects.html', {})

@login_required(login_url='login')
def update_object(request, object_id):
    updated_object = DvsInfoDbCsv.objects.get(pk = object_id)
    form = ObjectForm(request.POST or None, instance = updated_object)
    if form.is_valid():
            form.save()
            messages.success(request, ('Labojumi objekta datos ir veikti'))
            return redirect('single_object', object_id = updated_object.id_dvs)
    return render(request, 'update_object.html', {'updated_object': updated_object, 'form': form})

@login_required(login_url='login')
def update_akum(request, object_id):
    updated_akum = DvsInfoDbAkbCsv.objects.get(pk = object_id)
    form = AkumForm(request.POST or None, instance = updated_akum)
    upd_akb_obj_id = AKB.objects.get(pk = object_id)
    if form.is_valid():
            form.save()
            messages.success(request, ('Labojumi akumulatora datos ir veikti'))
            return redirect('single_object', object_id = upd_akb_obj_id.id_dvs)
    return render(request, 'update_akum.html', {'updated_akum': updated_akum, 'form': form})

@login_required(login_url='login')
def update_rtu(request, object_id):
    updated_rtu = DvsInfoDbRtuIekrtaCsv.objects.get(pk = object_id)
    form = RtuForm(request.POST or None, instance = updated_rtu)
    upd_rtu_obj_id = RTU.objects.get(pk = object_id)
    if form.is_valid():
            form.save()
            messages.success(request, ('Labojumi RTU iekārtas datos ir veikti'))
            return redirect('single_object', object_id = upd_rtu_obj_id.id_dvs)
    return render(request, 'update_rtu.html', {'updated_rtu': updated_rtu, 'form': form})

@login_required(login_url='login')
def update_raa(request, object_id):
    updated_raa = DvsInfoDbRaaIekrtaCsv.objects.get(pk = object_id)
    form = RaaForm(request.POST or None, instance = updated_raa)
    upd_raa_obj_id = RAA.objects.get(pk = object_id)
    if form.is_valid():
            form.save()
            messages.success(request, ('Labojumi RAA iekārtas datos ir veikti'))
            return redirect('single_object', object_id = upd_raa_obj_id.id_dvs)
    return render(request, 'update_raa.html', {'updated_raa': updated_raa, 'form': form})

@login_required(login_url='login')
def delete_object(request, object_id):
    deleted_object = DvsInfoDbCsv.objects.get(pk = object_id)
    form = ObjectForm(request.POST or None, instance = deleted_object)
    if form.is_valid():
            form.save()
            deleted_object.delete()
            messages.success(request, ('Objekta dati ir izdzēsti'))
            return redirect('home')
    return render(request, 'delete_object.html', {'deleted_object': deleted_object, 'form': form})

@login_required(login_url='login')
def delete_akum(request, object_id):
    deleted_akum = DvsInfoDbAkbCsv.objects.get(pk = object_id)
    form = AkumForm(request.POST or None, instance = deleted_akum)
    akb_obj_id = AKB.objects.get(pk = object_id)
    if form.is_valid():
            form.save()
            deleted_akum.delete()
            messages.success(request, ('Akumulatora dati ir izdzēsti'))
            return redirect('single_object', object_id = akb_obj_id.id_dvs)
    return render(request, 'delete_akum.html', {'deleted_akum': deleted_akum, 'form': form})

# @login_required(login_url='login')
# def delete_akum(request, object_id):
#     deleted_akum = DvsInfoDbAkbCsv.objects.get(pk = object_id)
#     form = AkumForm(request.POST or None, instance = deleted_akum)
#     dvs_all_obj = DvsInfoDbCsv.objects.all
#     redirect_id = 10
#     for x in dvs_all_obj:
#         if x.objekts == delete_akum.objekts:
#             redirect_id = x.id_dvs
#     if form.is_valid():
#             form.save()
#             deleted_akum.delete()
#             messages.success(request, ('Akumulatora dati ir izdzēsti'))
#             return redirect('single_object', object_id = redirect_id)
#     return render(request, 'delete_akum.html', {'deleted_akum': deleted_akum, 'form': form})


# @login_required(login_url='login')
# def delete_akum(request, object_id):
#     deleted_akum = DvsInfoDbAkbCsv.objects.get(pk = object_id)
#     test = DvsInfoDbCsv.objects.all
#     for x in test:
#         if  x.objekts == delete_akum.objekts:
#             redirect_id = x.id_dvs
#     if request.method=='POST':
#         deleted_akum.delete()
#         return redirect('single_object', object_id = redirect_id)
#     return render(request, 'delete_akum.html', {'deleted_akum': deleted_akum})

@login_required(login_url='login')
def delete_rtu(request, object_id):
    deleted_rtu = DvsInfoDbRtuIekrtaCsv.objects.get(pk = object_id)
    form = RtuForm(request.POST or None, instance = deleted_rtu)
    rtu_obj_id = RTU.objects.get(pk = object_id)
    if form.is_valid():
            form.save()
            deleted_rtu.delete()
            messages.success(request, ('RTU iekārtas dati ir izdzēsti'))
            return redirect('single_object', object_id = rtu_obj_id.id_dvs)
    return render(request, 'delete_rtu.html', {'deleted_rtu': deleted_rtu, 'form': form})

@login_required(login_url='login')
def delete_raa(request, object_id):
    deleted_raa = DvsInfoDbRaaIekrtaCsv.objects.get(pk = object_id)
    form = RaaForm(request.POST or None, instance = deleted_raa)
    raa_obj_id = RAA.objects.get(pk = object_id)
    if form.is_valid():
            form.save()
            deleted_raa.delete()
            messages.success(request, ('RAA iekārtas dati ir izdzēsti'))
            return redirect('single_object', object_id = raa_obj_id.id_dvs)
    return render(request, 'delete_raa.html', {'deleted_raa': deleted_raa, 'form': form})

@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        form = ObjectForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            reģions = request.POST['reģions']
            nodaļa = request.POST['nodaļa']
            iezīme = request.POST['iezīme']
            objekts = request.POST['objekts']
            objekta_nosaukums = request.POST['objekta_nosaukums']
            adrese = request.POST['adrese']
            atbidības_teritorija = request.POST['atbidības_teritorija']
            tehn_id = request.POST['tehn_id']
            gps_n = request.POST['gps_n']
            gps_e = request.POST['gps_e']
            ģis_x = request.POST['ģis_x']
            ģis_y = request.POST['ģis_y']
            pieslēguma_veids = request.POST['pieslēguma_veids']
            darbs_ar_2_centriem  = request.POST['darbs_ar_2_centriem ']
            garantētā_barošana = request.POST['garantētā_barošana']
            rtu_ražotājs = request.POST['rtu_ražotājs']
            rtu_2_ražotājs = request.POST['rtu_2_ražotājs']
            status = request.POST['status']
            rtu_ip_adrese = request.POST['rtu_ip_adrese']
            nfe_tabula = request.POST['nfe_tabula']
            protokols_ar_scada = request.POST['protokols_ar_scada']
            protokols_ar_ast = request.POST['protokols_ar_ast']
            dpp_1_saite_ar_slēgiekārtu = request.POST['dpp_1_saite_ar_slēgiekārtu']
            dpp_2_saite_ar_slēgiekārtu = request.POST['dpp_2_saite_ar_slēgiekārtu']
            js = request.POST['js']
            io = request.POST['io']
            ts = request.POST['ts']
            tv = request.POST['tv']
            tm = request.POST['tm']
            rekonstrukcijas_gads = request.POST['rekonstrukcijas_gads']
            vec_komp_gads = request.POST['vec_komp_gads']
            piezīme = request.POST['piezīme']
            
            messages.success(request, ('Kļūda pievienojot objektu'))
            #return redirect('add')
            return render(request, 'add.html', {'reģions': reģions, 'nodaļa': nodaļa, 'iezīme': iezīme, 'objekts': objekts, 'objekta_nosaukums': objekta_nosaukums, 'adrese': adrese, 'atbidības_teritorija': atbidības_teritorija, 'tehn_id': tehn_id, 'gps_n': gps_n, 'gps_e': gps_e, 'ģis_x': ģis_x, 'ģis_y': ģis_y, 'pieslēguma_veids': pieslēguma_veids, 'darbs_ar_2_centriem': darbs_ar_2_centriem, 'garantētā_barošana': garantētā_barošana, 'rtu_ražotājs': rtu_ražotājs, 'rtu_2_ražotājs': rtu_2_ražotājs, 'status': status, 'rtu_ip_adrese': rtu_ip_adrese, 'nfe_tabula': nfe_tabula, 'protokols_ar_scada': protokols_ar_scada, 'protokols_ar_ast': protokols_ar_ast, 'dpp_1_saite_ar_slēgiekārtu': dpp_1_saite_ar_slēgiekārtu, 'dpp_2_saite_ar_slēgiekārtu': dpp_2_saite_ar_slēgiekārtu, 'js': js, 'io': io, 'ts': ts, 'tv': tv, 'tm': tm, 'rekonstrukcijas_gads': rekonstrukcijas_gads, 'vec_komp_gads': vec_komp_gads, 'piezīme': piezīme })
        messages.success(request, ('Objekts ir pievienots datubāzei'))
        return redirect('home')
    else:
        return render(request, 'add.html', {})

@login_required(login_url='login')
def add_akb(request, object_id):
    akb_object_data = DvsInfoDbCsv.objects.get(pk = object_id)
    if request.method == 'POST':
        form = AkumForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            reģions = request.POST['reģions']
            nodaļa = request.POST['nodaļa']
            iezīme = request.POST['iezīme']
            objekts = request.POST['objekts']
            akb_ražotājs_un_nomināli = request.POST['akb_ražotājs_un_nomināli']
            akb_skaits = request.POST['akb_skaits']
            akb_izmērītais_ah = request.POST['akb_izmērītais_ah']
            akb_iekšējā_pretestība_mom = request.POST['akb_iekšējā_pretestība_mom']
            uzstādīšanas_vieta = request.POST['uzstādīšanas_vieta']
            uzstādīšanas_gads = request.POST['uzstādīšanas_gads']
            akb_izgatavošanas_partija_vai_datums = request.POST['akb_izgatavošanas_partija_vai_datums']
            pārbaudes_datums = request.POST['pārbaudes_datums']
            nākošā_pārbaude = request.POST['nākošā_pārbaude']     
            piezīme = request.POST['piezīme']
            
            messages.success(request, ('Kļūda pievienojot akumulatoru'))
            #return redirect('add')
            return render(request, 'add.html', {'reģions': reģions, 'nodaļa': nodaļa, 'iezīme': iezīme, 'objekts': objekts, 'akb_ražotājs_un_nomināli':akb_ražotājs_un_nomināli , 'akb_skaits':akb_skaits , 'akb_izmērītais_ah':akb_izmērītais_ah , 'akb_iekšējā_pretestība_mom':akb_iekšējā_pretestība_mom , 'uzstādīšanas_vieta':uzstādīšanas_vieta , 'uzstādīšanas_gads':uzstādīšanas_gads , 'akb_izgatavošanas_partija_vai_datums':akb_izgatavošanas_partija_vai_datums , 'pārbaudes_datums':pārbaudes_datums , 'nākošā_pārbaude':nākošā_pārbaude , 'piezīme':piezīme, 'akb_object_data':akb_object_data })
        messages.success(request, ('Akumulators ir pievienots datubāzei'))
        return redirect('single_object', object_id = akb_object_data.id_dvs)
    else:
        return render(request, 'add_akb.html', { 'akb_object_data':akb_object_data })

@login_required(login_url='login')
def add_rtu(request, object_id):
    rtu_object_data = DvsInfoDbCsv.objects.get(pk = object_id)
    if request.method == 'POST':
        form = RtuForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            reģions = request.POST['reģions']
            nodaļa = request.POST['nodaļa']
            iezīme = request.POST['iezīme']
            objekts = request.POST['objekts']
            tips = request.POST['tips']
            iekārtas_ražotājs = request.POST['iekārtas_ražotājs']
            modelis = request.POST['modelis']
            daudzums = request.POST['daudzums']
            uzstadīšanas_vieta = request.POST['uzstadīšanas_vieta']
            programmaturas_versija = request.POST['programmaturas_versija']
            piezīme = request.POST['piezīme']       
            
            messages.success(request, ('Kļūda pievienojot RTU iekārtu'))
            #return redirect('add')
            return render(request, 'add.html', {'reģions': reģions, 'nodaļa': nodaļa, 'iezīme': iezīme, 'objekts': objekts, 'tips':tips , 'iekārtas_ražotājs':iekārtas_ražotājs , 'modelis':modelis , 'daudzums':daudzums , 'uzstadīšanas_vieta':uzstadīšanas_vieta , 'programmaturas_versija':programmaturas_versija, 'piezīme':piezīme, 'rtu_object_data':rtu_object_data })
        messages.success(request, ('RTU iekārta ir pievienota datubāzei'))
        return redirect('single_object', object_id = rtu_object_data.id_dvs)
    else:
        return render(request, 'add_rtu.html', { 'rtu_object_data':rtu_object_data })

@login_required(login_url='login')
def add_raa(request, object_id):
    raa_object_data = DvsInfoDbCsv.objects.get(pk = object_id)
    if request.method == 'POST':
        form = RaaForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            reģions = request.POST['reģions']
            nodaļa = request.POST['nodaļa']
            iezīme = request.POST['iezīme']
            objekts = request.POST['objekts']
            raa_ražotājs = request.POST['raa_ražotājs']
            raa_modelis = request.POST['raa_modelis']
            raa_daudzums = request.POST['raa_daudzums']
            raa_protokols = request.POST['raa_protokols']
            raa_interface = request.POST['raa_interface']
            raa_pieslegums = request.POST['raa_pieslegums']
            piezīme = request.POST['piezīme']       
            
            messages.success(request, ('Kļūda pievienojot RAA iekārtu'))
            #return redirect('add')
            return render(request, 'add.html', {'reģions': reģions, 'nodaļa': nodaļa, 'iezīme': iezīme, 'objekts': objekts, 'raa_ražotājs':raa_ražotājs , 'raa_modelis':raa_modelis , 'raa_daudzums':raa_daudzums , 'raa_protokols':raa_protokols , 'raa_interface':raa_interface , 'raa_pieslegums':raa_pieslegums , 'piezīme':piezīme, 'raa_object_data':raa_object_data })
        messages.success(request, ('RAA iekārta ir pievienota datubāzei'))
        return redirect('single_object', object_id = raa_object_data.id_dvs)
    else:
        return render(request, 'add_raa.html', { 'raa_object_data':raa_object_data })


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

