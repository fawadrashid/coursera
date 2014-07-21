
# This is the server logic for a Shiny web application.
# You can find out more about building applications with Shiny here:
# 
# http://www.rstudio.com/shiny/
#

library(shiny)
#install.packages('gridBase')
library(gridBase)
library(grid)
library(devtools)
#data(USArrests)

shinyServer(function(input, output) {
  
  # Fill in the spot we created for a plot
  output$attrocitiesPlot <- renderPlot({
    
    midpts <- barplot(USArrests[,input$selectAttrocities], 
                      names.arg="",
                      col=rainbow(nrow(USArrests)),
                      ylab=input$selectAttrocities,
                      xlab="", beside=TRUE)
    
    ## Use grid to add the labels    
    vps <- baseViewports()
    pushViewport(vps$inner, vps$figure, vps$plot)
    
    grid.text(rownames(USArrests),
              x = unit(midpts, "native"), y=unit(-1, "lines"),
              just="right", rot=50)
    
    popViewport(3)
    
    output$selectionText <- renderText(paste("Crime selected:" , input$selectAttrocities))
    #verbatimTextOutput("Crime selected:" + input$selectAttrocities)
     
  })
  
})
