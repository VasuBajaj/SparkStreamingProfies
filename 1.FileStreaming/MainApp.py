from pyspark import SparkContext
from pyspark.streaming import StreamingContext


sc = SparkContext(appName = 'FileStreaming')
ssc = StreamingContext(sc, batchDuration = 1)

stream = ssc.queueStream([sc.parallelize(list(range(1,1000)),3)])

data =  stream.map(lambda x: (x%10)).countByValue()
data.pprint()

ssc.start()
#ssc.awaitTermination()
ssc.stop(stopSparkContext = True, stopGraceFully = True)
