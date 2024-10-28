# inve

Virtualenv activator that you don't source, it just execs its argv (or $SHELL)

Inspired by [this excellent gist by datagrok][datagrok-gist] that explained why `bin/activate` is wrong.

## Installing

idk, what I did is:

```sh
pip install --user --break-system-packages .
```

but you do you

## Using

Don't source it, just run it like you would run `sudo` or `ssh`

To deactivate, use Ctrl+D, or just `exit`, just like you would exit `sudo` or `ssh`


```console
$ virtualenv3 my-venv
$ my-venv/bin/inve
$ which python
.../my-venv/bin/python
$ exit
$ which python
/usr/bin/python
```

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

[datagrok-gist]: https://gist.github.com/datagrok/2199506/8f7d99fb92a3f68eba8172182eb835e24777e853
