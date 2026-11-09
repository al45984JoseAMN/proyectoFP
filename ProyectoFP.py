print("Bienvenido")
nombre = input("Nombre: ")
edad = int(input("Edad: "))
peso = float(input("Peso actual (kg): "))
altura = float(input("Altura (m): "))
agua = int(input("Agua consumida diaria (ml): "))
metros = int(input("Metros recorridos hoy: "))
sistolica = int(input("Presion arterial sistolica: "))
diastolica = int(input("Presion arterial diastolica: "))

# Calculos de salud

# Calculo de IMC y rangos de peso
imc = peso / (altura ** 2)
peso_min = 18.5 * (altura ** 2)
peso_max = 24.9 * (altura ** 2)

# Calculo de Presion Arterial Media (PAM)
pam = (sistolica + (2 * diastolica)) / 3

# Metas ideales de referencia
meta_agua = 2000
meta_metros = 5000

print(f"       REPORTE DE SALUD        ")
print(f"Paciente: {nombre} ({edad} años)")
print(f"Altura: {altura} m | Peso Actual: {peso} kg")

# Peso y IMC
print(f"1. Peso y IMC:")
print(f"   - IMC Calculado: {imc:.2f}")
print(f"   - Rango de peso saludable: {peso_min:.1f} kg a {peso_max:.1f} kg")

if peso < peso_min:
    pesoF = peso_min - peso
    print(f"   - Estado: Peso por debajo de lo normal.")
    print(f"   - Que cambiar: Te faltan {pesoF:.1f} kg para alcanzar el limite inferior saludable. Se sugiere una dieta nutritiva e hipercalorica.")
elif peso > peso_max:
    sobrePeso = peso - peso_max
    print(f"   - Estado: Sobrepeso detectado.")
    print(f"   - Que cambiar: Debes reducir {sobrePeso:.1f} kg para llegar al limite superior saludable mediante deficit calorico y ejercicio.")
else:
    print(f"   - Estado: Tu peso se encuentra en el rango ideal.")

# Hidratacion
print(f"2. Hidratacion:")
print(f"   - Consumo actual: {agua} ml")
print(f"   - Meta diaria recomendada: {meta_agua} ml")

if agua < meta_agua:
    aguaI = meta_agua - agua
    print(f"   - Estado: Consumo insuficiente.")
    print(f"   - Que cambiar: Te faltan {aguaI} ml de agua al dia para cumplir con la meta.")
else:
    print(f"   - Estado: Excelente hidratacion diaria.")

# Actividad fisica
print(f"3. Actividad Fisica:")
print(f"   - Metros recorridos: {metros} m")
print(f"   - Meta diaria recomendada: {meta_metros} m")

if metros < meta_metros:
    faltante_metros = meta_metros - metros
    print(f"   - Estado: Actividad baja.")
    print(f"   - Que cambiar: Te faltan {faltante_metros} metros de caminata para alcanzar la meta establecida.")
else:
    print(f"   - Estado: Meta de actividad fisica cumplida.")

# Presion arterial
print(f"4. Presion Arterial:")
print(f"   - Presion registrada: {sistolica}/{diastolica} mmHg")
print(f"   - Presion Arterial Media (PAM): {pam:.1f} mmHg")

if sistolica > 120 or diastolica > 80:
    print(f"   - Estado: Presion arterial elevada.")
    print(f"   - Que cambiar: Se recomienda moderar el consumo de sal, manejar el estres y consultar a un especialista.")
else:
    print(f"   - Estado: Presion arterial en valores optimos.")