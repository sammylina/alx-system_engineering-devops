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

file_line {'add custom header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server',
  line   => "add_header X-Served-By $host;",
  require => Package['nginx'],
}

service {'nginx':
  ensure  => running,
  require => Package['nginx'],
}


