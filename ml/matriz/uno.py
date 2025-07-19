from sklearn.metrics import confusion_matrix


print("""
    Ejemplo de cómo crear una matriz de confusión utilizando scikit-learn   
      """)


# Crear la matriz de confusión
y_real = [1, 0, 0, 1, 1, 1, 0, 1, 0, 0]
y_pred = [1, 1, 0, 1, 0, 1, 0, 0, 1, 0]

# Datos de ejemplo: valores reales y predichos
matriz_confusion = confusion_matrix(y_real, y_pred)

print("Matriz de confusión")
print(matriz_confusion)