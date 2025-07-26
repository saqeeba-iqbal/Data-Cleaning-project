# Netflix Data Cleaning Project
This repository contains a Python script for cleaning and preprocessing the Netflix Movies and TV Shows dataset. The goal of this project is to demonstrate fundamental data cleaning techniques, including handling missing values, removing duplicates, and standardizing data formats, to prepare the dataset for further analysis or machine learning tasks.

## Project Overview
Data cleaning is a crucial step in any data analysis or machine learning pipeline. This project focuses on transforming raw, messy data into a clean, usable format. The clean_netflix_data.py script automates several common data cleaning tasks, making the Netflix dataset more reliable for insights and model building.

## Dataset
The dataset used in this project is netflix1.csv, which contains information about movies and TV shows available on Netflix.

## Features
The cleaningAnalysis.py script performs the following data cleaning operations:

Missing Value Handling:

Fills missing director and country values with 'Not Given'.

Removes rows where date_added or duration are missing.

Fills missing rating values with the most frequent rating.

Duplicate Removal:

Identifies and removes duplicate rows to ensure data uniqueness.

Data Standardization:

Converts date_added to a proper datetime format.

Extracts numerical duration into two new columns: duration_minutes (for movies) and duration_seasons (for TV shows).

Converts release_year to an integer type.

Standardizes the listed_in (genres) column by splitting and stripping whitespace, converting it into a list of strings.

Outlier Discussion (Conceptual):

Includes a conceptual discussion on how to approach outlier detection for numerical fields like release_year and duration.

## Importance Cleaning Data
1 Ensures Data Reliability: It fixes incorrect, corrupted, or incomplete data, making the dataset trustworthy.

2 Enables Accurate Analysis: Clean data leads to more accurate and meaningful insights from your analysis.

3 Improves Model Performance: Machine learning models perform much better and provide more reliable predictions when trained on clean, well-prepared data. Messy data can lead to skewed results and poor model performance.

4 Facilitates Further Steps: It prepares the data for subsequent steps in the data pipeline, such as exploratory data analysis, visualization, and machine learning model training.
