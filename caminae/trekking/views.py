from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.utils.html import escape
from django.views.generic.edit import CreateView
from django.views.generic.detail import BaseDetailView

from caminae.authent.decorators import trekking_manager_required
from caminae.mapentity.views import (MapEntityLayer, MapEntityList, MapEntityJsonList, MapEntityFormat,
                                MapEntityDetail, MapEntityDocument, MapEntityCreate, MapEntityUpdate, MapEntityDelete)
from caminae.common.views import json_django_dumps, HttpJSONResponse
from .models import Trek, POI, WebLink
from .filters import TrekFilter, POIFilter
from .forms import TrekForm, POIForm, WebLinkCreateFormPopup



class TrekLayer(MapEntityLayer):
    queryset = Trek.objects.existing().filter(published=True)
    fields = ['name', 'departure', 'arrival', 'serializable_difficulty',
              'duration', 'ascent', 'serializable_themes',
              'serializable_usages', 'disabled_infrastructure', 'is_loop',
              'is_transborder']


class TrekList(MapEntityList):
    queryset = Trek.objects.existing()
    filterform = TrekFilter
    columns = ['id', 'name', 'departure', 'arrival']


class TrekJsonList(MapEntityJsonList, TrekList):
    pass


class TrekFormatList(MapEntityFormat, TrekList):
    pass


class TrekJsonDetail(BaseDetailView):
    queryset = Trek.objects.existing().filter(published=True)
    fields = ['name', 'departure', 'arrival', 'duration', 'description',
              'description_teaser', 'length', 'ascent', 'max_elevation',
              'web_links', 'advice', 'networks', 'ambiance']

    def get_context_data(self, **kwargs):
        o = self.object
        ctx = {}

        for fname in self.fields:
            field = o._meta.get_field_by_name(fname)[0]
            if field in o._meta.many_to_many:
                ctx[fname] = getattr(o, fname).all()
            else:
                ctx[fname] = getattr(o, fname)

        return ctx

    def render_to_response(self, context):
        return HttpJSONResponse(json_django_dumps(context))


class TrekDetail(MapEntityDetail):
    model = Trek

    def can_edit(self):
        return hasattr(self.request.user, 'profile') and \
               self.request.user.profile.is_trekking_manager()


class TrekDocument(MapEntityDocument):
    model = Trek


class TrekCreate(MapEntityCreate):
    model = Trek
    form_class = TrekForm

    @method_decorator(trekking_manager_required('trekking:trek_list'))
    def dispatch(self, *args, **kwargs):
        return super(TrekCreate, self).dispatch(*args, **kwargs)


class TrekUpdate(MapEntityUpdate):
    model = Trek
    form_class = TrekForm

    @method_decorator(trekking_manager_required('trekking:trek_detail'))
    def dispatch(self, *args, **kwargs):
        return super(TrekUpdate, self).dispatch(*args, **kwargs)


class TrekDelete(MapEntityDelete):
    model = Trek

    @method_decorator(trekking_manager_required('trekking:trek_detail'))
    def dispatch(self, *args, **kwargs):
        return super(TrekDelete, self).dispatch(*args, **kwargs)


class POILayer(MapEntityLayer):
    queryset = POI.objects.existing()


class POIList(MapEntityList):
    queryset = POI.objects.existing()
    filterform = POIFilter
    columns = ['id', 'name', 'type']


class POIJsonList(MapEntityJsonList, POIList):
    pass


class POIFormatList(MapEntityFormat, POIList):
        pass


class POIDetail(MapEntityDetail):
    model = POI

    def can_edit(self):
        return hasattr(self.request.user, 'profile') and \
               self.request.user.profile.is_trekking_manager()


class POIDocument(MapEntityDocument):
    model = POI



class POICreate(MapEntityCreate):
    model = POI
    form_class = POIForm

    @method_decorator(trekking_manager_required('trekking:poi_list'))
    def dispatch(self, *args, **kwargs):
        return super(POICreate, self).dispatch(*args, **kwargs)


class POIUpdate(MapEntityUpdate):
    model = POI
    form_class = POIForm

    @method_decorator(trekking_manager_required('trekking:poi_detail'))
    def dispatch(self, *args, **kwargs):
        return super(POIUpdate, self).dispatch(*args, **kwargs)


class POIDelete(MapEntityDelete):
    model = POI

    @method_decorator(trekking_manager_required('trekking:poi_detail'))
    def dispatch(self, *args, **kwargs):
        return super(POIDelete, self).dispatch(*args, **kwargs)



class WebLinkCreatePopup(CreateView):
    model = WebLink
    form_class = WebLinkCreateFormPopup

    def form_valid(self, form):
        self.object = form.save()
        print form.instance
        return HttpResponse("""
            <script type="text/javascript">opener.dismissAddAnotherPopup(window, "%s", "%s");</script>
        """ % (escape(form.instance._get_pk_val()), escape(form.instance)))
