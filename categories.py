from pyspark.sql import SparkSession as ss

sp_work = ss.builder.appName("category").getOrCreate()
products_table = sp_work.createDataFrame([
    (1, "ID1"),(2, "ID2"),(3, "ID3"),(4, "ID4"),(5, "ID5"),],
    ["id", "product_name", ]
)
categories_table = sp_work.createDataFrame([
    (1, "CTG1"),(2, "CTG2"),(3, "CTG3"),(4, "CTG4"),(5, "CTG5"),],
    ["id", "category_name"],
)




ER_table_products_vs_categories = sp_work.createDataFrame([
    (3, 1),(5, 2),(1, 3),(2, 4),],
    ["category_id", "product_id", ]
)

df_data = (products_table.join(ER_table_products_vs_categories,
    products_table.id == ER_table_products_vs_categories.product_id, how='left')
    .join(categories_table,
    ER_table_products_vs_categories.category_id == categories_table.id, how='left')
    .select(['category_name', 'product_name'])
)

df_data.orderBy("category_id", "product_id", ).show(truncate=True)