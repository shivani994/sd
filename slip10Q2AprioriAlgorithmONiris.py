#ass4 setaq1 slip10q2
#write a python programme to read the dataset("Iris.csv").dataset
#sownload from
#(http://archive.uci.edu/ml/dataset/iris)and apply Apriori algorithm
{
"cells:"[
 {
    "cell_type":"markdown",
    "id":"b58228cb",
    "metadata":{}
    "source":[
    " #SET -A\n",
    "\n",
    "### 1) Write a code to read the dataset("Iris.csv").dataset download from
(https://archive.ics.uci.edu/ml/datasets/iris)and apply Apriori algorithm."

]
  
 },
    {
    "cell_type":"code"
    "execution_count":1,
    "metadata":{},
    "output":[],
    "source":[
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import apyori import apriori"
    ] 
    },
    {
         
    "cell_type":"code",
    "execution_count":null,
    "id":"91ef7af6",
    "metadata":{},
    "outputs":[],
    "source":[
    "store_data=pd.read_csv('iris.csv',header=None)"
    ]
    },
    {
    "cell_type":"code",
    "execution_count":null,
    "id":"cd4c9ed9",
    "metadata":{},
    "outputs":[],
    "source":[
    "store_data.head()\n"
    ]
    },
    {
    "cell_type":"code",
    "execution_count":null,
    "id":"88d01808",
    "metadata":{},
    "outputs":[],
    "source":[
    "records=[]\n",
    "for i in range(0,300):\n"
    "records.append([str(store_data.values[i,j]for j in range(0,20)])\n"
    ]
         
    },
    {
    "cell_type":"code",
    "execution_count":null,
    "id":"ba30cca3",
    "metadata":{},
    "outputs":[],
    "source":[
    "association_rules=apriori(records,min_support=0.0045,min_confidence=0.2.min_lift=3,min_lengthh=2)\n",
    "association_results=list(association_rules)\n"
    ]

    },
    {
    "cell_type":"code",
    "execution_count":null,
    "id":"8ab0102a",
    "metadata":{},
    "outputs":[],
    "source":[
    "print(len(association_results))\n"
    ]
         
    },
    {
    "cell_type":"code",
    "execution_count":null,
    "id":"daa923d5",
    "metadata":{},
    "outputs":[],
    "source":[
    "print(association_results[0])\n"
    ]

    },
    {
    "cell_type":"code",
    "execution_count":null,
    "id":"4f9ceaad",
    "metadata":{},
    "outputs":[],
    "source":[
    "for item in association_results:\n",
    "pair =item[0]\n",
    "items=[x for x in pair]\n",
    "print(\"Rule:\"+items[0]+\"->\"+items[1])\n",
    "\n",
    "print(\:Support:\"+str(item[1]))\n",
    "\n",
    "print(\:Confidence:\"+str)item[2][0][2]))\n",
    "print(\"Lift:\"+str(item[2][0][3]))\n",
    "print(\"====================\")"
    ]
         
    }
],

    
    "metadata":{
    "kernelspec":{
    "display_name":"Puthon 3(ipykernel)",
    "language":"python",
    "name":"python3"
    },
    "language_info":
    {
    "codemirror_mode":{
    "name":"ipython",
    "version":3
    },
    "file_extension":".py"
    "mimetype":"text/x-python",
    "name":"python",
    "nbconvert_exporter":"python",
    "pygments_lexer":"ipython3",
    "version":"3.7.9"
    }
},

"nbformat":4,
"nbformat_minor":5
}


 