from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 redshift_conn_id='',
                 table_names='',
                 *args, **kwargs):
        """
        - Defines your operators params (with defaults)
        - Maps params to values
        """

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id = redshift_conn_id
        self.table_names = table_names

    def execute(self, context):
        """
        - Checks tables for zero values and zero records
        - Checks tables for zero rows
        """
        self.log.info('Performing data quality checks of all tables')
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)

        # Perform 'zero values' and 'zero records' quality check on all tables 
        for table in self.table_names:
            records = redshift.get_records(f"SELECT COUNT(*) FROM {table}")
            
            if len(records) < 1 or len(records[0]) < 1:
                raise ValueError("Failed data quality check, as %s table has no values" % table)

            num_records = records[0][0]
            if num_records < 1:
                raise ValueError("Failed data quality check, as %s table has no rows" % table)
                
            self.log.info("Completed data quality check successfully for %s table" % table)