import readline

class Completer:
    
    def init(self):
        readline.parse_and_bind('tab: complete')

    def update_callback(self, command_table):
        matches = []
        def callback(text, state):
            line = readline.get_line_buffer()
            begin = readline.get_begidx()
            words = line.split()

            if not words:
                matches = command_table.get_possible_postfix('') # empty string for all options
            else:
                matches = list(map(lambda match: match[begin:], command_table.get_possible_postfix(line)))

            try:
                return matches[state]
            except IndexError:
                return None
            except Exception as e:
                print(e)

        readline.set_completer(callback)