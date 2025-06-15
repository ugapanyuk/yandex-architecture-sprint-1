import random
import datetime
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Input(BaseModel):
    name: str
    type: str
    location: str
    unit: str


class TemperatureData(BaseModel):
    value: int | None
    unit: str
    timestamp: str | None
    location: str
    status: str
    sensor_id: int
    sensor_type: str
    description: str


data = {}

app = FastAPI()


def rand_temp():
    return random.randint(18, 28)

def dt():
    return str(datetime.datetime.now())    


@app.get("/temperature/")
async def get_by_location(location: str):
    return TemperatureData(
                value = rand_temp(),
                unit = str('C'),
                timestamp = dt(),
                location = str(location),
                status = 'active',
                sensor_id = '1',
                sensor_type = 'temperature',
                description = 'Temperature sensor in ' + str(location),
        )



@app.post("/api/v1/sensors/")
async def create_sensor(input: Input):
    data[input.location] = \
        TemperatureData(
            value = None,
            unit = str(input.unit),
            timestamp = None,
            location = str(input.location),
            status = 'active',
            sensor_id = '1',
            sensor_type = str(input.type),
            description = 'Temperature sensor in ' + str(input.name),
        )
    return input


@app.get("/api/v1/sensors/")
async def get_all_sensors():
    for x in data.values():
        x.value = rand_temp()
        x.timestamp = dt()
    return [x for x in data.values()]

