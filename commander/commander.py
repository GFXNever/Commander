import logging
import sys

if sys.version_info.major == 2:
    import completer
    import command_tree

    input_func = raw_input
else:
    import commander.completer as completer
    import commander.command_tree as command_tree

    input_func = input

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

class Commander:
    def __init__(self, prompt='>', intro=None):
        self.prompt = prompt
        self.intro = intro

        self.completer = completer.Completer()
        self.command_tree = command_tree.CommandTree()

    # default commands
    def do_quit(self, *args):
        return self.do_exit(args)

    def do_stop(self, *args):
        return self.do_exit(args)

    def do_exit(self, *args):
        return True

    def break_loop(self):
        self.running = False

    def handle_exit(self):
        self.break_loop()

    def handle_interrupt(self):
        pass

    def build_command_tree(self):
        methods = filter(lambda method: method.startswith('do_'), dir(self))
        commands = map(lambda method_name: (method_name[len('do_'):].split('_'), getattr(self, method_name).__get__(self, self.__class__)), methods)
        self.command_tree.build(commands)

    def enter_loop(self):
        self.build_command_tree()
        self.completer.update_callback(self.command_tree)
        self.completer.init()

        if self.intro:
            logger.info(self.intro)

        self.running = True
        while self.running:
            try:
                command = input_func(self.prompt + ' ')
                if not command:
                    continue

                full_command, handler = self.command_tree.get_command(command)
                args = command[len(full_command):].split()
                should_exit = handler(*args)
                
                if should_exit:
                    self.handle_exit()
                    break

            except (KeyboardInterrupt, EOFError):
                sys.stdout.write('\r\n')
                if self.handle_interrupt():
                    self.handle_exit()
                    break
            except command_tree.NoSuchCommandError as error:
                logger.error('Invalid command: \"{command}\"'.format(command=error.command))