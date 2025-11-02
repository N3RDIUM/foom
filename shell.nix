let pkgs = import <nixpkgs> { };
in pkgs.mkShell {
    packages = with pkgs; [
        python312
        python312Packages.mpd2
        python312Packages.ytmusicapi
    ];
    buildInputs = [  ];
}
