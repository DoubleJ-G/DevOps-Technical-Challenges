FROM ubuntu:20.04 as base

# Tools for adding postgresql repository

RUN apt-get update
RUN apt-get install -y wget gnupg2 lsb-release

# Add postgresql repository

RUN echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

# Install specific postgresql-14 version without interactive prompts and recommendations

RUN apt-get update
RUN apt-get update && \
		DEBIAN_FRONTEND=noninteractive \
		TZ=Australia/Sydney \
	  apt-get install -y --no-install-recommends \
		postgresql-14

# Cleanup after installation

RUN apt-get clean

# Create files for postgresql configuration

RUN mkdir /usr/local/pgsql && mkdir /usr/local/pgsql/data
RUN chmod -R 775 /usr/local/pgsql
RUN chown -R postgres:postgres /usr/local/pgsql

RUN echo "host all  all 0.0.0.0/0  md5" >> /etc/postgresql/14/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/14/main/postgresql.conf

# Switch to a less privileged user

USER postgres

# Create user and a database

RUN /etc/init.d/postgresql start &&\
    psql --command "CREATE USER iriusprod WITH SUPERUSER PASSWORD 'iriusprod';" &&\
    createdb -O iriusprod iriusprod

# Check database is ready to accept connections

HEALTHCHECK --interval=10s --timeout=5s --start-period=5s --retries=5 CMD [ "pg_isready" ]

# Expose port and run postgres

EXPOSE 5432

CMD [ "/usr/lib/postgresql/14/bin/postgres", "-D", "/usr/local/pgsql/data",  "-c", "config_file=/etc/postgresql/14/main/postgresql.conf" ]
