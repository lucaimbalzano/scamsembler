from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contentGenerator.textGenerator import GenerateTxtFile
from scraper.model.reddit.model import RedditListing, print_object
from scraper.core import Scraper
from scraper.settings import settings
from scraper.settings.browser import Browser
from route.reddit import redditRouter
import requests
import json


app = FastAPI()
app.include_router(redditRouter)
app.add_middleware(CORSMiddleware,
                   allow_methods=["*"],
                   allow_credentials=True,
                   allow_origins=["http://localhost:3000/"])

@app.get('/')
def run_check():
    return JSONResponse(content={"status": "Running!"})