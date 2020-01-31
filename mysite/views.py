from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def query(request, qstr=''):
	if qstr == 'allstore':
		res = {
		'id_1':'迷克夏',
		'id_2':'大苑子',
		'id_3':'星巴克',
		'id_4':'全家',
		'id_5':'7-11',
		}
	return JsonResponse(res)