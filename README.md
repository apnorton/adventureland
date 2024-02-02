Adventureland in Rust!
===

This project is going to take a couple different approaches:
1. Starting out, it will be a wasm-compiled library that gets loaded and called by the game client (probably in a loop)
2. I'll rip out the things that interface with game code into its own crate (and possibly publish this to cargo)
3. Eventually, I'll write a game client in Rust, possibly with Bevy.

Wasm + Adventureland
---

https://stackoverflow.com/questions/70420273/how-can-i-make-webpack-embed-my-wasm-for-use-in-a-web-worker 

To build with the new packaging script:
```
$ python build_and_package.py gaussian-bots
```
...and then copy/paste the js from `bot_code.js`.

If you don't have the virtual environment set up yet:
```
$ python -m venv .venv
$ python -m pip install -f requirements.txt
```