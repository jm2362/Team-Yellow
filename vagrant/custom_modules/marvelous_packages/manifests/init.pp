class marvelous_packages {
    $packages = [
        "epel-release",
        "git",
        "vim-enhanced",
        "python-virtualenv",
        "python-gunicorn"
    ]
    package { $packages: 
        ensure => installed,
        allow_virtual => false
    }
}

