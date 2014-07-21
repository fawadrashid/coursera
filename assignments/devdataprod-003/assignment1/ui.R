
# This is the user-interface definition of a Shiny web application.
# You can find out more about building applications with Shiny here:
# 
# http://www.rstudio.com/shiny/
#
library(shiny)
#data(USArrests)

shinyUI(pageWithSidebar(
  
  # Application title
  headerPanel("US Arrests Data"),
  
  # Sidebar with a slider input for number of bins
  sidebarPanel(
    # Copy the line below to make a select box 
    selectInput("selectAttrocities", label = h3("Select Crime Type"), 
                choices = names(USArrests), 
                selected = 1),
    
    
    textOutput("selectionText")
    
  ),
  
  # Show a plot of the generated distribution
  mainPanel(
    plotOutput("attrocitiesPlot")
  )
))

