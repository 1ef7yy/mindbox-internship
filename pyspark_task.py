# В датафреймах (pyspark.sql.DataFrame) заданы продукты, категории и связь
# между ними. Одному продукту может соответствовать много категорий,
# в одной категории может быть много продуктов. Напишите метод с помощью
# PySpark, который вернет все продукты с их категориями (датафрейм с
# набором всех пар «Имя продукта – Имя категории»). В результирующем
# датафрейме должны также присутствовать продукты, у которых нет категорий.

from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("dataframes_task").config("spark.memory.offHeap.enabled","true").config("spark.memory.offHeap.size","8g").getOrCreate()
spark.sparkContext.setLogLevel("FATAL")

category_df = spark.createDataFrame([
    (1, "category 1"),
    (2, "category 2"),
    (3, "category 3"),
    (4, "category 4"),
    (5, "category 5"),
    (6, "category 6"),],
    ["id", "category"],
)

product_df = spark.createDataFrame([
    (1, "product 1"),
    (2, "product 2"),
    (3, "product 3"),
    (4, "product 4"),
    (5, "product 5"),
    (6, "product 6"),
    (7, "product 7"),
    (8, "product 8"),
    (9, "product 9"),
    (10, "product 10"), 
    (11, "product 11"), 
    (12, "product 12"), 
    (13, "product 13"), 
    (14, "product 14"), 
    (15, "product 15"), 
    ],
    ["id", "product"]
)


pairing_df = spark.createDataFrame([
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (6, 3),
    (7, 3),
    (10, 4),
    (11, 5),
    (13, 5),
    (15, 6),
    ],
    ["product_id", "category_id"]
)




df_data = (product_df.join(pairing_df, product_df.id == pairing_df.product_id, how='left'))
df_data= df_data.join(category_df, pairing_df.category_id == category_df.id, how='left')
df_data = df_data.select(['category', 'product'])

df_data.show(truncate=False)

