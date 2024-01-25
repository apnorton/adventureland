Adventureland in Rust!
===

This project is going to take a couple different approaches:
1. Starting out, it will be a wasm-compiled library that gets loaded and called by the game client (probably in a loop)
2. I'll rip out the things that interface with game code into its own crate (and possibly publish this to cargo)
3. Eventually, I'll write a game client in Rust, possibly with Bevy.