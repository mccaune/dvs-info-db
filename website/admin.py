from django.contrib import admin
from .models import DvsInfoDbCsv
from .models import DvsInfoDbAkbCsv
from .models import DvsInfoDbRaaIekrtaCsv
from .models import DvsInfoDbRtuIekrtaCsv
from .models import RTUrazotajs

admin.site.register(DvsInfoDbCsv)
admin.site.register(DvsInfoDbAkbCsv)
admin.site.register(DvsInfoDbRaaIekrtaCsv)
admin.site.register(DvsInfoDbRtuIekrtaCsv)
admin.site.register(RTUrazotajs)

