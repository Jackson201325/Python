import os

a = os.path.join("C:/Users/jacks/Desktop/Atom Python/Self-taught Programer/Challenges/Chapter 9 Files, writing, closing,etc/Testing/YouGayIfOpen.txt")


print(a)

st = open(a, "w")
st.write("You Gay")
st.close()
