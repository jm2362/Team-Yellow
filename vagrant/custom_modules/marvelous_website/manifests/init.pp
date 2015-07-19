class marvelous_website ($host, $git) {
    vcsrepo { "/var/www/${host}": 
        ensure   => present,
        provider => git,
        source   => $git,
        revision => "master",
        owner    => "nginx",
        group    => "nginx",
    }  

    python::requirements { "/var/www/${host}/api/requirements.py" : }
    class { 'supervisord':
        install_pip => true,
    }

    supervisord::program { 'flask-api':
        command     => 'gunicorn api:app -b 127.0.0.1:5000 --daemon -w 2',
        directory   => "/var/www/${host}/api",
    }
}
