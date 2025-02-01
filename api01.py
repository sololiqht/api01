from fastapi import FastAPI

app = FastAPI()

@app.get("/get-message")
async def read_root():
    return {"message": "Congrats this is your first API"}

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1",port="8000")



#initial static string
static_string = "Initil_text"

@app.post("/add")
async def add_text(text:str):
    global static_string
    static_string += text
    return {"message":"Text added", "Current string": static_string}

@app.change("/change")
async def change_text(new_text:str):
    global static_string
    static_string = new_text
    return {"message":"Text changed", "Current string": static_string}

@app.delete("/delete")
async def delete_text():
    global static_string
    static_string = ""
    return {"message":"Text deleted","Current string": static_string}
