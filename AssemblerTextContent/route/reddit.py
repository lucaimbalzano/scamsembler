from controller import reddit as redditController
from fastapi import APIRouter


redditRouter = APIRouter(
    prefix="/reddit",
    tags=["Reddit"],
    responses={404: {"description": "Not found"}},
)   



@redditRouter.get("/get-single-reddit")
async def get_books():
    return redditController.getSingleReddit()