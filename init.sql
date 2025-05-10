CREATE DATABASE IF NOT EXISTS carteira_digital;
CREATE USER IF NOT EXISTS 'root'@'%' IDENTIFIED BY 'testeSenhaInfinita';
GRANT ALL PRIVILEGES ON carteira_digital.* TO 'root'@'%';
FLUSH PRIVILEGES;