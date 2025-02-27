
# 시각화
mpg <- ggplot2::mpg
ggplot(data <- mpg, aes(displ, hwy, colour = class)) + geom_point()

ggplot(
  data <- mpg,
  aes(x <- drv)
) + geom_bar()

table(mpg$drv)

group_data <- mpg %>%
  group_by(drv) %>%
  summarise(mean_hwy = mean(hwy))

group_data

ggplot(
  data <- group_data,
  aes(x <- drv, y <- mean_hwy)
) + geom_col()

ggplot(
  data <- mpg,
  aes(x <- drv, y <- hwy)
) + geom_boxplot()

group_data2 <- mpg %>%
  group_by(year) %>%
  summarise(count = n())

ggplot(
  data <- group_data2,
  aes(x <- year, y <- count)
) + geom_line()

library(foreign)

df <- read.spss("./수업/R/data/Koweps.sav", to.data.frame = T)

df2 <- df %>%
  select(h10_g3, h10_g4, h10_eco9, p1002_8aq1, h10_reg7) %>%
  rename(gender = h10_g3, birth = h10_g4, code_job = h10_eco9, income = p1002_8aq1, loc = h10_reg7) %>%
  mutate(age = 2025 - birth + 1)

# 결측치 처리하기
str(df2)
summary(df2)

table(is.na(df2))

table(is.na(df2$gender))
table(is.na(df2$birth))
table(is.na(df2$code_job))
table(is.na(df2$income))
table(is.na(df2$loc))
table(is.na(df2$age))

# 성별 데이터를 1 -> male 2 -> female
df2$gender <- ifelse(df2$gender == 1, "male", ifelse(df2$gender == 2, "female", NA))

table(df2$gender)
table(is.na(df2$gender))

# 성별 평균 임금의 차이
df3 <- df2 %>%
  select(gender, income) %>%
  filter(!is.na(income) & income != 9999 & income != 0) %>%
  group_by(gender) %>%
  summarise(mean_income = mean(income))

summary(df3)

ggplot(
  data <- df3,
  aes(x <- gender, y <- mean_income)
) + geom_col()

df2$age <- df2$age - 10

df4 <- df2 %>%
  select(age, income) %>%
  filter(!is.na(income) & income != 9999 & income != 0) %>%
  filter(!is.na(age) & age != 9999 & age != 0) %>%  
  group_by(age) %>%
  summarise(age_income = mean(income)) %>%
  arrange(desc(age_income))

summary(df4)

head(df4, 5)

ggplot(
  data <- df4,
  aes(x <- age, y <- age_income)
) + geom_col()

df5 <- df2 %>%
  select(age, income) %>%
  filter(!is.na(income) & income != 9999 & income != 0) %>%
  filter(!is.na(age) & age != 9999 & age != 0) %>% 
  mutate(class = ifelse(age < 40, "young", ifelse(age >= 40 & age < 60, "middle", "old"))) %>%
  group_by(class) %>%
  summarise(class_income = mean(income))

summary(df5)
table(df5)

ggplot(
  data <- df5,
  aes(x <- factor(class, levels = c("young", "middle", "old")), y <- class_income),  
) + geom_col()

ggplot(
  data <- df5,
  aes(x <- class, y <- class_income),  
) + geom_col() + scale_x_discrete(
  limits = c("young", "middle", "old")
)

df6 <- df2 %>%
  select(loc, income) %>%
  filter(!is.na(income) & income != 9999 & income != 0) %>%
  filter(!is.na(loc)) %>% 
  group_by(loc) %>%
  summarise(loc_income = mean(income))

head(df6,7)

ggplot(
  data <- df6,
  aes(x <- loc, y <-  loc_income),  
) + geom_col()

df7 <- df2 %>%
  select(loc, income, gender) %>%
  filter(!is.na(income) & income != 9999 & income != 0) %>%
  filter(!is.na(loc)) %>% 
  group_by(loc, gender) %>%
  summarise(c_income = mean(income))

head(df7, 20)

# 1. 서울          2. 수도권(인천/경기)    3. 부산/경남/울산   4.대구/경북   
# 5. 대전/충남   6. 강원/충북               7.광주/전남/전북/제주도
df7 <- mutate(df7, loc = ifelse(loc == 1, "서울", 
  ifelse(loc == 2, "수도권(인천/경기)", 
  ifelse(loc == 3, "부산/경남/울산", 
  ifelse(loc == 4, "대구/경북", 
  ifelse(loc == 5, "대전/충남",
  ifelse(loc == 6, "강원/충북",
  ifelse(loc == 7, "광주/전남/전북/제주도"))))))))

loc_gender_income_plot <- ggplot(
  data <- df7,
  aes(x <- loc, y <- c_income, fill = gender),  
) + geom_col(position = 'dodge')

library(plotly)

ggplotly(loc_gender_income_plot)


code_book = read_excel("수업/R/data/Koweps_Codebook.xlsx", sheet = 2)
code_book


df9 <- left_join(
  df2, code_book, by = "code_job"
)

dim(df9)

# code_job 결측치가 아니고, job이 결측치인 값이 존재하는가?
# 데이터에 job에 없는 code_job이 존재하는가? 안맞는게 존재하는가?
# 확인
df9 %>%
  filter(!is.na(code_job)) %>%
  filter(is.na(job))

summary(df9)
tail(df9)

df10 <- df9 %>%
  select(code_job, job, income) %>%
  filter(!is.na(income) & income != 9999 & income != 0) %>%
  filter(!is.na(job)) %>%
  group_by(job) %>%
  summarise(job_income = mean(income), job_cnt = n()) %>%
  filter(job_cnt >= 10) %>%
  arrange(desc(job_income))

summary(df10)

head(df10, 20)

ggplot(
  data <- head(df10, 10),
  aes(x <- reorder(job, -job_income), y <-  job_income),
) + geom_col() + theme(axis.text.x = element_text(angle = 90))

ggplot(
  data <- head(df10, 10),
  aes(x <- reorder(job, job_income), y <-  job_income),
) + geom_col() + coord_flip()

df11 <- df9 %>%
  select(job, gender, income) %>%
  filter(!is.na(income) & income != 9999 & income != 0) %>%
  filter(!is.na(job)) %>%
  filter(gender == "male") %>%
  group_by(job) %>%
  summarise(job_income = mean(income), job_cnt = n()) %>%
  filter(job_cnt >= 10) %>%
  arrange(desc(job_income))

ggplot(
  data <- head(df11, 10),
  aes(x <- reorder(job, job_income), y <-  job_income),
) + geom_col() + coord_flip()

df12 <- df9 %>%
  select(job, gender, income) %>%
  filter(!is.na(income) & income != 9999 & income != 0) %>%
  filter(!is.na(job)) %>%
  filter(gender == "female") %>%
  group_by(job) %>%
  summarise(job_income = mean(income), job_cnt = n()) %>%
  filter(job_cnt >= 10) %>%
  arrange(desc(job_income))

ggplot(
  data <- head(df12, 10),
  aes(x <- reorder(job, job_income), y <-  job_income),
) + geom_col() + coord_flip()

head(df11, 10)
head(df12, 10)

rbind(df11, df12)
total_data <- bind_rows(df11, df12)
total_data

total_data$gender<- ifelse(
  is.na(total_data$gender),
  'male',
  total_data$gender
)

total_data
