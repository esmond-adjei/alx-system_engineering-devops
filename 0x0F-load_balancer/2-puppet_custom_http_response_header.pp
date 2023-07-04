# Puppet manifest to configure a custom HTTP header in Nginx using Puppet.
#
# Requirements:
# - The name of the custom HTTP header must be X-Served-By.
# - The value of the custom HTTP header must be the hostname of the server Nginx is running on.
#
# Usage:
# Apply this Puppet manifest to a brand new Ubuntu machine to configure Nginx with the custom HTTP header.
#
# Example:
#   puppet apply 2-puppet_custom_http_response_header.pp


# Update the package manager repositories
exec { 'apt-update':
  command => '/usr/bin/apt update',
}

# Install Nginx package
package { 'nginx':
    ensure  => present,
    require => Exec['apt-update'],
}

# Add custom HTTP header directive to Nginx configuration
file_line {'Adding_Header':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'listen 80 default_server;',
    line    => 'add_header X-Served-By $hostname;',
    require => Package['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
}
