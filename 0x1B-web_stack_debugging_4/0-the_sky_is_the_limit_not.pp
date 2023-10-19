# fix stack

exec { 'fix':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

# restarting nginx server
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
