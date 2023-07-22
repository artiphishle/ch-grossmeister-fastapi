#
# api-chess 'games'
#
# @RUN: uvicorn main:app --reload
# @API: http://127.0.0.1:8000/game/5?q=gm_game
# @DOC: http://127.0.0.1:8000/docs
#
from typing import Union
from fastapi import FastAPI
app = FastAPI()

redis = get_redis_connection(
    host="redis-11844.c135.eu-central-1-1.ec2.cloud.redislabs.com",
    port=11844,
    password="pRdcpRkk...",
    decode_responses=True
)

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database: redis

@app.get('/products')
async def all():
    return []

# GET root/welcome
@app.get("/")
async def read_root():
    return {"Yes!": "Chess API online!"}

# GET game by game_id
# @app.get("/game/{game_id}")
# async def read_game(game_id: int, q: Union[str, None] = None):
    # return {
        # "game_id": game_id,
        # "q": q}

@app.get("/game/{game_id}")
async def read_game(game_id: str):
    return {
        "game_id": game_id,
        "white": "Franc",
        "black": "Fabio",
        "fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 0",
        "event": "unrated games #1",
        "site": "grossmeister.ch",
        "result": "*"
    }