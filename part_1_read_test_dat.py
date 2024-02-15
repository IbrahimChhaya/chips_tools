import cc_dat_utils

#Part 1
input_dat_file = "data/pfgd_test.dat"

print(cc_dat_utils.make_cc_level_pack_from_dat(input_dat_file))

whileLoop = True
while whileLoop:
    letter = input("magic letter?")
    if letter.lower() == 's':
        whileLoop = False


#Use cc_dat_utils.make_cc_level_pack_from_dat() to load the file specified by input_dat_file
#print the resulting data
