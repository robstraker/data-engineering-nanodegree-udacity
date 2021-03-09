from airflow.hooks.postgres_hook import PostgresHook
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'
    
    staging_events_copy = """
                  COPY {table_name}
                  FROM '{s3_link}'
                  ACCESS_KEY_ID '{key_id}'
                  SECRET_ACCESS_KEY '{secret_id}'
                  JSON 's3://udacity-dend/log_json_path.json';
    """
    
    staging_songs_copy = """
                  COPY {table_name}
                  FROM '{s3_link}'
                  ACCESS_KEY_ID '{key_id}'
                  SECRET_ACCESS_KEY '{secret_id}'
                  JSON 'auto';
    """   
    
    
    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 redshift_conn_id = '',
                 aws_credentials_id = '',
                 s3_bucket = '',
                 s3_key = '',
                 table_name = '',
                 *args, **kwargs):
        """
        - Defines your operators params (with defaults)
        - Maps params to values
        """
         
        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id = redshift_conn_id
        self.aws_credentials_id = aws_credentials_id
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.table_name = table_name
             
    def execute(self, context):
        """
        - Copies data from S3 to staging tables on Redshift
        """
        aws_hook = AwsHook(self.aws_credentials_id)
        credentials = aws_hook.get_credentials()
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        # Copy data from S3 to Redshift
        self.log.info('Copying data from S3 to Redshift %s table' % self.table_name)
        redshift.run("DELETE FROM {}".format(self.table_name))
        s3_path='s3://{}/{}'.format(self.s3_bucket, self.s3_key.format(**context))
        
        if self.table_name == 'staging_events':
            copy_table = StageToRedshiftOperator.staging_events_copy.format(
                            table_name=self.table_name,
                            s3_link=s3_path,
                            key_id=credentials.access_key,
                            secret_id=credentials.secret_key
            )
            redshift.run(copy_table)        
        else:
            copy_table = StageToRedshiftOperator.staging_songs_copy.format(
                            table_name=self.table_name,
                            s3_link=s3_path,
                            key_id=credentials.access_key,
                            secret_id=credentials.secret_key
            )
            redshift.run(copy_table)
        
        self.log.info('Completed copying data from S3 to Redshift %s table' % self.table_name)