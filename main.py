from fastapi import FastAPI


app = FastAPI()


@app.get('/home')
def get_home_page():
    return 'Hello world'
