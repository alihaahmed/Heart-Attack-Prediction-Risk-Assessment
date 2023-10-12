from pyspark.sql.types import StructType, StructField, StringType, DateType, IntegerType
from pyspark.sql import Row
from pyspark.sql import SparkSession
from flask import Flask
import findspark

# Create a SparkSession
findspark.init()
spark = SparkSession.builder.appName("heart-risk-analysis").getOrCreate()
df = spark.read.csv(('Resources/heart_clean_df.csv'),
                    header=True, inferSchema=True)
df.createOrReplaceTempView('heart')


# Create Flask app

app = Flask(__name__)

@app.route("/")
def welcome():
  return "Hello Spark API"

@app.route("/total-gender")
def total_gender():
  s = spark.sql("""
      SELECT Sex,
      Count (Sex) as Number_of_Patients
      FROM heart
      GROUP BY Sex
      """).toJSON().collect()
  
  return s


@app.route("/risk-gender")
def risk_gender():
  s = spark.sql("""
        SELECT Sex,
        Count (Sex) as Number_of_Patients
        FROM heart
        WHERE Heart_Attack_Risk = 1
        GROUP BY Sex
        """).toJSON().collect()
  
  return s

@app.route("/risk-old-age")
def risk_old_age():
  s = spark.sql("""
        SELECT Sex,
        Count (Sex) as Older_Than_50
        FROM heart
        WHERE Age > 50 and Heart_Attack_Risk = 1
        GROUP BY Sex
        """).toJSON().collect()
  
  return s

@app.route("/risk-history-old-age")
def risk_history_old_age():
  s = spark.sql("""
        SELECT Sex,
        Count (Sex) as Older_Than_50
        FROM heart
        WHERE Age > 50 and Previous_Heart_Problems =1 and Heart_Attack_Risk = 1
        GROUP BY Sex
        """).toJSON().collect()
  
  return s

@app.route("/risk-history-young-age")
def risk_history_young_age():
  s = spark.sql("""
        SELECT Sex,
        COUNT (Sex) as Yonger_Then_30
        FROM heart
        WHERE Age < 30 and Previous_Heart_Problems =1 and Heart_Attack_Risk = 1
        GROUP BY Sex
        """).toJSON().collect()
  
  return s

@app.route("/risk-young-age")
def risk_young_age():
  s = spark.sql("""
        SELECT Sex,
        COUNT (Sex) as Yonger_Then_30
        FROM heart
        WHERE Age < 30 and Heart_Attack_Risk = 1
        GROUP BY Sex
        """).toJSON().collect()
  
  return s

@app.route("/risk-avg-income")
def risk_avg_income():
  s = spark.sql("""
        SELECT Heart_Attack_Risk,
        AVG(Income) as Avg_Income
        FROM heart
        GROUP BY Heart_Attack_Risk
        """).toJSON().collect()
  
  return s

@app.route("/risk-by-country")
def risk_by_country():
  s = spark.sql("""
        SELECT Country,
        COUNT(Country) as Number_of_Patients
        FROM heart
        GROUP BY Country
        """).toJSON().collect()
  
  return s

@app.route("/risk-all")
def risk_all():
  s = spark.sql("""
        SELECT Heart_Attack_Risk,
        COUNT(Heart_Attack_Risk) as Number_of_Patients
        FROM heart
        WHERE Diabetes =1 and Family_History =1 and Smoking =1 and Obesity =1 and Alcohol_Consumption =1
        GROUP BY Heart_Attack_Risk
        """).toJSON().collect()
  
  return s

@app.route("/risk-avg-sleep")
def risk_avg_sleep():
  s = spark.sql("""
        SELECT Heart_Attack_Risk,
        AVG(Sleep_Hours_Per_Day) as Avg_Sleeping_Time_Per_Day
        FROM heart
        GROUP BY Heart_Attack_Risk
        """).toJSON().collect()
  
  return s

@app.route("/risk-lifestyle")
def risk_lifestyle():
  s = spark.sql("""
        SELECT Diet,
        AVG(Exercise_Hours_Per_Week) as Avg_Exercise_Hours_Per_Week
        FROM heart
        WHERE Heart_Attack_Risk = 1
        GROUP BY Diet
        """).toJSON().collect()
  
  return s

@app.route("/risk-avg-exercise")
def risk_avg_exercise():
  s = spark.sql("""
        SELECT Diet,
        AVG(Exercise_Hours_Per_Week) as Avg_Exercise_Hours_Per_Week
        FROM heart
        WHERE Heart_Attack_Risk = 0
        GROUP BY Diet
        """).toJSON().collect()
  
  return s

if __name__ == '__main__':
    app.run(debug=True)