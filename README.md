# inve
Virtualenv activator that you don't source, it just execs its argv (or $SHELL)

Inspired by some blogpost (or was it a github gist?) that explained why `bin/activate` is wrong that I've seen years ago and lost the link to it.
If you're the author of that post, please reach out so that I can give you a credit.

## Installing

idk, what I did is:

```sh
pip install --user --break-system-packages .
```

but you do you

## Using

Don't source it, just run it like you would run `sudo` or `ssh`

## How do I deactivate?

Ctrl+D, or just `exit`, just like you would exit `sudo` or `ssh`

## It doesn't show venv name in the prompt

Yeah, it assumes you are in charge of your prompt and doesn't want to mess it up.

Try adding sth like this to `.bashrc`:

```bash
function ps1_context {
  virtualenv=`basename "$VIRTUAL_ENV"`
  for v in "$virtualenv"; do
    echo -n "${v:+$v }"
  done
}

PS1="\$(ps1_context) $PS1"
```

or if you already have a custom PS1, you can put it in there, wrap it in your favourite colors, etc.
