exec {'apt-get update':
  command => '/usr/bin/apt-get update',
}

#make sure apache is not installed
package {'apache2.2-common':
  ensure => absent,
}

package {'nginx':
  ensure  => installed,
  require => [Package['apache2.2-common'],Exec['apt-get update']],
}

file {'/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file_line {'redirect and return 301':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server',
  line   => "\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;",
}

service {'nginx':
  ensure  => running,
  require => Package['nginx'],
}


