#!/usr/bin/env python
# coding: utf-8

# In[60]:

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}

import pandas as pd
import numpy as np
import pickle as pkl
#from tensorflow import keras
import json

import uvicorn
from fastapi import Body, FastAPI
from apiExamples import *

import logging
import datetime

from pydantic import BaseModel, Field
from typing import Optional, Union, NewType, Tuple, List, Dict, DefaultDict

import argparse

from random import randint, choice, seed
seed(0) 


from fastapi.middleware.cors import CORSMiddleware



# In[61]:
#####################################################################################################################################
#HelloWorldEx = Body(...,
#    examples={"simple": {"summary": "One sample example.",
#                         "description": "One sample example",
#                         "value": {"hello": "hello"},
#                         },
#             })
#
#HelloWorldRe =  {200: {"description": "Success",
#                       "content": {
#                                   "application/json": {
#                                                        "examples": {"simple": {
#                                                                                "summary": "One sample example.",
#                                                                                "value": {"hello": "world", "status":200}
#                                                                               },
#                                                                    }
#                                                       }
#                                  }
#                      },
#                 400: {"description": "Success",
#                       "content": {
#                                   "application/json": {
#                                                        "examples": {"simple": {
#                                                                                "summary": "One sample example.",
#                                                                                "value": {"hello": "", "status":404}
#                                                                               },
#                                                                    }
#                                                       }
#                                  }
#                      },
#                }
#
#HelloWorld = NewType('HelloWorld', str)
#class HelloWorldData(BaseModel):
#    hello: HelloWorld
#
#class HelloWorldReturn(BaseModel):
#    hello: HelloWorld
#    status: int
######################################################################################################################################

# preload
#taxonomyTable = pd.read_csv('TaiwanSpecies20210813_UTF8.csv')
plg2coor = pkl.load(open('plg2coor.pkl', 'rb'))

# new types
Array = NewType('Array', List[List[float]])
Date = NewType('Date', datetime.datetime)
Polygons = NewType('Polygons', List[int] )
Heatmaps = NewType('Heatmaps', List[Dict])
List2D = NewType('Track', List[List])
  
# self-defined request & response
class Request(BaseModel):
    polygon: Polygons
    name: str # 學名
    date: Date
    
class BioInfoRsp(BaseModel):
    name: str # 學名
    taxonomy: Dict # 界門綱目科屬種
    others: Dict # 其他資訊
    status: int

class BioDistRsp(BaseModel):
    heatmap: Heatmaps
    featimp: Dict # 特徵重要度 
    status: int
    
class BioTrackRsp(BaseModel):
    track: List2D
    status: int
    
class EcoDivRsp(BaseModel):
    thld: float
    diversity: List2D    
    status: int
    
def Query(table, condition):
    if table == 'taxonomy':
        df = taxonomyTable
        for n, v in condition.items():
            df = df[df[n] == v]
    return df.copy()

app = FastAPI()


#####################################################################################################################################
#@app.post("/helloworld", response_model=Union[HelloWorldReturn, bytes], responses=HelloWorldRe)
#async def helloworld(j: Union[HelloWorldData, bytes] = HelloWorldEx):
#    """
#    說明：hello world 測試用 api
#    路徑：/helloworld
#    方法：POST  
#    輸入：json  
#    json keys：{"hello":字串}  
#              當 "hello" 字串為 "world" 就回應 "world"，其他的值就會回空字串 ""
#         
#         例：
#         {"hello": "hello" 
#         }
#    """
#    try:
#        if not isinstance (j, bytes):
#            hello = 'world'if np.array(j.hello) == 'hello' else ':('
#            status = 200
#        else:
#            d = json.loads(j.decode("utf-8").replace("\n", ''))
#            hello = 'world'if np.array(d['hello']) == 'hello' else ':('
#            status = 200
#        
#    except Exception as e:
#        logging.basicConfig(filename='api.log', level=logging.DEBUG)
#        t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#        logging.error(f'[{t}] api:helloworld {e}')
#        hello = ''
#        status = 400
#    
#    return {"hello":hello, "status":status}
#####################################################################################################################################


