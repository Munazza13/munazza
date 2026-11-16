# predict.py
import joblib
import pandas as pd
from sklearn.datasets import load_breast_cancer
#step 1: Load the saved model
def loadd_model(model_path="best_model.joblib"):
  model=joblib.load(model_path)
  return model 
#Step 2: Create a resuable prediction function
def make_prediction(model,input_data)
 prediction=model.predict(input_data)
 probabilities=mode.predict_proba(input_data)
 result="Maligant" if prediction[0]==0 else "benign"
 return{
  "prediction":result,
  "probabilities":{
     "malignant":probabilities[0][0],
      "benign":probabilities[0][1]
  }
 }
#Step 3:Run a sample prediction when executed directly
if __name__=="__main__":
   model=load_breast_cancer()
   feature_names=data.feature_names
   sample_input=dict(zip(feature_names,data.data[0]))
#Modify a few values for demonstraion
sample_input["mean radius"]=15.0
sample_input["mean texture"]=18.0
sample_input["mean perimeter"]=100.0
input_df=pd.DataFrame(
   [sample_input],
   columns=feature_names
)
output=make_prediction(model,input_df)
print("Model loaded successfully!")
print("\nPrediction:", output["prediction"])
orint("\nPrediciton probabilities:")
print("Malignant:",output["probabilities"]["malignant"])
print("Benign:",output[probabilities"]["benign"])
  
