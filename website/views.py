from django.shortcuts import render, redirect
from .models import DvsInfoDbCsv
from .models import DvsInfoDbAkbCsv
from .models import DvsInfoDbRaaIekrtaCsv
from .models import DvsInfoDbRtuIekrtaCsv
from .models import RTUrazotajs
from .models import ObjektuSadalijums
from .models import RTUvecums
from .forms import ObjectForm
from django.contrib import messages
from django.views import generic

def test(request):
    main_dvs = DvsInfoDbCsv.objects.all
    return render(request, 'test.html', {'main_dvs': main_dvs})

def index(request):
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'login.html', {})

def home(request):
    main_dvs = DvsInfoDbCsv.objects.all
    return render(request, 'home.html', {'main_dvs': main_dvs})

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

def single_object(request, object_id):
    single_object = DvsInfoDbCsv.objects.get(pk = object_id)
    single_object_akb = DvsInfoDbAkbCsv.objects.all
    single_object_rtu = DvsInfoDbRtuIekrtaCsv.objects.all
    single_object_raa = DvsInfoDbRaaIekrtaCsv.objects.all
    return render(request, 'single_object.html', {'single_object': single_object, 'single_object_akb': single_object_akb, 'single_object_rtu': single_object_rtu, 'single_object_raa': single_object_raa})

def search_objects (request):
    if request.method == 'POST':
        meklesana = request.POST.get('meklesana')
        mekletais_objekts = DvsInfoDbCsv.objects.filter(objekts__contains = meklesana)
        return render(request, 'search_objects.html', {'meklesana': meklesana, 'mekletais_objekts': mekletais_objekts})
    else:
        return render(request, 'search_objects.html', {})
# def show_object(request, object_id):
#     object_to_get = DvsInfoDbCsv.objects.get(pk = object_id)
#     return render(request, 'show_object.html', {'object_to_get': object_to_get})
    
    
def update_object(request, object_id):
    updated_object = DvsInfoDbCsv.objects.get(pk = object_id)
    form = ObjectForm(request.POST or None, instance = updated_object)
    if form.is_valid():
            form.save()
            messages.success(request, ('Labojumi ir veikti'))
            return redirect('home')
    return render(request, 'update_object.html', {'updated_object': updated_object, 'form': form})

# class ModelDeleteView(DeleteView):
#     model = ObjectForm(request.POST or None, instance = delete_object)
#     template_name = "delete_object.html"

def delete_object(request, object_id):
    deleted_object = DvsInfoDbCsv.objects.get(pk = object_id)
    form = ObjectForm(request.POST or None, instance = deleted_object)
    if form.is_valid():
            form.save()
            deleted_object.delete()
            messages.success(request, ('Objekts ir izdzēsts'))
            return redirect('home')
    return render(request, 'delete_object.html', {'deleted_object': deleted_object, 'form': form})


    
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



