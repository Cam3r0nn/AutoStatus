# AutoStatus
Automatically change your custom Discord status!

This is a simple python script that will change your custom Discord status.
You just make a .env file in the same directory as the script and write whats below in the file.

> TOKEN=TOKENHERE

Then next you will create a messages.txt in the same directory as the script.
You will put new status messages on a new line, it will randomly select a message.

Now, finally you will go on line 51 and change the following:

> STATUS -> dnd, idle, online

> EMOJI_NAME -> Emoji's Name

> EMOJI_ID -> Emoji's ID

And if you want to change the interval in which it updates go to line 52,
and change 3660 to whatever you please, the time is in seconds.
