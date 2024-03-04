from fastapi import FastAPI
from routes.route import router

app = FastAPI()
app.include_router(router)


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)