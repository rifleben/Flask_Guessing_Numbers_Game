from flask import Flask
import random

random_int = random.randint(0, 9)
print(random_int)

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Return a friendly HTTP greeting to start the game."""
    return '<h1 style="color:blue;"> Hello, Friend, Guess a number between 0 and 9!</h1>' \
           '<img src="https://media0.giphy.com/media/NAy2FD8xWrH4jUIBrq/giphy.gif?cid=ecf05e470n8pmrll085um85n7dmvfn4uyhu7ckevxvz0b5e3&rid=giphy.gif&ct=g" width=300>'


@app.route('/<int:number>')
def return_number(number):
    """returns if the number is the correct guess or not"""
    if number == random_int:
        return '<h1 style="color:blue;"> You found me!</h1>' \
               '<img src="https://media4.giphy.com/media/xDd7UQJcd3Z16FZqvu/giphy.gif?cid=ecf05e47il7h4j2acdapy57g5cnpda8dac2k87ybb2cncbpe&rid=giphy.gif&ct=g" width=300 >'
    elif number > random_int:
        return '<h1 style="color:blue;"> Too high, try again!</h1>' \
               '<img src="https://media2.giphy.com/media/MwrQvTZA9Puuc/giphy.gif?cid=ecf05e47sb3ew89hu83qkz6uql7ilrb6korsu50f07mc1smz&rid=giphy.gif&ct=g" width=300 >'
    else:
        return '<h1 style="color:blue;"> Too low, try again!</h1>' \
               '<img src="https://media1.giphy.com/media/rS2uLYRGkGWySNX69v/giphy.gif?cid=ecf05e47xw11b9vh4hej8lzj0k3nokpa30urtvv94d13mhfo&rid=giphy.gif&ct=g" width=300 >'


if __name__ == '__main__':
    app.run(debug=True)
