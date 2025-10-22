# Strings

texto = "Curso Backend Python"

print (texto.lower())
print (texto.upper())
print (texto.capitalize())
print (texto.title())
print (texto.strip())
print (texto.lstrip())
print (texto.rstrip())
print (texto.replace("Curso", "Aula de"))
"Curso" in texto # operador in
print (texto.find("a"))
print (texto.index())
print (texto.startswith("Curso")) 
print (texto.endswith("Python"))
print (texto.split()) 
novo_texto = texto.split("-")
print (novo_texto)
texto_novo = "-".join(novo_texto)
print (texto_novo)
print (texto.isdigit())
print (texto.isalpha())
print (texto.isalnum())
print (texto.isspace())

# Formatação f-strings

curso = "Python"

dia = "Terças e Quintas"

num_dec = 0.736482521

print(f'o curso de {curso} acontece as {dia}, {num_dec:0.2f}')

#Encode, decode normalmente utilizados quando for trafegar dados

texto = "Olá, fração, decoding" 

b_utf = texto.encode('utf-8')

print (b_utf)

texto_decodificado = b_utf.decode('utf-8')

print(texto_decodificado)