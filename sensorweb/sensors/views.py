from django.shortcuts import render
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.flot import LineChart
from sensors.utils.csv_parser import parser
from sensors.forms import GraphForm
from sensors.utils.graph_utils import graphs
from sensors.exceptions import SensorGraphException


def index(request):
    return render(request, "index.html", {})

def upload_csv_form(request):
    '''Upload a CSV file list, parse it and save the Sensors in DB'''
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
    '''Draw one or more praph with the GraphForm parameters'''
    form = GraphForm()
    graph_list = None
    if request.method == 'POST':
        form = GraphForm(request.POST)
        if form.is_valid():
            graph_list = graphs(form.cleaned_data)
    return render(request, "graph.html", {'graphs': graph_list,
                                          'form': form})
