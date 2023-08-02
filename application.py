from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application = Flask(__name__)

app=application

## Route for a home page

@app.route('/predictdata')

def index():
    return render_template('index.html')


@app.route('/',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    
    else:

        data=CustomData(
                bedrooms= int(request.form.get('bedrooms')),
                bathrooms= float(request.form.get('bathrooms')),
                floors= float(request.form.get('floors')),
                condition= int(request.form.get('condition')),
                grade= int(request.form.get('grade')),
                yr_built= int(request.form.get('yr_built')),               
                sqft_living= int(request.form.get('sqft_living')),
                sqft_lot= int(request.form.get('sqft_lot')),
                sqft_above= int(request.form.get('sqft_above')),
                sqft_basement= int(request.form.get('sqft_basement')),
                lat= float(request.form.get('lat')),
                longs= float(request.form.get('longs'))
        )
        
        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        print(results)
        return render_template('home.html',results=results[0])        

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)  