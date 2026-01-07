let pkgs = import <nixpkgs> { };
in pkgs.mkShell {
    packages = with pkgs; [
        python313
        python313Packages.mpd2
        python313Packages.ytmusicapi
    ];
    buildInputs = [  ];
}
