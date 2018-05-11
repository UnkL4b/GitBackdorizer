import random

formatters = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'END': '\033[0m',
 }


ban_1 = """
              
                      UnkL4b
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

          "Há mais perigo em teus commits 
             do que em vinte exploits!"
     

Tool based in "50 ton of backdoors" by Ulisses Castro
- https://www.slideshare.net/ulissescastro/50-ton-of-backdoors

""".format(**formatters)

ban_2 = """
                      UnkL4b
    ▬▬ι{GREEN}════════{END}  Git Backdorizer {GREEN}════════{END}ι▬▬

         {GREEN}          ____
                 _.' :  `._
             .-.'`.  ;   .'`.-.
    __      / : ___\ ;  /___ ; \      __
  ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
  :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
       `:-.._J '-.-'L__ `-- ' L_..-;'
         "-.__ ;  .-"  "-.  : __.-"
             L ' /.------.\ ' J
              "-.   "--"   .-"{END}
             __{GREEN}.l"-:_JL_;-";.{END}__
          .-j/'.;  ;""\"\"  / .'\\"-.
        .' /:`. "-.:     .-" .';  `.
     .-"  / ;  "-. "-..-" .-"  :    "-.
  .+"-.  : :      "-.__.-"      ;-._   \\
  ; \  `.; ;                    : : "+. ;
  :  ;   ; ;                    : ;  : \:
 : `."-; ;  ;                  :  ;   ,/;
  ;    -: ;  :                ;  : .-"'  :
  :\     \  : ;             : \.-"      :
   ;`.    \  ; :            ;.'_..--  / ;
   :  "-.  "-:  ;          :/."      .'  :
     \       .-`.\        /t-""  ":-+.   :
      `.  .-"    `l    __/ /`. :  ; ; \  ;
        \   .-" .-"-.-"  .' .'j \  /   ;/
         \ / .-"   /.     .'.' ;_:'    ;
          :-""-.`./-.'     /    `.___.'
                \ `t  ._  /  
                 "-.t-._:'


Tool based in "50 ton of backdoors" by Ulisses Castro
- https://www.slideshare.net/ulissescastro/50-ton-of-backdoors

""".format(**formatters)

def banner():
    banners = [ban_1, ban_2]
    return(random.choice(banners))
