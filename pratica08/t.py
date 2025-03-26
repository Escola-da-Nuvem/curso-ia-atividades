from sklearn.model_selection import train_test_split

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=42)
