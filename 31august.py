# В банка е депозирано 1 кг злато на стойност 2500лв. , тече лихва 1.8% на месец.
# Колко е станала цената на златото с лихвите за 7 месеца?

Depozit_cold = int(input())
interest_rate = float(input())
cold_bonus = float(input())

mouth = Depozit_cold * 1.8

rate = cold_bonus * 1

result = mouth * rate / 100
january = result + 2500
print(january)

february = january * 1.8 / 100 + january
print(february)

march = february * 1.8 / 100 + february
print(march)

april = march * 1.8 / 100 + march
print(april)

may = april * 1.8 / 100 + april
print(may)

june = may * 1.8 / 100 + may
print(june)

july = june * 1.8 / 100 + june
print(july)