node default {
    include redis

    stage { 'repos': }
    stage { 'marv_nginx': }

    class { 'marvelous_packages': stage => 'repos' }

    class { 'marvelous_nginx': host => $host }

    class { 'marvelous_website': 
        host => $host,
        git  => $git
    }

    Stage['repos'] -> Stage['main']
}

