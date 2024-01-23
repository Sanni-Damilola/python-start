values = open("file_to_read_or_write_to.txt", "w") # overide a file
# values = open("file_to_read_or_write_to.txt", "a") // update a file
newFile = open("new_file.html", "w")
values.write("\nSanni is a Dude")
newFile.write("<b>Yo!</b>")
values.close()

