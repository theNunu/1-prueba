import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

# Generar datos de ejemplo de etiquetas reales y predichas
actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)

# Crear la matriz de confusión utilizando sklearn
confusion_matrix = metrics.confusion_matrix(actual, predicted)

# Crear la visualización de la matriz de confusión
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])

# Graficar la matriz de confusión
cm_display.plot()
plt.show()

"""  
Resultado Explicado
La Matriz de Confusión creada tiene cuatro cuadrantes diferentes:

Negativo verdadero (cuadrante superior izquierdo)
Falso positivo (cuadrante superior derecho)
Falso negativo (cuadrante inferior izquierdo)
Verdadero positivo (cuadrante inferior derecho)
Verdadero significa que los valores se predijeron con precisión, Falso significa que hubo un error o una predicción incorrecta.

"""