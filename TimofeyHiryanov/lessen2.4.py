d = {'Moscow': 78621, # Значение и ключ после пвоеточия
     'Dolgoprudny': 6283,
     'Piter': 2851}

d['Rostov'] = 762
for key in d:
    print(key)
    print(key, d[key])