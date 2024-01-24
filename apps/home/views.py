# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.home.forms import SubscriptionForm
from apps.home.models import Subscription


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        elif load_template == 'ui-list-subscript-users.html':
            query_set = Subscription.objects.all()

            context['data'] = [{
                'user': each.user,
                'credit_card': each.credit_card,
                'activation_date': each.activation_date,
                'preferences': each.preferences,
                'level': each.level

            } for each in query_set]

            context['titles'] = ['user',
                                 'credit_card',
                                 'activation_date',
                                 'preferences',
                                 'level'
                                 ]

        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


class SubscriptionView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'home/ui-add-subscription.html'
    form_class = SubscriptionForm
    success_url = reverse_lazy('home')
