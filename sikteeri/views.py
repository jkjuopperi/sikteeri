# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("sikteeri.views")

from django.conf import settings
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.comments.models import Comment
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseForbidden

def frontpage(request):
    if settings.MAINTENANCE_MESSAGE == None:
        if not request.user.is_authenticated():
            return redirect('membership.views.new_application')
        return render_to_response('frontpage.html',
                                {"title": _('Django and the jazz cigarette')},
                                  context_instance=RequestContext(request))

    else:
        return render_to_response('maintenance_message.html',
                                  {"title": _('Under maintenance'),
                                   "maintenance_message": settings.MAINTENANCE_MESSAGE},
                                  context_instance=RequestContext(request))
