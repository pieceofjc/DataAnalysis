cv <- read.csv(file <- "./수업/R/data/csv_exam.csv")
cv

pv <- read.csv(file <- "C:/Users/SAMSUNG/Downloads/JY/수업/R/data/csv_exam.csv")
pv

head(cv,10) # default 6, 20까지

tail(cv,8) # default 6

dim(cv) # row, col

str(cv) # 정보

View(cv) # 뷰어

summary(cv) # 통계량

cv$total <- cv$math + cv$english + cv$science
cv

cv$mean <- cv$total / 3
cv

cv$pass <- ifelse(cv$mean > 65, "pass", ifelse(cv$mean == 65, "hold", "fail"))
cv

cv <- cv %>%
  rename(mscore = mean)

cv

cv[cv$class == 1, ]

select(cv[cv$class == 3, ], class, math:science)

arrange(cv, desc(math)) # 내림차순
arrange(cv, -math) # 내림차순

cv %>%
    group_by(math) %>%
    summarise(math)

a <- data.frame(id = c(1, 2, 3), gender = c(1, 2, 1))
b <- data.frame(id = c(4, 5, 6), gender = c(2, 2, 2))
rbind(a, b)

d <- data.frame(id = c(1, 2, 1), gender = c(2, 2, 2))

e <- inner_join(a,d,by="id")
e

f <- left_join(a,d,by="id")
f

g <- right_join(a,d,by="id")
g

h <- full_join(a,d,by="id")
h

inner_join(
    inner_join(a,c,by="id"),
    b,
    by = "id")

library(ggplot2)
library(dplyr)

df <- ggplot2::midwest
head(df)
dim(df)
str(df)

View(df)

df <- df %>%
  rename(asian = percasian) %>%
  rename(black = percamerindan) %>%
  rename(total = poptotal)

df <- df %>%
  rename(amerindan = black) %>%
  rename(black = percblack)

df2 <- df %>%
    select(total,black,asian,amerindan)

df2 <- df2 %>% mutate(ratio = asian / total * 100)
df2

m <- mean(df2$ratio)
m
df2$rank <- ifelse(df2$ratio > m, "large", ifelse(df2$ratio == m, "middle", "small"))

tail(df2)

df2 <- df2[order(df2$asian), ]
head(df2,20)

large_cnt <- 0
middle_cnt <- 0
small_cnt <- 0

for (i in df2$rank) {
  if (i == "large") {
    large_cnt <- large_cnt + 1
  } else if (i == "middle") {
    middle_cnt <- middle_cnt + 1
  } else if (i == "small") {
    small_cnt <- small_cnt + 1
  }
}

print(c(large_cnt, middle_cnt, small_cnt))



