import os
import glob
import datetime
import logging
import joblib

from flask import Flask, request


logging.basicConfig(
    level=logging.WARNING,
    filename=f"applog_{datetime.date.today()}.log",
    filemode='a',
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'
)
logging.info("logging file opened")

APP = Flask(__name__)

ENVIRONMENT_CONFIGURATION = "config.DevelopmentConfig"
APP.config.from_object(ENVIRONMENT_CONFIGURATION)


def load_model(model_name):
    """Load the most recent model from joblib file"""
    dir_path = os.getcwd()
    list_of_files = glob.glob(f"{dir_path}/{model_name}*.joblib")
    latest_file = max(list_of_files, key=os.path.getctime)
    model = joblib.load(latest_file)
    return model


@APP.route('/run', methods=['POST'])
def run_model():
    """Run the requested model with supplied data"""
    request_data = request.get_json(force=True)
    model_name = request_data['model']
    model = load_model(model_name)
    try:
        data = request_data['data']
        result = model.predict(data)
    except KeyError:
        message = "ERROR - no data was passed to the api"
        logging.error(message)
        result = 'no data was passed to the api'

    return f"You requested a {model_name} model run\n\nPredicted result: {result}\n"


@APP.route('/list_models', methods=['GET'])
def list_models():
    """Return a list of currently stored model files"""
    dir_path = os.getcwd()
    list_of_files = glob.glob(f"{dir_path}/*.joblib")
    return list_of_files

if __name__ == "__main__":
    APP.run(port=8000, debug=True)
