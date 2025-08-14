populacaoA = 80000
populacaoB = 200000
anos = 0

while populacaoB >= populacaoA:
    populacaoA += (populacaoA * 0.03) 
    populacaoB += (populacaoB * 0.015) 
    anos += 1

print(f"Levariam {anos} anos para que a que a população do país A ultrapassasse ou igualasse a população do país B.")