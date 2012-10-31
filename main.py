import os
import sys
import bot

dir_path = os.path.dirname(sys.argv[0])
current_cwd = os.getcwd()

if dir_path != current_cwd:
        os.chdir(dir_path)

bot = bot.Bot(True)
bot.learn_all()
bot.start()