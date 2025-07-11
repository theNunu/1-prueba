# strip    -Elimina los espacios al principio y al final de la cadena:
txt = "   la manzana   "
x = txt.strip()

print("de todas las frutas", x, "es mi favorita")
print("de todas las frutas", txt, "es mi favorita")

print(" -- Ejemplo para eliminar los caracteres iniciales y finales ---")


txt = ",,,,,sszzoo....yellow.manzana..."

x = txt.strip(",.szimaon")
#eliminar los caracteres iniciales y finales de la cadena que se encuentran en la lista ",.szoi" .

print(x)