import commander
import logging

class BasicCLI(commander.Commander):
    def do_foo(self, *args):
        print('doing foo!')

    def do_foo_bar(self, *args):
        print('doing foo::bar!')

    def do_foo_baz(self, *args):
        print('doing foo:baz!')
    
    def do_foo_qux(self, *args):
        print('doing foo::qux!')

    def handle_interrupt(self):
        print('did you try to interrupt me?')

if __name__ == '__main__':
    commander.logger.handlers[0].setFormatter(logging.Formatter('%(asctime)s [%(levelname)-5.5s] %(message)s'))
    cli = BasicCLI(prompt='~>', intro='Hello World!')
    cli.enter_loop()