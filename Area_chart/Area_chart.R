x <- seq(0, 10, length.out = 100)
y <- sin(x)

plot(x, y, type = "n", main = "Graphique d'Aire", xlab = "Temps", ylab = "Amplitude")
polygon(c(x, rev(x)), c(rep(0, length(x)), rev(y)), col = "skyblue", border = NA)
lines(x, y, col = "slateblue", lwd = 2)
