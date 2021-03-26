import pandas as pd

# Pandas Tutorials: 06 Calculate Statistics

titanic = pd.read_csv("data/data3.csv")

print("\nTitanic.head():\n", titanic.head())

# How to calculate summary statistics?
# Aggregating statistics

print("\ntitanic[\"AGE\"].mean():\n", titanic["Age"].mean())

# Different statistics are available and can be applied to columns with numerical
# data. Operations in general exclude missing data and operate across rows by default.

# What is the median age and ticket fare price of the Titanic passengers?

print("\ntitanic[[\"Age\", \"Fare\"]].median():\n", titanic[["Age", "Fare"]].median())

# The statistic applied to multiple columns of a DataFrame (the selection of two columns return a DataFrame,
# see the subset data tutorial) is calculated for each numeric column.
#
# The aggregating statistic can be calculated for multiple columns at the same time.
# Remember the describe function from first tutorial tutorial?

print("\ntitanic[[\"Age\", \"Fare\"]].describe():\n", titanic[["Age", "Fare"]].describe())

# Instead of the predefined statistics, specific combinations of aggregating statistics
# for given columns can be defined using the DataFrame.agg() method:

print("\ntitanic.agg(\n{\n\"Age\": [\"min\", \"max\", \"median\", \"skew\"],\n\"Fare\": [\"min\", \"max\", \"median\", "
      "\"mean\"],\n}\n)")

print(titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
))

# Details about descriptive statistics are provided in the user guide section on descriptive statistics.

#

# Aggregating statistics grouped by category

#

# What is the average age for male versus female Titanic passengers?

print("\ntitanic[[\"Sex\", \"Age\"]].groupby(\"Sex\").mean()\n", titanic[["Sex", "Age"]].groupby("Sex").mean())

# As our interest is the average age for each gender, a subselection on these two columns is
# made first: titanic[["Sex", "Age"]]. Next, the groupby() method is applied on the Sex
# column to make a group per category. The average age for each gender is calculated and returned.
#
# Calculating a given statistic (e.g. mean age) for each category in a column
# (e.g. male/female in the Sex column) is a common pattern. The groupby method is
# used to support this type of operations. More general, this fits in the more general split-apply-combine pattern:
#
# Split the data into groups
#
# Apply a function to each group independently
#
# Combine the results into a data structure
#
# The apply and combine steps are typically done together in pandas.
#
# In the previous example, we explicitly selected the 2 columns first. If not,
# the mean method is applied to each column containing numerical columns:

print("\ntitanic.groupby(\"Sex\").mean()\n", titanic.groupby("Sex").mean())

# It does not make much sense to get the average value of the Pclass. if we are only interested in the average age for
# each gender, the selection of columns (rectangular brackets [] as usual) is supported on the grouped data as well:

print("\ntitanic.groupby(\"Sex\")[\"Age\"].mean()\n", titanic.groupby("Sex")["Age"].mean())

# What is the mean ticket fare price for each of the sex and cabin class combinations?

print("\ntitanic.groupby([\"Sex\", \"Pclass\"])[\"Fare\"].mean()\n", titanic.groupby(["Sex", "Pclass"])["Fare"].mean())

# Grouping can be done by multiple columns at the same time. Provide the column names as a list to the groupby() method.

# A full description on the split-apply-combine approach is provided in the user guide section on groupby operations.

#

# Count number of records by category¶

#

# What is the number of passengers in each of the cabin classes?

print("\ntitanic[\"Pclass\"].value_counts()\n", titanic["Pclass"].value_counts())

# The value_counts() method counts the number of records for each category in a column.
#
# The function is a shortcut, as it is actually a groupby operation
# in combination with counting of the number of records within each group:

print("\ntitanic.groupby(\"Pclass\")[\"Pclass\"].count()\n", titanic.groupby("Pclass")["Pclass"].count())

# Note
#
# Both size and count can be used in combination with groupby. Whereas size includes NaN values
# and just provides the number of rows (size of the table), count excludes the missing values. In the
# value_counts method, use the dropna argument to include or exclude the NaN values.

# The user guide has a dedicated section on value_counts , see page on discretization.

# REMEMBER
# Aggregation statistics can be calculated on entire columns or rows
#
# groupby provides the power of the split-apply-combine pattern
#
# value_counts is a convenient shortcut to count the number of entries in each category of a variable
