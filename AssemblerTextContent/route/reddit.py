from controller import reddit as redditController
from fastapi import APIRouter


redditRouter = APIRouter(
    prefix="/reddit",
    tags=["Reddit"],
    responses={404: {"description": "Not found"}},
)   



@redditRouter.get("/get-cycle-reddit/{cycle}")
async def getReddit(cycle:int):
    return redditController.getRedditsByCycle(cycle)