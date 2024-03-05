from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from routes.route import router

app = FastAPI()
app.include_router(router)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Default route for the homepage:
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Welcome to Asset Performance Analytics Dashboard</title>
            <style>
                body {
                    background-color : black;
                    font-family: Arial, sans-serif;
                    margin: 50px;
                }
                .container {
                    background-color : gray;
                    width: 60%;
                    text-align: center;
                    padding: 20px;
                    border: 2px solid cyan;
                    border-radius: 8px;
                    margin: 0 auto;
                    margin-top: 100px;
                }
                .container:hover {
                    box-shadow: 4px 4px 11px cyan;
                    background-color: darkgray;
                }
                h1 {
                    color: blue;
                }
                p {
                    color: white;
                }
                a {
                    color: #007bff;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                    color:red
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to Asset Performance Analytics Dashboard</h1>
                <p>This is a sample FastAPI application serving as the backend for an Asset Performance Analytics Dashboard.</p>
                <p>To explore the API documentation and test the endpoints, please go to <b><a href="/docs">/docs</a></b></p>
            </div>
        </body>
    </html>
    """

# Redirect /docs to Swagger UI
@app.get("/docs", include_in_schema=False)
async def get_docs():
    return RedirectResponse("/docs")
