accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Exactitud:", accuracy)
print("Matriz de confusión:\n", conf_matrix)
print("Reporte de clasificación:\n", report)