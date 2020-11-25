# Assignment 8: Exploratory Data Analysis

MACS 30000, Autumn 2019

Due **Monday, December 9 at 11:30am**

Worth **10 points**

--------------------

For this assignment, you will continue to work with the General Social Survey (GSS) [2018 data](http://gss.norc.org/get-the-data/stata) that you wrangled in Assignment 7. Using the exploratory data analysis skills we have reviewed in-class, you will conduct an exploratory analysis of the data to identify interesting questions and (potential) answers. Recall the types of questions we seek to answer using EDA:

1. What type of variation occurs within my variables?
1. What type of covariation occurs between my variables?
1. Are there outliers in the data?
1. Do I have missingness? Are there patterns to it?
1. How much variation/error exists in my statistical estimates? Is there a pattern to it?

## What not to do

##### Build a statistical model

No complex statistical methods should be employed. Focus instead on primarily graphical analysis, though you can also use basic statistical tests you may have learned in other classes (e.g. tests for normality, difference of means).

##### Adjust for survey weights

Do not worry about using survey weights in your exploratory analysis. Just treat every observation equally.

## What you should do

The final submission should include two components.

### Lab notebook (6 points)

This is a record of all your exploratory analysis. It should be extensive (minimum 30-40 graphs), and mostly code and graphics.

* Minimally annotate your code and output as necessary to keep track of what you've done and highlight important insights gained through your exploration
* It should be somewhat stream-of-consciousness (that is, a stored record of your exploration as you explore the data), though certainly feel free to maintain a structure or go back and reformat different sections
* Don't bother cleaning up each graph to have meaningful labels

### Exploration write-up (4 points)

In a short response (around 750 words), summarize your insights and what you've learned about the data. This could include one or two important research questions you think you could answer using the data, as well as some initial hypotheses supported by your exploratory analysis. Or perhaps you've identified unusual variation in a single variable, or extreme outliers or systematic missingness in the data that should be accounted for in future analysis. **This component will look different for each student.** That's fine. What we want to see is genuine effort and some thought put into what you've learned from this EDA.

* This component should include mostly written analysis and a handful (1-3) of graphs to support your questions and answers
* Clean up these graphs so that they are publication-ready. This means that you should give each graph a meaningful title, axes labels, legends, etc.

## Dataset documentation

Consult the GSS codebook [index](https://gss.norc.org/documents/codebook/GSS_Codebook_index.pdf) and [main body](https://gss.norc.org/documents/codebook/GSS_Codebook_mainbody.pdf) for more details on the meanings of column names and value codes. The index contains a list of all variables available from the GSS, with their variable names in the data file and a brief description of the variable. The main body contains a detailed description of all variables available from the GSS, with full question wording and potential responses. You can also find more information about the survey at the [GSS website](http://gss.norc.org/).

## Writing the code

Here are some relevant resources for how to write code in Python or R to generate EDA graphs.

* [VanderPlas, Jake. (2016). *Python Data Science Handbook*. O'Reilly Media, Inc.](http://proquestcombo.safaribooksonline.com.proxy.uchicago.edu/book/programming/python/9781491912126)
* [Unwin, A. (2015). *Graphical data analysis with R* (Vol. 27). CRC Press.](http://proquestcombo.safaribooksonline.com.proxy.uchicago.edu/9781498786775)

## Submission format

Submit your assignment as a set of **reproducible notebooks** - one notebook for the lab notebook, and one notebook for the exploration write-up.

* If you use Python, this means a Jupyter Notebook (`.ipynb`).
* If you use R, this means a Jupyter Notebook (`.ipynb`) or R Markdown document (`.Rmd` knitted with `output: github_document` or `output: pdf_document` in the [front matter](http://rmarkdown.rstudio.com/markdown_document_format.html) - HTML documents are frowned upon as they cannot be viewed directly on GitHub). Be sure to stage and commit not only the source file but also the output images as well so everything is visible in GitHub.

**Do not submit a plain `.py` or `.R` script.** Your generated graphs will not be visible in the repo, and we will not be running every single script to ensure it works correctly. Make sure to use a notebook format. If you have questions about this, please ask.
