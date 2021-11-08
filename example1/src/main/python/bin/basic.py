from pyspark.sql import SparkSession

spark = SparkSession \
.builder \
.master('yarn') \
.appName("Python Spark SQL basic example") \
.getOrCreate()

print('*' * 10)
print("Spark Object Created Successfully")
print('==' * 10)
spark.stop()

