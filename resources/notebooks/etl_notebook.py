# Databricks notebook source
# Simple ETL Example
df = spark.range(0, 100)
df = df.withColumn("squared", df["id"] * df["id"])
display(df)
