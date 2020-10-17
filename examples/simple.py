import commander

class BasicCLI(commander.Commander):
    def do_foo(self, *args):
        print('doing foo!')

    def do_foo_bar(self, *args):
        print('doing foo::bar!')

    def do_foo_baz(self, *args):
        print('doing foo:baz!')
    
    def do_foo_qux(self, *args):
        print('doing foo::qux!')

    
if __name__ == '__main__':
    cli = BasicCLI(prompt='~>', intro='Hello World!')
    cli.enter_loop()