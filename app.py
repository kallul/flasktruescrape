import time, os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from collections import OrderedDict
import json
from flask import Flask, render_template, Response, request, redirect, url_for


app = Flask(__name__)



if __name__ == '__main__':
    app.run()
