calculations_of_resistance.py

 Ohm's Law: V = I * R
 Therefore:
 R = V / I
 V = I * R
 I = V / R

print("Resistance Calculator")
print("---------------------")

voltage = float(input("Enter voltage (V): "))
current = float(input("Enter current (A): "))

if current != 0:
    resistance = voltage / current
    print(f"Resistance = {resistance:.2f} Ω")
else:
    print("Current cannot be zero.")
