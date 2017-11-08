import urllib.request
from . import models


def read_from_file(url):
    file = urllib.request.urlopen(url)
    data_bytes = file.read()
    data_string = data_bytes.decode("utf8")
    file.close()
    return data_string
    
def save_raamatud(data_string):
    data = data_string.splitlines()
    dataLen = len(data)
    
    kasKirjeteArvudSamad = (models.raamatud.objects.all().count() >= (dataLen-1))
    
    if(not kasKirjeteArvudSamad):
        for i in range(1, dataLen):
            attribute = data[i].split(',')
            model = models.raamatud()
            omanikeModel = models.omanikud()
            model.raamatu_nr = attribute[0]
            model.raamatu_nimi = attribute[1]
            model.raamatu_lehti = attribute[2]
            
            model.save()
            for item in models.omanikud.objects.all():
                if(int(item.omatud_raamatu_nr) == int(attribute[0])):
                    model.omanikud.add(item)

def save_omanikud(data_string):
    data = data_string.splitlines()
    dataLen = len(data)
    
    kasKirjeteArvudSamad = (models.raamatud.objects.all().count() >= (dataLen-1))
    
    if(not kasKirjeteArvudSamad):
        for i in range(1, dataLen):
            attribute = data[i].split(',')
            model = models.omanikud()
            model.id = attribute[0]
            model.omaniku_nr = attribute[1]
            model.omanik_nimi = attribute[2]
            model.omatud_raamatu_nr = attribute[3]
            
            model.save()
            