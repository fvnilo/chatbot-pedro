import os
import aiml
import yaml

class Bot:
    """AIML Kernel wrapper that represents a bot"""
    def __init__(self, verbose = False, config='bot.yaml'):
        """Ctor"""
        stream = file(config)
        self._predicates = yaml.load(stream)
        self._kernel = aiml.Kernel()
        self._verbose = verbose
        self._setPredicates()

    def _setPredicates(self):
        """Sets the settings to the bot"""
        keys = self._predicates.viewkeys()
        for key in keys:
            self._kernel.setBotPredicate(key, self._predicates[key])

    def _print_if_verbose(self, message):
        """Prints the messages if verbose mode is on"""
        if self._verbose: print message
    
    def learn(self, aiml_file):
        """Learn an .aiml file to the bot"""
        self._kernel.learn(aiml_file)
            
    def learn_all(self, reset=True):
        """Learn all the files .aiml files in the current working directory"""
        if reset:
            self.reset()
                    
        for aiml_file in os.listdir("aiml"):
            if aiml_file.endswith(".aiml"):
                self.learn(os.path.join('aiml', aiml_file))

    def start(self, prompt="> "):
        """Start the interaction with the bot"""
        while True:
                print self._kernel.respond(raw_input(prompt))

    def reset(self):
        """Reset the bot's brain"""
        self._kernel.resetBrain()
        self._setPredicates()
        self._print_if_verbose("Bot reset successful")

