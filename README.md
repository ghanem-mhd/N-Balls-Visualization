


# N-Balls-Visualization

This package will help you to visualize high dimensional balls generated by the method proposed [here](https://github.com/gnodisnait/nball4tree). The method precisely imposes tree-structured category information onto word-embeddings, resulting in ball embeddings in higher dimensional spaces (N-balls for short). In addition to visualizing, the package can also be used to generate balls for a set of input words.

The process consists of three steps:
1. [Generating Nballs](#n-balls-generation)
2. [Reducing Dimensionality](#reducing-dimensionality)
3. [Plotting](#plotting)

# Table of Contents:
* [Generating Nballs](#n-balls-generation)
	* [Input](#input)
	* [Output](#output)
	* [Using Jupyter Notebook](#using-jupyter-notebook)
	* [Using Command-line](#using-command-line)
* [Reducing Dimensionality](#reducing-dimensionality)
	* [The Fixing Algorithm](#the-fixing-algorithm)
	* [Input](#input-1)
	* [Output](#output-1)
	* [Using Jupyter Notebook](#using-jupyter-notebook-1)
	* [Using Command-line](#using-command-line-1)
	* [Console Output Explanation](#console-output-explanation)
* [Plotting](#plotting)
	* [Input](#input-2)
	* [Output](#output-2)
	* [Using Jupyter Notebook](#using-jupyter-notebook-2)
	* [Plotting Options](#plotting-options)
	* [Using Command-line](#using-command-line-2)
* [Examples](#examples)

If you already have the balls in high dimensions you can skip the first step and go directly to [step 2](reducing-dimensionality).

## Getting Started
The package can be used in two ways. The first one by running the [Jupyter Notebooks](https://github.com/ghanem-mhd/N-Balls-Visualization/tree/master/jupyter_notebooks). The second one is just through command line by running the desired function. 

We recommend to install [Anaconda](https://www.anaconda.com/distribution/) as it contains all the required dependencies to run this package. Otherwise if you prefer to do it the hard way, feel free to install all the requirements for this package.

### Prerequisites
After setting up Anaconda or installing the requirements by yourself, please take care of the following:

* In case you want to use jupyter notebooks, please make sure you have the latest version of [Ipywidgets](https://github.com/jupyter-widgets/ipywidgets) package. 

* In case you want to use the package to generate balls regardless of using jupyter notebooks or command line, make sure you already downloaded Wordnet resource by running the following:
  ```
  implort nltk
  nltk.donwload()
  ```
  
## N-Balls Generation: 
You can use the package to generate the balls for a set of words. This step is optional and can be skipped if you already have the balls generated. 

### Input:
* **Set of words:**  You can either choose one of the predefined samples or just enter your words in English only.
* **Pre-trained word embeddings:** You have to give a path to file which contains a pre-trained word embedding. In case you don't have this file you can download from [here](https://drive.google.com/open?id=1Liu7AynOXXv7gWXVs4npuKAZeSygbGWQ). The file provided in the previous link taken from [GloVe](https://nlp.stanford.edu/projects/glove/) (6B tokens, 400K vocab, uncased, 50d).

### Output:
* **Nballs:** A file contains the balls in high dimensions with the tree structure perfectly encoded.

### Using Jupyter Notebook:
Open [Nballs Generation Notebook](https://github.com/ghanem-mhd/N-Balls-Visualization/blob/master/jupyter_notebooks/nballs-generation.ipynb). The notebook is consist from only one cell. To generate the balls follow the following steps:
1. Run the cell. A drop down list will be shown. Select one of the samples provided or custom option.
2. If you select custom option, another input field will be shown to let you enter you words comma separated. Click check button to move to the next step.
3. After selecting the input sample or the custom option another input field will be shown to provide a word2vector file path.
4. After providing the file path, click on generate balls button.
5. The log will be shown to indicate the status of the process. You can find the generate balls file in the data directory of the project.

### Using Command-line:
Run the following command:
```
python main.py --generate_nballs --input INPUT_FILE --w2v WORD2VECTOR_FILE --output OUTPUT_FILE_PATH
```
* --input: A file contains words. Each line should contain one word.
* --w2v: A file of pre-trained word embeddings.
* --output: The output directory.

## Reducing Dimensionality:
The package will visualize the balls in 2d.  The dimensions of the balls will be reduced to 2. In other words, the balls will be converted to circles. In this step, the PCA method is used to reduce the dimensions. During the PCA, some of the tree relationships are not maintained e.g. siblings circles might be overlapped or child circle located outside its parent circle an algorithm is being used to fix these broken relationships. 

### The Fixing Algorithm:
The idea behind the algorithm is to fix the broken relationships between circles while keeping its topological structure. The algorithm uses the information provided by the tree structure and the balls in high dimensions to determine whether two circles need to be modified to recover the original status between them. The algorithm checks two conditions the first one is "Is disjoint" and the second one is "Is contained". The first condition is being checked for all children of one family. The second one is being checked for a parent of one family with its children.

If the first condition is not satisfied, which means two circles are overlapping while they should be disjoint, the two circles will be scaled down (only radius) by a factor which makes the two circles disjoint. If one of the circles has children, all children will also be scaled down and shifted. By doing so all the topological relationships between the children of the circles will be kept.

If the second condition is not satisfied, which means a child circle is located or overlapping with its parent, the parent circle will be scaled up (only radius) by a factor which makes the child circle located inside its parent. Also in case, the parent circles contain other child circles, all of them will be scaled by the same factor and shifted.

### Input:
The input of this step is the following:
* **Nballs:**  The file contains the balls which generated by step 1 or your own balls file.
* **Children:** A file contains the child-parent relationships between the balls. 

### Output:
* **Output Before:** A file contains the circles after applying PCA on balls and without fixing the broken relationships.
* **Output After:** A file contains the circles after applying PCA and fixing the broken relationships.
* Both files can be found in the data folder of the project.

### Using Jupyter Notebook:
Open [Interactive Visualization Notebook](https://github.com/ghanem-mhd/N-Balls-Visualization/blob/master/jupyter_notebooks/interactive_visualization.ipynb). To reduce the dimensions follow the following steps:
1. Run the first cell. Two file upload buttons will be shown. One for balls files and the other for children file.
2. Select the corresponding files for each one. After choosing the files the reduce button will be enabled.  
3. Click on reduce button and check the [result]((#console-output-explanation)).

### Using Command-line:
```
python main.py --reduceAndFix --balls BALLS_FILE_PATH --children CHILDREN_FILE_PATH --output_path OUTPUT_FILE_PATH
```
* --balls: A file contains the balls which generated by step 1 or your own balls file.
* --children: A file contains the child-parent relationships between the balls.
* --output: The output file which contains the circles. The path will be used to generate two files one contains the circles before applying the algorithm and one after applying the algorithm.

### Console Output Explanation:
After executing dimensionality reduction step, the result of three check operations will be shown. Each operation checks whether the tree structure is maintained by checking two conditions, namely disjoint and contains conditions. The first operation is performed on the input balls. The second one is performed on the circles before running the fixing of the algorithm. The third one is performed on the circles after running the algorithm.

## Plotting:
During this step, the circles from the second step will be visualized. In the visualization, every circle corresponds to a word. The word is shown at a random point on the circle perimeter with the same color as the circle.

### Input:
* **Circles:**  The file used as output in the [Reducing Dimensionality](#reducing-dimensionality). 
* **Set of words:**  You can either choose one of the predefined samples or just enter your words in English only.

### Output:
* **None**

### Using Jupyter Notebook:
Open [Interactive Visualization Notebook](https://github.com/ghanem-mhd/N-Balls-Visualization/blob/master/jupyter_notebooks/interactive_visualization.ipynb). To plot the circles from the second step, follow the following steps:
1. Run the second cell. Please make sure you already executed the [Reducing Dimensionality](#reducing-dimensionality).
2. An interactive UI elements will be shown.
3. Read [plotting options](#plotting-options) for more information.

#### Plotting Options:
* **Filter:** You can use the filter to show or hide certain words. The filter can be operated in two modes: SubTree and Individual.
* **SubTree Filter Mode:** In this mode, whenever you hide one of the words all children will be hidden. Also, whenever you check one of the words all the ancestors of the words will be shown.
* **Individual Filter Mode:** In this mode, hiding or showing a word will only affect the words itself.
* **Show All:** This button will show all words.
* **Hide All:** This button will hide all words.
* **Circles:** This toggle button is to switch between the circles before and after applying the fixing algorithm.

### Using Command-line:
Please note that using the Jupyter notebook will be more useful as we can directly filter some words.
```
python main.py --vis --circles CIRCLES_FILE_PATH --showenWords WORDS_FILE_PATH
```
* --circles: A path to the file used in the [Reducing Dimensionality](#reducing-dimensionality).
* --showenWords: A path to file contains the words that should be visualized. Each line should contain one word. This parameter is optional and if it is not present all words will be visualized.

## Examples:
### Examaple 1:
This small example demonstrate how the visualization is keeping the topological structure of the balls. This example contains 4 balls. The parent is capital.n.03 with three children: berlin.n.01, amsterdam.n.01 and paris.n.01. The first two balls berlin.n.01 and amsterdam.n.01 are externally discontent. The child ball paris.n.01 is internally contained in the parent ball. After reducing the dimensions the circles corresponding to the balls are still have the same topological relationships. The following picture showing the result of the plotting.
![Example 1 plotting](https://github.com/ghanem-mhd/N-Balls-Visualization/blob/master/pic/example1.PNG)



