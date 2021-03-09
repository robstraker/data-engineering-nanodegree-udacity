from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 redshift_conn_id='',
                 table_name = '',
                 sql_query = '',
                 insert_data = '',
                 *args, **kwargs):
        """
        - Defines your operators params (with defaults)
        - Maps params to values
        """

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id = redshift_conn_id
        self.table_name = table_name
        self.sql_query = sql_query
        self.insert_data = insert_data

    def execute(self, context):
        """
        - Loads Fact table from Redshift
        - Appends or deletes-inserts data from Staging tables
        """
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        # Load Fact table from Redshift
        self.log.info('Loading Fact table %s from Redshift' % self.table_name)
            
        if self.insert_data == True:
            sql_insert = 'INSERT INTO %s %s' % (self.table_name, self.sql_query)
            redshift.run(sql_insert)
        else:
            sql_delete = 'DELETE FROM %s' % self.table_name
            redshift.run(sql_delete)
            sql_insert = 'INSERT INTO %s %s' % (self.table_name, self.sql_query)
            redshift.run(sql_insert)          
            
        self.log.info('Finished loading Fact table %s' % self.table_name)
