# Increase the ULIMIT of the default file
exec { 'fix':
  path    => ['/bin/'],
  command => 'sed -i "s/-n 15/-n 1000/" /etc/default/nginx',
  notify => Service['nginx']
}

service { 'nginx':
  ensure => running,
  enable => true
}
