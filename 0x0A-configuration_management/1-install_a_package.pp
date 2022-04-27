# Install flask 2.1.0 using pip3

exec {'apt-update':
  command  => '/usr/bin/apt-get update',
}

package {'python3-pip':
  ensure  => installed,
  require => Exec['apt-update'],
}

package {'flask':
  ensure   => '2.1.0',
  provider => pip3,
  require  => Package['python3-pip'],
}
