import gradio as gr
from inference import generate_question


def main():
    app = gr.Interface(
        title='Ice Breaker GPT 🧊🔨',
        fn=generate_question,
        inputs=[],
        outputs=gr.Textbox(label='Host'),
        theme=gr.themes.Monochrome(
            font=[gr.themes.GoogleFont('Inconsolata'), 'Arial', 'sans-serif']
        ),
        allow_flagging='never',
    )
    app.launch()


if __name__ == '__main__':
    main()
