# Lista dos valores da glicemia 
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

# Realizando uma list comprehension utilizando if e else
rotulos = [
    ('Hipoglicemia', glicose) if glicose <= 70
    else ('Normal', glicose) if glicose < 100
    else ('Alterada', glicose) if glicose < 125
    else ('Diabetes', glicose)
    for glicose in glicemia
]

# Exibindo o resultado
print(rotulos)
