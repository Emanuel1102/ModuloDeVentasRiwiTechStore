# funcion en caso de que el usuario ingrese el texto con espacios

def text_capitalize(texto):
    text_capitalize=[]

    for palabra in texto.split(' '):
        text_capitalize.append(palabra.capitalize())
    
    return ''.join(text_capitalize)