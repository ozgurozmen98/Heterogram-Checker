k_input = input("Bir kelime gir : ")   # girdi sağlıyorum
k_input = k_input.lower() # girdiyi küçültüyorum

kosul = (len(k_input) == len(set(k_input)))   # len ile uzunlugunu alıyorum set ile uniq kontrolü sağlıyorum

print(kosul)


