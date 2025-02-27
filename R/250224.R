# name = c("A", "B", "C", "D", "E")
# grade = c(1,3,2,1,2)
# student = data.frame(name, grade)

# midterm = c(80,70,90,60,80)
# final = c(70,90,80,80,80)
# scores = cbind(midterm, final)

# gender = c("M", "F", "F", "F", "M")
# students = data.frame(student, gender, scores)

# total_score = midterm + final
# cbind(students, total_score)

# new_student = data.frame(name="F", grade=2, gender="M", midterm=90, final=80)
# rbind(students,new_student)

# students$sum <- ifelse(students$midterm + students$final >= 150, "pass", "fail")

# students <- students %>% mutate(total = midterm + final, mean = (midterm + total)/2) # nolint

# table(students$grade)

# students$pass <- students$sum
# students$sum <- NULL
# students[order(students$final, decreasing = FALSE)]
# students

# r1 <- 0
# r2 <- 0
# 
# while (r1 + r2 != 10) {
#   r1 <-int(readline('insert plseas : '))
#   r1 <- as.integer(r1)
#   r2 <-int(readline('insert plseas : '))
#   r2 <- as.integer(r2)
#   
#   if(r1 + r2 == 10) {
#     print(r1, r2)
#     break
#   }
# }

# for(i in 1:6) {
#   for(j in 1:6) {
#     if(i + j == 10) {
#       print(c(i,j))
#     }
#   }
# }

# r1 <- 1
# r2 <- 1
# 
# while (r1 < 7) {
#   while (r2 < 7) {
#     if(r1 + r2 == 10) {
#       print(c(i,j))
#     }
#     r2 <- r2 + 1
#   }
#   r1 <- r1 + 1
# }
# 
# func_1 <- function() {
#   print("hello R")
# }
# 
# func_1()

# func_3 <- function(a,b){
#   result <- a + b
#   return (result)
# }
# 
# func_3(3,4)

# 기본 값이 있는 매개변수
# func_4 <- function(a,b=3) {
#   return (a+b)
# }

# func_4(7)

# func_5 <- function(a,b=3,c=8) {
#   return (a+b+c)
# }

# func_5(7)

# func_5(3,,2)

# func_6 <- function(x,...) {
#   print(c(x, summary(...)))
# }

# v <- 1:10

# func_6("Summary ", v)

# sum <- 0

# for (i in 10:1) {
#   sum <- sum + i
# }

# print(sum)

# mean_func <- function(v) {
#   count <- 0
#   sum <- 0
#   for (i in v) {
#     count <- count + 1
#     sum <- sum + i
#   }
#   return (sum/count)
# }

# mean_func(c(1,2,3,4,5,5,5,5,6))


