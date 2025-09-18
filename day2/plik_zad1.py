# działania z plikami
# context manager
# with

# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open("test.log", "w", encoding="utf-8") as f:  # filehandler
    f.write("Powitanie\n")
    f.write("kolejne\n")
    f.write("Jescze jedno\n")

# # FileExistsError: [Errno 17] File exists: 'test.log'
# with open("test.log", "x", encoding="utf-8") as f:  # filehandler
#     f.write("Powitanie\n")
#     f.write("kolejne\n")
#     f.write("Jescze jedno\n")

# w - nadpisze dane w pliku
with open("test.log", "w", encoding="utf-8") as f:  # filehandler
    f.write("Nowe dane\n")

with open("test.log", "a", encoding="utf-8") as f:  # filehandler
    f.write("Dośpisanie\n")
    f.write("kolejne\n")
    f.write("Jescze jedno\n")

with open("test.log", "r", encoding="utf-8") as file:
    lines = file.read()

print(lines)
