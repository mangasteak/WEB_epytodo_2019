#!/usr/bin/env python3

from app import app

app.secret_key = "very_secret_key"
app.run()