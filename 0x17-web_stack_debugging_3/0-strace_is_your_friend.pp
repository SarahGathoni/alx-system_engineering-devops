# Fixing 500 error for Apache WordPress .
#file:wp-settings.php

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
