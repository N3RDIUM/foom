# `foom`
A curses-based mpd client.

## Capabilities
- [ ] Search for music on YouTube
- [ ] Download music from YouTube
- [ ] Parallely download multiple songs
- [ ] Create and manage playlists
- [ ] Play music
- [ ] Visualize music
- [ ] FULL Mpris integration

## Roadmap
- [ ] Search and download util
- [ ] Player
- [ ] Mpris integration
- [ ] Visualizer (w/ cover art display in visualizer and player screens)
- [ ] Plugin support
- [ ] Isolate the UI, mpris integration into separate pkgs/repos?

## Requirements
Make sure `mpd` is properly installed, set up and running.

## Usage
Install the [Nix](https://nixos.org/) Package Manager:
```bash
$ sh <(curl --proto '=https' --tlsv1.2 -L https://nixos.org/nix/install) --daemon
```

Clone this repo and `cd` into it:
```bash
git clone https://n3rdium/foom.git
cd foom
```

Enter nix shell (this will "install" all deps for you):
```bash
nix-shell
```

Now, to start foom, run:
```bash
python src/main.py
```

## Screenshots
Coming soon!

## Contributing
Coming soon!
