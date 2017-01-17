# -*-coding:utf-8;-*-
from __future__ import unicode_literals
from django.contrib.sites.models import Site
from django.shortcuts import redirect, render
from django.contrib import messages

from django.urls import reverse

from index import forms
from index import models


def index(request):
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Ваша заявка принята. Ожидайте звонка нашего специалиста.')
        return redirect(reverse('index'))
    site = Site.objects.filter(domain=request.get_host()).first()
    campaign = models.Campaign.objects.filter(id=request.session.get('campaign_id'))
    visitor = models.Visitor.objects.filter(id=request.session.get('visitor_id')).first()
    if not visitor:
        visitor = models.Visitor.objects.create(
            area=site.area,
            campaign=campaign.first() if campaign else None,
        )
    request.session['visitor_id'] = visitor.id
    form = forms.OrderForm(initial={
        'visitor': visitor
    })
    return render(request, site.area.get_template('index.html'), context={'form': form})


def proxy(request, campaign_id=None):
    if campaign_id:
        request.session['campaign_id'] = campaign_id
    return redirect(models.Area.get_random().get_url())
