import pygtrie as trie
import logging

class NoSuchCommandError(KeyError):
    def __init__(self, command):
        self.command = command

class CommandTree:
    def __init__(self):
        self.command_trie = trie.CharTrie()

    def build(self, commands):
        for command in commands:
            name = command[0]
            handler = command[1]
            self.add_command(name[-1], handler=handler, *name[:-1]) # last element is the command to add, the rest are prior supercommands

    def add_command(self, command, *supercommands, **kwargs):
        handler = kwargs.get('handler', None)
        
        supercommands = list(supercommands)
        full_command = ' '.join(supercommands + [command])
        self.command_trie[full_command] = handler

    def get_possible_postfix(self, command_prefix):
        return list(self.command_trie.iterkeys(prefix=command_prefix, shallow=True))

    def get_command(self, command):
        match = self.command_trie.longest_prefix(command)
        if not match:
            raise NoSuchCommandError(command)
        return match