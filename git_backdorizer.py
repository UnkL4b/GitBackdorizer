from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter


class GitBackdorizer(object):

    def __init__(self):
        self.desc_init = """

                              . .  ,  , 
                              |` \/ \/ \,', 
                              ;          ` \/\,. 
                             :               ` \,/ 
                             |                  / 
                             ;                 : 
                            :                  ; 
                            |      ,---.      / 
                           :     ,'     `,-._ \ 
                           ;    (   o    \   `' 
                         _:      .      ,'  o ; 
                        /,.`      `.__,'`-.__, 
                        \_  _               \ 
                       ,'  / `,          `.,' 
                 ___,'`-._ \_/ `,._        ; 
              __;_,'      `-.`-'./ `--.____) 
           ,-'           _,--\^-' 
         ,:_____      ,-'     \ 
        (,'     `--.  \;-._    ;              Git Backdorizer v1.0 
        :    Y      `-/    `,  :     "Tool based in about linux native backdoors"
        :    :       :     /_;'       By Ulisses Castro - @usscastro
        :    :       |    :            
         \    \      :    : 
          `-._ `-.__, \    `. 
             \   \  `. \     `. 
           ,-;    \---)_\ ,','/ 
           \_ `---'--'" ,'^-;' 
           (_`     ---'" ,-') 
           / `--.__,. ,-'    \ 
           )-.__,-- ||___,--' `-. 
          /._______,|__________,'\ 
          `--.____,'|_________,-' 


~> MENU

[1]

"""

    def start(self):
        try:
            print(self.desc_init)
            while 1:
                html_completer = WordCompleter(['<html>', '<body>', '<head>', '<title>'])
                user_input = prompt(':> ', completer=html_completer)
                if 'exit' == user_input:
                    exit()
                else:
                    print(user_input)
        
        except KeyboardInterrupt:
            exit() 


if __name__ == '__main__':
    gb = GitBackdorizer()
    gb.start()
