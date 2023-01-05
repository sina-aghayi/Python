def greet (lang):
    if lang == 'fa' :
        print("salam")
    elif lang == 'es' :
        print('hola')
    elif lang == 'fr' :
        print('Bonjour')
    else :
        print('please use es , fa or fr')
greet('fa')