# Install flask@2.1.0 from pip3

package { 'pip3':
    ensure => 'installed',
}

package { 'flask==2.1.0':
    require  => Package['pip3'],
    provider => 'pip3'
}
