print("Escreva o texto para ser convertido: ")
a=input()

def morse(txt):
    d = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
         'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
         'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
         'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
         'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
         'Z':'--..', ' ':'.....'}
    translation = ''
    if txt.startswith('.') or txt.startswith('−'):
        d_encrypt = dict([(v, k) for k, v in d.items()])
        txt = txt.split(' ')
        for x in txt:
            translation += d_encrypt.get(x)
    else:
        txt = txt.upper()
        for x in txt:
            translation += d.get(x) + ' '
    return translation.strip()

print("Texto convertido: ")  
print(morse(a))