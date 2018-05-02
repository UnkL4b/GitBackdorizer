from colorama import Fore
from colorama import Style
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter


class GitBackdorizer(object):

    def __init__(self):
        formatters = {             
            'RED': '\033[91m',     
            'GREEN': '\033[92m',   
            'END': '\033[0m',      
         }
        self.desc_init = """
              

    ▬▬ι{RED}════════{END}  Git Backdorizer {RED}════════{END}ι▬▬

                       .-.
                      |_:_|
                     /(_Y_)\\
{RED}.{END}                   ( \/M\/ )
{RED} '.{END}               _.'-/'-'\-'._
{RED}   ':{END}          _/.--'[[[[]'--.\_
{RED}     ':{END}        /_'  : |::"| :  '.\\
{RED}       ':{END}     //   ./ |oUU| \.'  :\\
{RED}         ':{END}  _:'..' \_|___|_/ :   :|
{RED}           ':.{END}  .'  |_[___]_|  :.':\\
            [::\ |  :  | |  :   ; : \\
             '-'   \/'.| |.' \  .;.' |
             |\_    \  '-'   :       |
             |  \    \ .:    :   |   |
             |   \    | '.   :    \  |
             /       \   :. .;       |
            /     |   |  :__/     :  \\\\
           |  |   |    \:   | \   |   ||
          /    \  : :  |:   /  |__|   /|
          |     : : :_/_|  /'._\  '--|_\\
          /___.-/_|-'   \  \\
                         '-'

     "Tool based in about linux native backdoors"
                      Ulisses Castro - @usscastro
 


~> MENU

1. Generate Backdoor
2. Listening

[exit]

""".format(**formatters)


    def menu(self):
        while 1:
            user_input = prompt(':> ')
            if 'exit' == user_input:
                exit()
            else:
                print(user_input)


    def start(self):
        try:
            print(self.desc_init)
            self.menu()
        
        except KeyboardInterrupt:
            exit() 


if __name__ == '__main__':
    gb = GitBackdorizer()
    gb.start()
