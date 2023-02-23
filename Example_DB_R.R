#R script with examples of codes that I used to work with DB
#  For the first example I have a DB of surveys with information of public transport driver for a study of road safety. 

install.packages("tidyverse")
library(tidyverse)
install.packages("readxl")
library(readxl)
install.packages("PDE", dependencies = TRUE)

encuestas <- read_excel("Registros encuestas (1).xlsx") # DB from the survey. I can´t share this information
licencias <- read_excel("licencias a revisar.xlsx") # licences to check and transform some data on the encuestas DB


library("PDE")
PDE_pdfs2table()

