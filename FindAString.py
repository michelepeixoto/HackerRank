def count_substring(s, sub_s):
    count = 0
    for i in range(len(s)):
        has_sub_s = False
        if s[i] == sub_s[0]:
            for j in range(len(sub_s)):
                try:
                    if s[i+j] == sub_s[j]:
                        #print("matched: ", s[i+j], sub_s[j])
                        has_sub_s = True
                    else:
                        #print("nope: ", s[i+j], sub_s[j])
                        has_sub_s = False
                        break
                except:
                    has_sub_s = False
                    break
            if has_sub_s == True:
                #print(i, s[i])
                count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)