library(tidyverse)

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

d.subj = read.csv("../results/subject_control.csv")
d.obj = read.csv("../results/object_control.csv")
d.intrans = read.csv("../results/subject_intransitive.csv")



d.subj %>% 
  group_by(verb) %>% 
  dplyr::summarize(accuracy = mean(correct), ci_low = mean(correct) - ci.low(correct), ci_high = mean(correct) + ci.high(correct))



d.obj %>% 
  group_by(verb) %>% 
  dplyr::summarize(accuracy = mean(correct), ci_low = mean(correct) - ci.low(correct), ci_high = mean(correct) + ci.high(correct))

d.intrans %>%
  group_by(verb) %>% 
  dplyr::summarize(accuracy = mean(correct), ci_low = mean(correct) - ci.low(correct), ci_high = mean(correct) + ci.high(correct))


d.subj %>% 
  dplyr::summarize(accuracy = mean(correct), ci_low = mean(correct) - ci.low(correct), ci_high = mean(correct) + ci.high(correct))


d.obj %>% 
  dplyr::summarize(accuracy = mean(correct), ci_low = mean(correct) - ci.low(correct), ci_high = mean(correct) + ci.high(correct))


#### GPT-2 XL

d.subj = read.csv("../results/subject_control.gpt2-xl.csv")
d.obj = read.csv("../results/object_control.gpt2-xl.csv")
d.intrans = read.csv("../results/subject_intransitive.gpt2-xl.csv")



d.subj %>% 
  group_by(verb) %>% 
  dplyr::summarize(accuracy = mean(correct), ci_low = mean(correct) - ci.low(correct), ci_high = mean(correct) + ci.high(correct))


d.obj %>% 
  group_by(verb) %>% 
  dplyr::summarize(accuracy = mean(correct), ci_low = mean(correct) - ci.low(correct), ci_high = mean(correct) + ci.high(correct))

d.intrans %>%
  group_by(verb) %>% 
  dplyr::summarize(accuracy = mean(correct), ci_low = mean(correct) - ci.low(correct), ci_high = mean(correct) + ci.high(correct))


d.subj %>% 
  dplyr::summarize(accuracy = mean(correct), ci_low = mean(correct) - ci.low(correct), ci_high = mean(correct) + ci.high(correct))


d.obj %>% 
  dplyr::summarize(accuracy = mean(correct), ci_low = mean(correct) - ci.low(correct), ci_high = mean(correct) + ci.high(correct))


