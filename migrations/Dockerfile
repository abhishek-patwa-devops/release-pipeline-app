FROM flyway/flyway:13.12.2

# We only migrate PostgreSQL. Remove the unused drivers that carry HIGH CVEs
# (Databricks, Couchbase, SQL Server, GCP) together with the Flyway plugins that load them.
RUN rm -rf /flyway/drivers/databricks-jdbc-*.jar \
           /flyway/drivers/couchbase \
           /flyway/drivers/mssql-jdbc-*.jar \
           /flyway/drivers/gcp \
           /flyway/lib/flyway/flyway-database-databricks-*.jar \
           /flyway/lib/flyway/flyway-database-nc-couchbase-*.jar \
           /flyway/lib/flyway/flyway-sqlserver-*.jar \
           /flyway/lib/flyway/flyway-gcp-*.jar

COPY *.sql /flyway/sql/
