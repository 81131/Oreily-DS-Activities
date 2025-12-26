from matplotlib import pyplot as plt

years = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
gdp = [85.09,88.00,94.38,94.48,89.02,84.30,88.61,74.58,83.72,98.96]


#Format: plt.plot(xAxixData, yAxixData, color, marker, linestyle)
#Options - color: b, g, r, c, m, y, k, w, orange, purple, brown, pink, gray, olive, navy
#Options - marker: ., ,, o, v, ^, <, >, s, p, *, h, +, x, D
#Options - linestyle: solid, dashed, dashdot, dotted, -, --, -., :
plt.plot(years, gdp, color = "green", marker = 'o', linestyle = 'solid')

plt.title("Sri Lanka GPD")

plt.ylabel("Billions of $")
plt.show()