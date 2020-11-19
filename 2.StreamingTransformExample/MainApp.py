from pyspark.streaming import *
from pyspark import *


sc = SparkContext(AppName = 'StreamingTransformExample')
ssc = StreamingContext( sc, batchDuration=1)


#create a dataframe
