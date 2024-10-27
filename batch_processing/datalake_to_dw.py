import sys
import os
import warnings
import traceback
import logging
import time
import dotenv
dotenv.load_dotenv('.env')

from pyspark import SparkConf, SparkContext

utils_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')) # Going back to utils directory
sys.path.append(utils_path)
from helpers import load_cfg
from minio_utils import MinIOClient

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(funcname)s:%(levelname)s:%(message)s')
warnings.filterwarnings('ignore')

#################################
# Parameters & Arguments
#################################
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
DB_STAGING_TABLE = os.getenv('DB_STAGING_TABLE')

CFG_FILE = "./config/datalake.yaml"
cfg = load_cfg(CFG_FILE)
datalake_cfg = cfg['datalake'] # Transform into a dictionary-like variable

MINIO_ENDPOINT = datalake_cfg['endpoint']
MINIO_ACCESSKEY = datalake_cfg['access_key']
MINIO_SECRETKEY = datalake_cfg['secret_key']
BUCKET_NAME = datalake_cfg['bucket_name_2']

CFG_FILE_SPARK = "./config/spark.yaml"

