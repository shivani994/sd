#Write a Python Programme to apply Apriori algorithm on Groceries dataset.
#Dataset can be downloaded from
#(https://github.com/amankharwal/Websitedata/blob/master/Groceries_dataset.csv)
#Also display support and confidence for each rule.

{
"cells": [
{
"cell_type": "markdown",
"id": "6df9f70d",
"metadata": {
"id": "6df9f70d"
},
"source": [
"# SET - A\n",
"\n",
"### 2) Write a code to read the dataset (“Groceries.csv”) dataset download from(https://github.com/amankharwal/Website-
{
"cells": [
{
"cell_type": "markdown",
"id": "6df9f70d",
"metadata": {
"id": "6df9f70d"
},
"source": [
"# SET - A\n",
"\n",
"### 2) Write a code to read the dataset (“Groceries.csv”) dataset download from
(https://github.com/amankharwal/Website{
"cells": [
{
"cell_type": "markdown",
"id": "6df9f70d",
"metadata": {
"id": "6df9f70d"
},
"source": [
"# SET - A\n",
"\n",
"### 2) Write a code to read the dataset (“Groceries.csv”) dataset download from
(https://github.com/amankharwal/Website-{
"cells": [
{
"cell_type": "markdown",
"id": "6df9f70d",
"metadata": {
"id": "6df9f70d"
},
"source": [
"# SET - A\n",
"\n",
### 2) Write a code to read the dataset (“Groceries_data.csv”) dataset download from(https://github.com/amankharwal/Website-data/blob/master/Groceries_dataset.csv) and apply Apriori algorithm also displaysupport and confidence for each rule."
]
},
{
"cell_type": "code",
"execution_count": null,
"id": "56e6340c",
"metadata": {
"id": "56e6340c"
},
"outputs": [],
"source": [
"import numpy as np\n",
"import matplotlib.pyplot as plt\n",
"import pandas as pd\n",
"from apyori import apriori"
]
},
{
"cell_type": "code",
"execution_count": null,
"id": "7091c7cf",
"metadata": {
"id": "7091c7cf"
},
"outputs": [],
"source": [
"store_data=pd.read_csv('Groceries_dataset.csv',header=None)"
]
},
{
"cell_type": "code",
"execution_count": null,
"id": "0beac933",
"metadata": {
"id": "0beac933"
},
"outputs": [],
"source": [
"association_rules=apriori(records,min_support=0.0045,min_confidence=0.2,min_lift
=3,min_length=2)\n",
"association_results=list(association_rules)\n"
]
},
{
"cell_type": "code",
"execution_count": null,
"id": "e4d1fd53",
"metadata": {
"id": "e4d1fd53"
},
"outputs": [],
"source": [
"print(len(association_results))\n"
]
},
{
"cell_type": "code",
"execution_count": null,
"id": "55580074",
"metadata": {
"id": "55580074"
},
"outputs": [],
"source": [
"print(association_results[0])\n"
]
},
{
"cell_type": "code",
"id": "80937225",
"metadata": {
"id": "80937225"
},
"outputs": [],
"source": [
"for item in association_results:\n",
" pair = item[0]\n",
" items = [x for x in pair]\n",
" print(\"Rule:\"+items[0]+\"->\"+items[1])\n",
" \n",
" print(\"Support:\"+str(item[1]))\n",
"\n",
" print(\"Confidence:\"+str(item[2][0][2]))\n",
" print(\"Lift:\"+str(item[2][0][3]))\n",
" print(\"========================================\")"
]
}
],
"metadata":{
"kernelspec": {
"display_name": "Python 3 (ipykernel)",
"language": "python",
"name": "python3"
},
"language_info": {
"codemirror_mode": {
"name": "ipython",
"version": 3
},
"file_extension": ".py",
"mimetype": "text/x-python",
"name": "python",
"nbconvert_exporter": "python",
"pygments_lexer": "ipython3",
"version": "3.7.9"
},
"colab": {
"name": "Data Mining Assignment-3.ipynb",
"provenance": []
}
},
"nbformat": 4,
"nbformat_minor": 5
}
    ``