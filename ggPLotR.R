library(datasets)
data(iris)
##
ggplot(data= iris, aes(x=Species,y=Petal.Length, color=Species,shape=Species,size=Species))+
  geom_point()+
  facet_wrap(~species)+
  labs(subtitle="Species VS Petal LEngth",title="IRIS -Species",caption = "Reference provided by IRIS Dataset")+

## GGPAris

    install.packages("GGally",repos = "https://cran.r-project.org", type= "source") 

  library(GGally)

ggpairs(iris, mapping=ggplot2::aes(color = Species, size = Species, shape = Species))
  
