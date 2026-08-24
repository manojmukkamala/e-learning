# R

R tutorials. Currently contains one course:

- [`Introduction to Text Analytics with R/`](Introduction%20to%20Text%20Analytics%20with%20R/)
  — the 12-part Data Science Dojo YouTube series on text analytics with
  R (TF-IDF, naive Bayes, random forests on SMS spam data). The folder
  has its own `README.md` with links to every video.

## Introduction to Text Analytics with R — how to run it

Requires [R](https://cran.r-project.org/) (3.x+; RStudio optional).
Each `IntroToTextAnalytics_PartN.R` starts by installing the packages it
needs (`ggplot2`, `e1071`, `caret`, `quanteda`, `irlba`,
`randomForest`) — let Part 1 do that first.

The scripts expect the dataset in the working directory:

1. Download the [Kaggle SMS Spam Collection
   Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
   (originally from the [UCI ML
   Repository](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection))
   as `spam.csv` — note the scripts read it with
   `fileEncoding = "UTF-16"`, so keep the original encoding.
2. Run the parts in order (`Part1.R` → `Part12.R`).
3. Parts 10–12 `load()` the `rf.cv.1..4.RData` model artifacts; drop
   those files in the working directory before reaching Part 10.

`spam.csv` and the `rf.cv.*.RData` files are not committed to this repo
(design choice — see `../AGENTS.md`). Re-download them from the course
author's repo: <https://github.com/datasciencedojo/IntroToTextAnalyticsWithR>.
