df <- read.csv('study_data_clean.csv')
fit <- lm(score ~ hours * method, data=df)
summary(fit)
