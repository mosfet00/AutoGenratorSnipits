#Rewellx vfd                     RWVF03240100
#Em sknit and sfill and s pump   SFST04240100
#skem old                        SKEM03240100
#em96                            EM9601240100
#smartkinit CE                   SKMM07240100
#Rewellx MAX v2                  RWMX02240200
#Rewellx MAX v2.0 (Black)        RWMX02250200  RWMX-51 - GSMtested-01
#Rewellx VFD v3.1                RWVD03250200



# Define the base string and the range
base_string = "RSKMM07240100"  # Base string to be used in the sequence
start = 161  # Starting number for the sequence
end = 30  # Ending number for the sequence
threshold = 1  # Threshold to switch from '+' to '-'

# Loop through the range and format the strings
for i in range(start, end + 1):
    if i <= threshold:
        # Format with '+' for numbers up to the threshold
        print(f"[+{base_string}{i:002d}N+]")
    else:
        # Format with '-' for numbers above the threshold
        print(f"[-{base_string}{i:002d}N-]")




# GSM LIST  - [+GSMtested-100+]

# tools https://phrasefix.com/tools/merge-text/


# # Define the base string and the range
# base_string = "GSMtested-"  # Base string to be used in the sequence
# start = 1  # Starting number for the sequence
# end = 100  # Ending number for the sequence
# threshold = 100  # Threshold to switch from '+' to '-'

# # Loop through the range and format the strings
# for i in range(start, end + 1):
#     if i <= threshold:
#         # Format with '+' for numbers up to the threshold
#         print(f" - [+{base_string}{i:002d}N+]")
#     else:
#         # Format with '-' for numbers above the threshold
#         print(f"[-{base_string}{i:002d}N-]")
        
