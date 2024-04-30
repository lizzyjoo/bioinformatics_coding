# Analyze data from The Cancer Genome Atlas (TCGA)
# Analyze smoking-related clinical variables recorded for a subset of patients 

# install biostatistics course package to obtain clinical data csv file
remotes::install_github("UCLouvain-CBIO/rWSBIM1207")  
# tidyverse library
library("tidyverse")

# from library
library("rWSBIM1207")

# using .csv() function to get path, than read as dataframe
clinical <- read.csv(clinical1.csv())

# structure of the data frame
str(clinical)

# create data frame with just the following columns: 
# patientID, gender, age_at_diagnosis, smoking_history, 
# number_pack_years_smoked, year_of_tobacco_smoking_onset, and stopped_smoking_year.

clinical_mini <- select(clinical, patientID, gender, age_at_diagnosis, smoking_history, number_pack_years_smoked, year_of_tobacco_smoking_onset, stopped_smoking_year)
clinical_mini

# the number of males and females in the cohort
clinical_mini %>% 
  count(gender)

# or
clinical_mini %>%
  group_by(gender) %>%
  count()

# variable corresponding to the age at diagnosis converted from days into years
clinical_mini <- clinical_mini %>%
  mutate(years_at_diagnosis = age_at_diagnosis / 365)

select(clinical_mini,
       years_at_diagnosis,
       age_at_diagnosis)
# mean and median age at diagnosisl use summarize function 
clinical_mini %>%
  summarize(mean = mean(years_at_diagnosis, na.rm = TRUE),
            median = median(years_at_diagnosis, na.rm = TRUE))
# can also remove NA values prior using filter
clinical_mini %>%
  filter(!is.na(years_at_diagnosis)) %>%
  summarize(mean = mean(years_at_diagnosis),
            median = median(years_at_diagnosis))

# the mean and median age at diagnosis for males and females.
clinical_mini %>% 
  group_by(gender) %>% 
  summarize(mean = mean(years_at_diagnosis, na.rm = TRUE),
            median = median(years_at_diagnosis, na.rm= TRUE))

# number of people who were diagnosed before year 50
clinical_mini %>% 
  
  filter(years_at_diagnosis < 50) %>% 
  count()

# compare the mean age at diagnosis between current smoker and lifelong non-smoker (smoking_history)
clinical_mini %>% 
  filter(smoking_history == 'current smoker' | smoking_history == 'lifelong non-smoker') %>% 
  group_by(smoking_history) %>% 
  summarize(mean = mean(years_at_diagnosis, na.rm = TRUE))

# patients who stopped smoking more than 15 years ago; the number of smoking years for these cases
clinical_mini %>% 
  filter(smoking_history == "current reformed smoker for > 15 years") %>%
  mutate(years_smoked = stopped_smoking_year - year_of_tobacco_smoking_onset) %>%
  filter(!is.na(years_smoked)) %>%
  select(patientID, years_smoked)


clinical_mini %>%
  filter(smoking_history == 'current smoker' | smoking_history == 'lifelong non-smoker') %>%
  group_by(gender, smoking_history) %>%
  summarize(n = n()) %>%
  pivot_wider(names_from = "smoking_history",
              values_from = "n")  