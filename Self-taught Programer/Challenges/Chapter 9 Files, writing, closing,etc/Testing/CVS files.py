import csv
import os

a = os.path.join("C:/Users/jacks/Desktop/Atom Python/Self-taught Programer/Challenges/Chapter 9 Files, writing, closing,etc/Testing/st.csv")

with open (a, "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(["one","two","three"])
    write.writerow(["four","five","six"])
print(write)
