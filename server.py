"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

MEAN_WORDS = [
  'a loser', 'horrible', 'not good', 'a butt-face', 'a butt-wipe', 'bad', 'dumb', 'silly-brain' 
]

stylestuff = """<style>
                .rainbow {
                -webkit-box-sizing: content-box;
                -moz-box-sizing: content-box;
                box-sizing: content-box;
                cursor: pointer;
                border: none;
                font: normal normal bold 70px/normal "Bad Script", Helvetica, sans-serif;
                color: rgba(0, 0, 0, 0);
                text-align: center;
                -o-text-overflow: clip;
                text-overflow: clip;
                text-shadow: 3px 0 0 rgb(217,31,38) , 6px 0 0 rgb(226,91,14) , 9px 0 0 rgb(245,221,8) , 12px 0 0 rgb(5,148,68) , 15px 0 0 rgb(2,135,206) , 18px 0 0 rgb(4,77,145) , 21px 0 0 rgb(42,21,113) ;
                -webkit-transition: all 600ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
                -moz-transition: all 600ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
                -o-transition: all 600ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
                transition: all 600ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
              }
              
              .rainbow:hover {
                text-shadow: -3px 0 0 rgb(217,31,38) , -6px 0 0 rgb(226,91,14) , -9px 0 0 rgb(245,221,8) , -12px 0 0 rgb(5,148,68) , -15px 0 0 rgb(2,135,206) , -18px 0 0 rgb(4,77,145) , -21px 0 0 rgb(42,21,113) ;
                -webkit-transition: all 500ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
                -moz-transition: all 500ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
                -o-transition: all 500ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
                transition: all 500ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
              } 
        </style>"""
def select_compliment(compliments):
    option_values = []
    for i in compliments:
        option_values.append('<option value="{}">{}</option>'.format(i, i.title()))

    return "\n".join(option_values)


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>
      <body>
      Hi! This is the home page.<br>
      <a href="/hello">Be nice to me</a><br>
      <a href="/dis">Be mean to me</a><br>
      </body>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          Choose your compliment: 
          <select name="compliment">
            {}
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """.format(select_compliment(AWESOMENESS))

@app.route('/dis')
def dis():
    """Say hello and prompt for user's name."""
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          Choose your disrespect: 
          <select name="compliment">
            {}
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """.format(select_compliment(MEAN_WORDS))


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")



    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
      <link async href="http://fonts.googleapis.com/css?family=Bad%20Script" data-generated="http://enjoycss.com" rel="stylesheet" type="text/css"/>
        <title>A Compliment</title>
{style}
      </head>
      <body>
        <div><p class="rainbow">Hi, {player}! I think you're {compliment}!</p></div>
      </body>
    </html>
    """.format(player=player.title(), compliment=compliment, style=stylestuff)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
