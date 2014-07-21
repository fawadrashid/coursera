---
title       : Coursera Developing Data Products Course
subtitle    : Assignment 1
author      : Fawad Rashid
job         : USA Arrests rates across states by crimes
framework   : io2012        # {io2012, html5slides, shower, dzslides, ...}
highlighter : highlight.js  # {highlight.js, prettify, highlight}
hitheme     : tomorrow      # 
widgets     : []            # {mathjax, quiz, bootstrap}
mode        : selfcontained # {standalone, draft}
knit        : slidify::knit2slides
---

## Description

Thi is a Shiny app that visualizes USA arrests dataset. The application allows user to select a crime type and see the crime across states using a barplot

--- 

## Details

The barplot shows the spread of a cetain crime type across the various US states. You may select a crime type to see the crime rate across various states. 

---

## Crime trends graph example

Here is a crime chart barplot


```r
df<- midpts <- barplot(USArrests[,"Murder"], 
                      names.arg="",
                      col=rainbow(nrow(USArrests)),
                      ylab="Murder",
                      xlab="", beside=TRUE)
```

![plot of chunk unnamed-chunk-1](assets/fig/unnamed-chunk-1.png) 
---

## Graph explained

The graph uses reactive select input that triggers bar plot. The select input crime type which is read from the USArrests dataset columns triggers the bar plot re-render when the selection is changed. The graph is quite simple as the dataset is quite simple as well. It plots the number of crimes of a certain  crime type plotted across US states


---
## Conclusion

The application took me more time as it should have around 3-4 hours as I have very little experience wth R. I have very little experience with data analysis hence i chose to do something simple in a attempt to demostrate that I have understood most of what was taught in regards to Shiny during the class

The plot was quite simply to draw although getting the x axis labels aligned took me some time

I hope i was able to complete the assignment with the limited knoweledge I had 
