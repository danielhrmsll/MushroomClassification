import joblib

def preditct(data,model):
    if model == "Support Vector Machine":
        model = joblib.load(f'modelos/modelo_svm.joblib')
    elif model == "Random Forest Classifier":
        model = joblib.load(f'modelos/modelo_rf.joblib')
    elif model == "Extra Trees Classifier":
        model = joblib.load(f'modelos/modelo_et.joblib')
    
    return model.predict(data)