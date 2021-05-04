import uvicorn
from fastapi import FastAPI  # type:ignore
from fastapi.responses import UJSONResponse  # type:ignore
from mabel.logging import get_logger, set_log_name
from models import ExampleModel  # remove this in your app

set_log_name("TEMPLATE")
logger = get_logger()
app = FastAPI()


@app.post('/example', response_class=UJSONResponse)  # remove this in your app
def handle_example_request(parameters: ExampleModel):
    try:
        # hash the payload so we have a unique ID for it, the allows us to 
        # match logs
        request_id = abs(hash(parameters.json()))
        logger.debug(F"Started ID:{request_id}")

        # this is where the work should be done

    except Exception as err:
        error_message = F"{type(err).__name__}: {err} (ID:{request_id})"
        logger.error(error_message)
        return {}, 500
    finally:
        logger.debug(F"Finished ID:{request_id}")

    return {}, 200


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)  
