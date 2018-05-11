import logging
import json
import os
import copy
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http.response import JsonResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.templatetags.static import static
from django.urls import reverse
from django.utils.timezone import now
from smartpanel.forms import DisplayForm
from smartpanel.models import Layout, Display


logger = logging.getLogger(__name__)


def all(request):
    return render(request, 'smartpanel/my.html', {'smartpanels': Layout.objects.all()})


@login_required
def my(request):
    return render(request, 'smartpanel/my.html', {'smartpanels': Layout.objects.filter(owner=request.user),
                                                  'edit': True})


@login_required
def design(request):
    return render(request, 'smartpanel/layout_config.html', {'widgets_list': generate_widget_list()})


def generate_dependencies_files_list(uwl):
    css_files_list = []
    js_files_list = []
    external_js_files_list = []
    external_css_files_list = []
    for widget in uwl:
        if os.path.exists(os.path.join(settings.BASE_DIR, 'static/smartpanel/widgets/%s/%s.js' % (widget, widget))):
            js_files_list.append(static('smartpanel/widgets/%s/%s.js' % (widget, widget)))
        if os.path.exists(os.path.join(settings.BASE_DIR, 'static/smartpanel/widgets/%s/%s.css' % (widget, widget))):
            css_files_list.append(static('smartpanel/widgets/%s/%s.css' % (widget, widget)))
        try:
            requirements_file = open(os.path.join(settings.BASE_DIR, 'static/smartpanel/widgets/%s/requirements.json'
                                                  % widget))
            requirements = json.load(requirements_file)
            if 'scripts' in requirements:
                for script in requirements['scripts']:
                    if script.__class__ is dict:
                        external_js_files_list.append(script)
                    else:
                        js_files_list.append(static('smartpanel/widgets/%s/%s' % (widget, script)))
            if 'stylesheets':
                for stylesheet in requirements['stylesheets']:
                    if stylesheet.__class__ is dict:
                        external_css_files_list.append(stylesheet)
                    else:
                        css_files_list.append(static('smartpanel/widgets/%s/%s' % (widget, stylesheet)))
        except:
            pass
    return (css_files_list, js_files_list, external_js_files_list, external_css_files_list)


def generate_widget_list():
    widget_directory = os.path.join(settings.BASE_DIR, 'static/smartpanel/widgets')
    list_widget_files = os.listdir(widget_directory)
    list_widgets = []
    for widget_file in list_widget_files:
        if os.path.isdir(os.path.join(settings.BASE_DIR, 'static/smartpanel/widgets', widget_file)):
            list_widgets.append({
                'name': json.load(open(os.path.join(widget_directory, '%s/%s_schema.json' %
                                                    (widget_file, widget_file))))['title'],
                'file': widget_file
            })
    return list_widgets


@login_required
def layout_config(request, layout_id):
    layout = get_object_or_404(Layout, id=layout_id, owner=request.user)
    error = False
    try:
        if request.method == "POST" and 'data' in request.POST and 'name' in request.POST and 'design' in request.POST:
            name = request.POST['name']
            design = json.loads(request.POST['design'])
            data = json.loads(request.POST['data'])
            for key, value in design.items():
                if key in data and 'data' in data[key] and 'widget' in data[key] and 'placeholder' in data[key]:
                    design[key]['widget'] = data[key]['widget']
                    design[key]['data'] = data[key]['data']
                    design[key]['placeholder'] = data[key]['placeholder']
            layout.name = name
            layout.design = design
            layout.save()
    except:
        error = True
    return render(request, 'smartpanel/layout_config.html',
                  {'layout': layout, 'error': error,
                   'debug': request.GET.get('debug', False), 'widgets_list': generate_widget_list()})


@login_required
def layout_delete(request, layout_id):
    layout = get_object_or_404(Layout, id=layout_id, owner=request.user)
    if request.method == "POST":
        layout.delete()
        return redirect('smartpanel-home')
    return redirect('smartpanel-layout-config', layout_id)


def layout(request, layout_id, display=None):
    layout = get_object_or_404(Layout, id=layout_id)
    uwl = []  # unique widget list
    for key, value in layout.design.items():
        if 'widget' in value and value['widget'] not in uwl:
            uwl.append(value['widget'])
    dependencies_files_list = generate_dependencies_files_list(uwl)
    return render(request, 'smartpanel/layout.html',
                  {'layout': layout, 'stylesheets': dependencies_files_list[0],
                   'scripts': dependencies_files_list[1], 'external_scripts': dependencies_files_list[2],
                   'external_stylesheets': dependencies_files_list[3], 'display': display})


@login_required
def publish_new_layout_version(request, layout_id):
    layout = get_object_or_404(Layout, id=layout_id, owner=request.user)
    if request.method == "POST":
        layout.version += 1
        layout.version_date = now()
        layout.save()
        messages.info(request, 'SmartPanel layout published')
    return redirect('smartpanel-layout-my')


@login_required
def new_display(request):
    if request.method == "POST":
        screen_form = DisplayForm(request.POST)
        if screen_form.is_valid():
            display = screen_form.save(commit=False)
            display.owner = request.user
            display.save()
            return redirect('smartpanel-home')
    else:
        screen_form = DisplayForm()
    return render(request, 'smartpanel/display.html', {'screen_form': screen_form})


def displays(request):
    return render(request, 'smartpanel/displays.html', {'screens': Display.objects.all()})


def display_refresh(request, display_id, layout_id, version):
    display = get_object_or_404(Display, id=display_id)
    refresh_info = copy.deepcopy(request.GET)
    refresh_info['source_ip'] = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
    refresh_info['time'] = now()
    cache.set('display-%s' % display.id, refresh_info)
    if display.layout.id != int(layout_id) or display.layout.version != int(version):
        return JsonResponse({'refresh': True, 'url': reverse('smartpanel-display', args=(display_id, ))})
    return JsonResponse({'refresh': False, 'url': reverse('smartpanel-display', args=(display_id, ))})


def display(request, display_id):
    display = get_object_or_404(Display, id=display_id)
    return layout(request, display.layout.id, display=display)


def displays_debug(request):
    results = {}
    for display in Display.objects.all():
        results['display-%s' % display.id] = cache.get('display-%s' % display.id, {})
    return JsonResponse(results)


@login_required
def my_displays(request):
    return render(request, 'smartpanel/displays.html', {'screens': Display.objects.filter(owner=request.user),
                                                        'edit': True})


@login_required
def edit_display(request, display_id):
    display = get_object_or_404(Display, id=display_id, owner=request.user)
    if request.method == "POST":
        display_form = DisplayForm(request.POST, instance=display)
        if display_form.is_valid():
            display.save()
            return redirect('smartpanel-home')
    else:
        display_form = DisplayForm(instance=display)
    return render(request, 'smartpanel/display.html', {'screen_form': display_form, 'edit': True})


@login_required
def delete_display(request, display_id):
    display = get_object_or_404(Display, id=display_id, owner=request.user)
    if request.method == "POST":
        display.delete()
        return redirect('smartpanel-home')
    return redirect('smartpanel-list-my-displays')