@app.post("/api/bioinfo", response_model=Union[BioInfoRsp, bytes], responses=BioInfoRe)
async def bioinfo(j: Union[Request, bytes] = BioInfoEx):
    """
    Abstract: Bilology information of a species  
    Url: /api/bioinfo  
    Method: POST  
    Raw: Json / Text  
    Request: {"polygon": (<font color=red>not used here</font>) Array of indices between 0 and 2939 which maps to a 70×42 raster of Taiwan. 0 represents grid (0, 0) which is the most northwestern grid of the raster, 2939 represents grid (69, 41) which is the most southeastern grid of the raster.  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"name": String of the science name of the species.  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"date": (<font color=red>not used here</font>) Which season to query, should be the first day of the season.}  
    """

    name = ''    
    taxonomy = {'kingdom':'', 'kingdom':'', 'phylum':'', 'class':'', 'order':'', 'family':'', 'genus':'', 'species':''}
    others = {}
    status = 200
    try:
        if not isinstance (j, bytes): 
            name = j.name
        else:
            d = json.loads(j.decode("utf-8").replace("\n", ''))
            name = d['name']

        q = Query('taxonomy', {'name': name})
        taxonomy = q[['kingdom', 'kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'species']].to_dict('records')[0]
        print(q, taxonomy)
        
    except Exception as e:
        logging.basicConfig(filename='api.log', level=logging.DEBUG)
        t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.error(f'[{t}] api:auxinfo {e}')
        name = ''
        taxonomy = {'kingdom':'', 'kingdom':'', 'phylum':'', 'class':'', 'order':'', 'family':'', 'genus':'', 'species':''}
        others = {}    
        status = 400


    return {"name":name, "taxonomy":taxonomy, "others":others, "status":status}


@app.post("/api/biodist", response_model=Union[BioDistRsp, bytes], responses=BioDistRe)
async def biodist(j: Union[Request, bytes] = BioDistEx):
    """
    Abstract: Biology distribution of a species  
    Url: /api/biodist  
    Method: POST  
    Raw: Json / Text  
    Request: {"poligon": (<font color=red>not used here</font>) Array of indices between 0 and 2939 which maps to a 70×42 raster of Taiwan. 0 represents grid (0, 0) which is the most northwestern grid of the raster, 2939 represents grid (69, 41) which is the most southeastern grid of the raster.  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"name": String of the science name of the species.  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"date": (<font color=red>not used here</font>) Which season to query, should be the first day of the season.}  
    """    

    
    heatmap = [[]]
    featimp = {'altitude':10, 'vegetation':5, 'water content':7}
    status = 200    
    try:
        if not isinstance (j, bytes):
            polygons =[plg2coor[pid] for pid in j.polygon]
            name = j.name
            date = j.date
            heatmap =[ {"id": pid, "heatmap": (np.random.rand(3,3)*10).tolist()}  for pid in j.polygon ]
            featimp = {'altitude':randint(1,10), 'vegetation':randint(1,10), 'water content':randint(1,10)} ## to be changed
        else:
            d = json.loads(j.decode("utf-8").replace("\n", ''))
            polygons =[ plg2coor[pid] for pid in d['polygon'] ]
            name = d['name']
            date = d['date']
            heatmap =[ {"id": pid, "heatmap": (np.random.rand(3,3)*10).tolist()}  for pid in j.polygon ]
            featimp = {'altitude':randint(1,10), 'vegetation':randint(1,10), 'water content':randint(1,10)} ## to be changed

            
    except Exception as e:
        print('fuck happened')
        logging.basicConfig(filename='api.log', level=logging.DEBUG)
        t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.error(f'[{t}] api:helloworld {e}')
        heatmap = [[]]
        featimp = {'altitude':-99, 'vegetation':-99, 'water content':-99}
        status = 400
    
    return {"heatmap":heatmap, "featimp":{}, "status":status}


@app.post("/api/biotrack", response_model=Union[BioTrackRsp, bytes], responses=BioTrackRe)
async def biotrack(j: Union[Request, bytes] = BioTrackEx):
    """
    Abstract: Biology track of a species  
    Url: /api/biotrack  
    Method: POST  
    Raw: Json / Text  
    Request: {"poligon": Array of indices between 0 and 2939 which maps to a 70×42 raster of Taiwan. 0 represents grid (0, 0) which is the most northwestern grid of the raster, 2939 represents grid (69, 41) which is the most southeastern grid of the raster.  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"name": String of the science name of the species.  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"date": Which season to query, should be the first day of the season.}  
    """    

    
    track = [[]]
    status = 200        
    try:
        if not isinstance (j, bytes):
            polygons =[ plg2coor[pid] for pid in j.polygon ]
            name = j.name
            date = j.date            
            
            ts = [ datetime.datetime(2020, 1, 1), datetime.datetime(2020, 4, 1), datetime.datetime(2020, 7, 1), datetime.datetime(2020, 10, 1), 
                  datetime.datetime(2021, 1, 1), datetime.datetime(2021, 4, 1), datetime.datetime(2021, 7, 1), datetime.datetime(2021, 10, 1)]
            track = [[t]+ choice(choice(polygons)) for t, _  in zip(ts, range(randint(3,10))) ]
        else:
            d = json.loads(j.decode("utf-8").replace("\n", ''))
            polygons =[ plg2coor[pid] for pid in d['polygon'] ]
            name = d['name']
            date = d['date']
            track = [[t]+choice(choice(polygons)) for t, _  in zip(ts, range(randint(3,10))) ]


    except Exception as e:
        logging.basicConfig(filename='api.log', level=logging.DEBUG)
        t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.error(f'[{t}] api:helloworld {e}')
        track = [[]]
        status = 400
    
    return {"track":track, "status":status}


@app.post("/api/ecodiv", response_model=Union[EcoDivRsp, bytes], responses=EcoDivRe)
async def ecodiv(j: Union[Request, bytes] = EcoDivEx):
    """
    Abstract: Biology track of a species  
    Url: /api/biotrack  
    Method: POST  
    Raw: Json / Text  
    Request: {"poligon": Array of indices between 0 and 2939 which maps to a 70×42 raster of Taiwan. 0 represents grid (0, 0) which is the most northwestern grid of the raster, 2939 represents grid (69, 41) which is the most southeastern grid of the raster.  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"name": String of the science name of the species.  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"date": Which season to query, should be the first day of the season.}  
    """    

    
    thld = 10
    diversity = []    
    status = 200   
    try:
        if not isinstance (j, bytes):
            polygons =[ plg2coor[pid] for pid in j.polygon ]
            name = j.name
            date = j.date
            
            diversity = [ [datetime.datetime(y, m, 1), randint(20,50)] for y, m in zip([2019]*2+[2020]*4+[2021]*4, [7, 10, 1, 4, 7, 10, 1, 4, 7, 10])]
        else:
            d = json.loads(j.decode("utf-8").replace("\n", ''))
            polygons =[ plg2coor[pid] for pid in d['polygon'] ]
            name = d['name']
            date = d['date']
            
            diversity = [ [datetime.datetime(y, m, 1), randint(20,50)] for y, m in zip([2019]*2+[2020]*4+[2021]*4, [7, 10, 1, 4, 7, 10, 1, 4, 7, 10])]


    except Exception as e:
        logging.basicConfig(filename='api.log', level=logging.DEBUG)
        t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.error(f'[{t}] api:helloworld {e}')
        thld = 0
        diversity = []    
        status = 400
    
    return {"thld":thld, "diversity":[], "status":status}



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    def printTitle(title):
        print(f'-'*(len(title)-9+4))
        print(f'| {title} |')
        print(f'-'*(len(title)-9+4))

    parser = argparse.ArgumentParser()
    parser.add_argument('-port', metavar='PPPP', type=int, 
                        dest='port', action='store', default=8100,
                        help='port number for the api service')
    args = parser.parse_args()
    title = f"start DSP TAIPOWER API at sport \033[36m{args.port}\033[0m"
    printTitle(title)
    uvicorn.run(app, host="0.0.0.0", port=args.port)
