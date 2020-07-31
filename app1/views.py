import json
from django.shortcuts import render
from coviod19.settings import COVIOD19_FILE


def showIndex(request):
    dict_data= json.loads(open(COVIOD19_FILE).read())          #import from settings
    states=[x for x in dict_data]
    states.pop(0)

    return render(request,'index.html',{'data':states})


def details(request):
    state=request.GET.get('state_detail')

    dict_data = json.loads(open(COVIOD19_FILE).read())
    d=[]
    r=[]
    a=[]
    c = []
    for x,y in dict_data[state]['districtData'].items():

        res = {key: val for key, val in y.items()   #filter dictionary values from  heterogeneous dictinory using dict comprehension
               if isinstance(val, int)}             #where type is int type
        conf= res.get('confirmed')
        c.append(conf)
        act=res.get('active')
        a.append(act)
        reco=res.get('recovered')
        r.append(reco)
        dec=res.get('deceased')
        d.append(dec)
    con=sum(c)
    active=sum(a)
    recover=sum(r)
    decea=sum(d)
    return render(request,'state_detail.html',{'data1':state,'data2':dict_data[state],'confirmed':con,'active':active,'recover':recover,'deceased':decea})



