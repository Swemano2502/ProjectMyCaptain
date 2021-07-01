def most_frequent():
    all_freq = {}
    test_str=input("Please enter a string")  
    for i in test_str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    print (str(all_freq))

most_frequent()
