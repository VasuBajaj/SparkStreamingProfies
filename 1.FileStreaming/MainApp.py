from pyspark import SparkContext
from pyspark.streaming import StreamingContext


sc = SparkContext(appName = 'FileStreaming')
ssc = StreamingContext(sc, batch_duration = 1)

stream = ssc.QueueStream([sc.parallelize(list(range(1,1000)),3)])

data =  stream.map(lambda x: (x, x%10)).countByValue(lambda x,y = x+y)
data.pprint()

ssc.start()
ssc.awaitTermination()
ssc.stop(stopSparkContext = True, stopGracefully = True)
