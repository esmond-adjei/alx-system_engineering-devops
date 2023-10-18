# Replace "phpp" with "php" in wp-settings.php
exec { 'modify_wp_settings':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/'
}