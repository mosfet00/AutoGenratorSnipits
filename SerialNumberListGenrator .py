#Remotwell vfd                   RWVF03240100
#Em sknit and sfill and s pump   SFST04240100
#skem old                        SKEM03240100
#em96                            EM9601240100
#smartkinit CE                   SKMM07240100



# Define the base string and the range
base_string = "RWVF03240100"  # Base string to be used in the sequence
start = 1  # Starting number for the sequence
end = 95  # Ending number for the sequence
threshold = 100  # Threshold to switch from '+' to '-'

# Loop through the range and format the strings
for i in range(start, end + 1):
    if i <= threshold:
        # Format with '+' for numbers up to the threshold
        print(f"[+{base_string}{i:002d}N+]")
    else:
        # Format with '-' for numbers above the threshold
        print(f"[-{base_string}{i:002d}N-]")