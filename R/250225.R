library(ggplot2)
library(dplyr)

df <- ggplot2::midwest
# head(df)
# dim(df)
# str(df)

# View(df)

df2 <- df %>%
  rename(asian = percasian) %>%
  rename(total = poptotal) %>%
  rename(adult = popadults) %>%
  mutate(child = total - adult) %>%
  mutate(child_ratio = (child / total) * 100) %>%
  arrange(child_ratio)

head(df2)

df3 <- select(df2, county, total, adult, child, child_ratio)
head(df3)

# ifelse() 간단하게
iftest <- function(flag, t_value, f_value) {
  result <- c()
  result_index <- 1
  for (i in flag) {
    if (i) {
      result[result_index] <- t_value
    } else {
      result[result_index] <- f_value
    }
    result_index <- result_index + 1
  }
  return(result)
}

df3$test <- iftest(df3$child_ratio > 49, "large", "small")
df3

# df2 <- df %>%
#     select(total,black,asian,amerindan)

# df2 <- df2 %>% mutate(ratio = asian / total * 100)
# df2

# m <- mean(df2$ratio)
# m
# df2$rank <- ifelse(df2$ratio > m, "large", ifelse(df2$ratio == m, "middle", "small"))

# tail(df2)

# df2 <- df2[order(df2$asian), ]
# head(df2,20)

# large_cnt <- 0
# middle_cnt <- 0
# small_cnt <- 0

# for (i in df2$rank) {
#   if (i == "large") {
#     large_cnt <- large_cnt + 1
#   } else if (i == "middle") {
#     middle_cnt <- middle_cnt + 1
#   } else if (i == "small") {
#     small_cnt <- small_cnt + 1
#   }
# }

# print(c(large_cnt, middle_cnt, small_cnt))








