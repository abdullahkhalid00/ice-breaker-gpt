import gradio as gr
from ui import demo
from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def root():
    return 'Gradio app running at /gradio', 200

app = gr.mount_gradio_app(app=app, blocks=demo, path='/gradio')
