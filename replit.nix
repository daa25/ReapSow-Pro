{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.firebase-admin
    pkgs.python311Packages.requests
    pkgs.python311Packages.python-dotenv
  ];
}