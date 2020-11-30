# Question 1: FNN Implementation of a simple Neural Probabilistic model

#### Main Notebooks
ass2_q1_iv.ipynb
ass2_q1.ipynb

The above notebooks are used to train each corresponding network that varies in parameters. 
ass2_q1_iv.ipynb is a network before weight tying.
ass2_q1.ipynb is after the input and output weights are tied.

The implementation of [A neural probabilistic language model](https://jmlr.org/papers/volume3/tmp/bengio03a.pdf) using the PyTorch [word language examples](https://github.com/pytorch/examples/tree/master/word_language_model)  

#### Note for Running:

If running on Google Colab, ensure that the Google Drive that is linked has the dataset in the folder 'wiki-text-2'. Else, omit the first 2 code blocks. 

The dataset can be obtained from [here](https://github.com/pytorch/examples/tree/master/word_language_model/data/wikitext-2).


# Question 2: CNN Implementation of BiLSTM-CRF Model

#### Main Notebooks
ner_cnn_1.ipynb
ner_cnn_2.ipynb
ner_cnn_3.ipynb
ner_cnn_4.ipynb
ner_cnn_5.ipynb
ner_cnn_6.ipynb

The above notebooks are used to train each corresponding number of CNN layers. They share the same code, with only the training results and graphs differing from each other.

CNNAnalysis.ipynb is used to generate the final comparison graphs between all 6 models. Each model has their results stored in the corresponding txt files as logs.

#### Note for Running:
The notebooks are run on a multi-gpu system. As such, the ```cuda(gpu_num)``` needs to be edited accordingly to your own machine to run. To run your default gpu, simply change the usages to ```cuda()```.
___

###### Members

1. Muddineni Krishnavyas 
2. Tan Zhi Yang 
3. Tan Sheng Rong (Leader)
4. Toh Ting Yu Darren 
5. Wang Guan Zhi, Leonard