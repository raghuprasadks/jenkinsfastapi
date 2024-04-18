from fastapi import FastAPI
import mangum
import uvicorn

app = FastAPI()
# comment
@app.get("/")
def read_root():
    return {"Hello": "NH Team"}

@app.get("/jenkins")
def read_root():
    return {"Hello": "Jenkins Team"}

handler = mangum.Mangum(app)

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8080)
