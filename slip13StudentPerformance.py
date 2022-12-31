#ass4setbq1 slip13q2
#1)Write a Python program to read “StudentsPerformance.csv” file. Solve following:
#- To display the shape of dataset.
#- To display the top rows of the dataset with their columns.
#- To display the number of rows randomly.
#- To display the number of columns and names of the columns.
#Note: Download dataset from following link :
#(https://www.kaggle.com/spscientist/students-performance-inexams?
#select=StudentsPerformance.csv)

{
"nbformat": 4,
"nbformat_minor": 0,
"metadata": {
"colab": {
"name": "Data Mining Assignment-3 SET-B-1.ipynb",
"provenance": []
},
"kernelspec": {
"name": "python3",
"display_name": "Python 3"
},
"language_info": {
"name": "python"
}
},
"cells": [
{
"cell_type": "markdown",
"source": [
"### SET-B\n",
"\n",
"1) Write a Python program to read \"StudentsPerformance.csv\" file. solve the following :\n",
"- To display the shape of dataset.\n",
"- To display the top rows of the dataset with their columns.\n",
"- To display the number of rows randomly.\n",
"- To display the number of columns and names of the columns.\n",
"- Note : Download dataset from following link:\n",
"(https://www.kaggle.com/spscientist/students-performance-inexams?select=StudentsPerformance.csv)"
],
"metadata": {
"id": "0hhW5uEs_wK2"
}
},
{
"cell_type": "code",
"source": [
"# Import required libraries\n",
"import numpy as np\n",
"import matplotlib.pyplot as plt\n",
"import pandas as pd\n"
],
"metadata": {
"id": "W61H7Yo7E_sP"
},
"execution_count": 2,
"outputs": []
},
{
"cell_type": "code",
"source": [
"# Read the downloaded dataset\n",
"store_data=pd.read_csv('StudentsPerformance.csv',header=None)"
],
"metadata": {
"id": "uC2jGgIFFVa3"
},
"execution_count": None,
"outputs":[]
},
{
"cell_type": "code",
"source": [
"# To display the shape of dataset. (By Using shape method)\n",
"store_data.shape"
],
"metadata": {
"id": "wU6-JdtCF3ar"
},
"execution_count": None,
"outputs": []
},
{
"cell_type": "code",
"source": [
"# To display the top rows of the dataset with their columns.(By using head method\n",
"store_data.head()"
],
"metadata": {
"id": "xHtDSrSsGT2v"
},
"execution_count": None,
"outputs": []
},
{
"cell_type": "code",
"source": [
#To display the number of rows randomly.(By using sample method)\n",

"store_data.sample(10)"
],
"metadata": {
"id": "2Gwsi4oTG9QN"
},
"execution_count": None,
"outputs": []
},
{
"cell_type": "code",
"source": [
# To display the number of columns and names of the columns. (By using columnsmethod)\n",

"store_data.columns()"
],
"metadata": {
"id": "ZdXc3aoUHO80"
},
"execution_count": None,
"outputs": []
}
]
}