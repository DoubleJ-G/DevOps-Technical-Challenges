FROM ubuntu:20.04 as base

# Install packages without interactive prompts and recommendations

RUN apt-get update && \
		DEBIAN_FRONTEND=noninteractive \
		TZ=Australia/Sydney \
	  apt-get install -y --no-install-recommends \
		apache2 \
		php \
		php-pgsql \
		postgresql-client

# Copy entrypoint script

COPY ./entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh

# Cleanup after installation

RUN apt-get clean

# Enable pgsql php module

RUN phpenmod pgsql

# Change owner of log and data files

RUN chmod -R 775 /var/log/apache2
RUN chown -R www-data:www-data /var/log/apache2

RUN chmod -R 775 /var/www/html
RUN chown -R www-data:www-data /var/www/html

# Graceful shutdown of apache

STOPSIGNAL SIGWINCH

# Expose port and run apache

EXPOSE 80
CMD [ "usr/bin/entrypoint.sh" ]