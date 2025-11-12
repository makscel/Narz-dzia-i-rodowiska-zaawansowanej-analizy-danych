#zadanie 1
data <- readRDS("C:/Users/celtn/Desktop/data.rds")
head(subset(data, a != 0 & b != 0), 10)
nrow(data)
sum(is.na(data)) / (nrow(data) * ncol(data))
range(data$time)

#zadanie 2
statystyki <- function(x) {
  c(
    Min = min(x, na.rm = TRUE),
    Q1 = quantile(x, 0.25, na.rm = TRUE),
    Me = median(x, na.rm = TRUE),
    Śr = mean(x, na.rm = TRUE),
    Q3 = quantile(x, 0.75, na.rm = TRUE),
    Max = max(x, na.rm = TRUE)
  )
}

cat("Statystyki dla zmiennej 'a':\n")
print(statystyki(data$a))

cat("\nStatystyki dla zmiennej 'b':\n")
print(statystyki(data$b))

#zadanie 3
przedzialy <- c(0, 5, 10, 20, 30, 40, 80, Inf)
etykiety <- c("[0,5)", "[5,10)", "[10,20)", "[20,30)", "[30,40)", "[40,80)", "[80,Inf)")

rozkład_procentowy <- function(x) {
  x_cut <- cut(x, breaks = przedzialy, labels = etykiety, right = FALSE)
  prop <- prop.table(table(x_cut)) * 100
  wynik <- setNames(as.numeric(prop[etykiety]), etykiety)
  wynik[is.na(wynik)] <- 0
  return(round(wynik, 2))
}

a_proc <- rozkład_procentowy(na.omit(data$a))
b_proc <- rozkład_procentowy(na.omit(data$b))

tabela <- data.frame(
  zakres = etykiety,
  `a [%]` = a_proc,
  `b [%]` = b_proc
)
print(tabela)

#zadanie 4
data <- data[order(data$time), ]

braki <- is.na(data$a)

grupa <- integer(length(braki))
blok_id <- 0
for (i in seq_along(braki)) {
  if (braki[i]) {
    grupa[i] <- blok_id
  } else {
    blok_id <- blok_id + 1
    grupa[i] <- blok_id
  }
}

data$brak_a <- braki
data$grupa <- grupa

braki_data <- data[data$brak_a, ]

grupy_unikalne <- unique(braki_data$grupa)
czas_start <- tapply(braki_data$time, braki_data$grupa, min)
czas_koniec <- tapply(braki_data$time, braki_data$grupa, max)
dlugosc <- as.numeric(difftime(czas_koniec, czas_start, units = "secs")) + 1

dlugosc <- dlugosc[dlugosc > 0]

granice <- c(
  0, 30, 60, 5*60, 15*60, 30*60, 60*60,
  3*60*60, 6*60*60, 12*60*60, 24*60*60, 2*24*60*60, Inf
)
etykiety <- c(
  "(0, 30s)", "[30s, 1min)", "[1min, 5min)", "[5min, 15min)", "[15min, 30min)",
  "[30min, 1h)", "[1h, 3h)", "[3h, 6h)", "[6h, 12h)", "[12h, 1d)", "[1d, 2d)", ">= 2d"
)

przedzialy <- cut(dlugosc, breaks = granice, labels = etykiety, right = FALSE)

tabela <- as.data.frame(table(przedzialy))
colnames(tabela) <- c("przedział", "liczba")

print(tabela)

#zadanie 5
data$time <- as.POSIXct(data$time)

data$czas_10min <- as.POSIXct(cut(data$time, breaks = "10 min"))

srednie_lista <- tapply(data$a, data$czas_10min, function(x) mean(x, na.rm = TRUE))

czas_sredni <- as.POSIXct(names(srednie_lista))
srednia_a <- as.numeric(srednie_lista)

plot(czas_sredni, srednia_a, type = "o", col = "blue",
     xlab = "Czas", ylab = "Średnia a",
     main = "Średnia wartość zmiennej 'a' w przedziałach 10-minutowych")

#zadanie 6
hist(data$a,
     breaks = 30,
     main = "Histogram zmiennej 'a'",
     xlab = "Wartości a",
     ylab = "Liczba wystąpień (log)",
     col = "skyblue",
     border = "white",
     yaxt = "n"                
)

ticks <- axTicks(2) 
log_ticks <- ticks[ticks > 0]   
axis(2, at = log_ticks, labels = log10(log_ticks))
box()

plot_vals <- hist(data$a, breaks = 30, plot = FALSE)
counts <- plot_vals$counts
plot_vals$counts <- log10(counts + 1)
plot(plot_vals, col = "skyblue", border = "white",
     main = "Histogram zmiennej 'a' (skala log y)",
     xlab = "Wartości a", ylab = "log10(Liczba wystąpień)")

