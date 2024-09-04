from os import getenv
from app import app
from pyrogram.client import Client
from pyrogram.filters import user
from pyrogram.types import Message

def edit_message(text: str) -> str:
    table: dict[str, str] = { 'з': 'Z', 'в': 'V', 'З': 'Z', 'В': 'V'}
    return text.translate(text.maketrans(table))

@app.on_message(filters=user(getenv(key='ME')))
def on_message(_: Client, message: Message) -> None:
    message.edit_text(text=edit_message(message.text))

if __name__ == '__main__':
    app.run()