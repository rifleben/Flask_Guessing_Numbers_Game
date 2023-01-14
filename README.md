# Flask_Guessing_Numbers_Game

![](https://github.com/rifleben/Flask_Guessing_Numbers_Game/blob/main/Flask_game_gif.gif)

Learning by doing...! First time working with Flask and learning a bit about the webDev side of Python.

This is a simple number guessing game built using Flask, a micro web framework for Python. The game generates a random integer between 0 and 9, and the user is prompted to guess the number by visiting the / endpoint of the server.

The / route returns a friendly greeting to start the game, along with an image to entertain the user.

The /<int:number> route is used to submit the user's guess. If the guess is correct, the user will be informed that they found the number and an image will be displayed. If the guess is too high or too low, the user will be informed and another image will be displayed.

To run the game, simply start the server with the command flask run. The server will be running on http://localhost:5000/.

The game also has a debug mode that can be run by passing debug=True to the app.run() function, if you're in development mode.

### Note:

If you are running on a Mac with Airdrop/Airplay on, you may need to disable or move the port in which the game is played.

More details here:

https://stackoverflow.com/questions/69818376/localhost5000-unavailable-in-macos-v12-monterey
