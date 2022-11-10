# Install flask@2.1.0 from pip3

package { 'pip3':
    ensure => 'installed',
    name   => 'python3-pip'
}

package { 'flask':
    require  => Package['pip3'],
    provider => 'pip3',
    name     => 'flask==2.1.0'
}
