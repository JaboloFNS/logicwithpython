anos_exp = int(input("Digite quantos anos de experiência na área você tem:"))

if anos_exp == 0:
    nivel = "Estagiário"
elif anos_exp > 0 and anos_exp <= 3:
    nivel = "Junior"
elif anos_exp > 3 and anos_exp <= 8:
    nivel = "Pleno"
else:
    nivel = "Senior"

print (f"Seu nível de experiência é equivalente a {nivel}")

