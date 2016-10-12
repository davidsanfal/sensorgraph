from django.shortcuts import render
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.flot import LineChart
from sensors.utils.csv_parser import parser
from sensors.forms import GraphForm
from sensors.utils.graph_utils import datasets
from sensors.exceptions import SensorGraphException


def index(request):
    return render(request, "index.html", {})

def upload_csv_form(request):
    msg = None
    if request.method == 'POST':
        try:
            files_uploaded = parser(request.FILES.getlist("files"))
            msg = {'status': 'success',
                   'title': 'Files Uploaded',
                   'content': files_uploaded}
        except SensorGraphException as e:
            msg = {'status': 'danger',
                   'title': 'Parse Error',
                   'content': str(e).splitlines()}
    return render(request, "upload.html", {'msg': msg})

def graph(request):
    form = GraphForm()
    charts = None
    if request.method == 'POST':
        form = GraphForm(request.POST)
        if form.is_valid():
            charts = datasets(form.cleaned_data)
    return render(request, "graph.html", {'charts': charts,
                                          'form': form})
